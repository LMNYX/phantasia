from fastapi import APIRouter, Response, status
from src.models.user import User
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

class AuthenticatedUserDetails(BaseModel):
    id: int
    username: str
    permissions: List[str]
    is_banned: bool

class AuthenticatedUser(BaseModel):
    authenticated: bool
    user: AuthenticatedUserDetails


@router.get("/authenticate", status_code=200,
            response_model=AuthenticatedUser,
            summary="Authenticate a user",
            description="Authenticate a user",
            responses={
                status.HTTP_200_OK: {"model": AuthenticatedUser},
                status.HTTP_401_UNAUTHORIZED: {"model": AuthenticatedUser}
            })
async def user_authenticate(access_key: str, response: Response):
    if await User.exists_by_access_key(access_key):
        user_data = await User.find_by_access_key(access_key)
        return AuthenticatedUser(
            authenticated=True,
            user=AuthenticatedUserDetails(
                id=user_data.id,
                username=user_data.username,
                permissions=user_data.permissions,
                is_banned=user_data.is_banned
            )
        )
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return AuthenticatedUser(authenticated=False, user=None)
