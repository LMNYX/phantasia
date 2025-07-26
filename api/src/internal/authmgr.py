import hashlib
from functools import wraps
import inspect
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from src.models.user import User


api_key_header_scheme = APIKeyHeader(name="Authorization", auto_error=False)

async def _get_current_user(authorization: str | None = Depends(api_key_header_scheme)) -> User:
    if authorization is None or not authorization.startswith("Token "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided.",
            headers={"WWW-Authenticate": "Token"},
        )
    
    token = authorization.split(" ")[1]
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    
    user = await User.get_or_none(access_key=hashed_token)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token.",
        )
        
    return user

def requires_auth(permissions_required: List[str] | None = None):
    def decorator(func):
        async def _check_permissions(user: User = Depends(_get_current_user)):
            if permissions_required:
                user_permissions = getattr(user, 'permissions', [])
                if "SUPERUSER" not in user_permissions and not all(p in user_permissions for p in permissions_required):
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="You do not have sufficient permissions to perform this action.",
                    )
            return user

        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        sig = inspect.signature(func)
        
        params = [p for p in sig.parameters.values() if p.name != 'user']

        user_param = inspect.Parameter(
            "user",
            inspect.Parameter.KEYWORD_ONLY,
            default=Depends(_check_permissions),
            annotation=User,
        )
        params.append(user_param)
        
        wrapper.__signature__ = sig.replace(parameters=params)
        
        return wrapper
    return decorator
