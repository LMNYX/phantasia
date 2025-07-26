from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from typing import List

from src.models.user import User
from src.internal.authmgr import requires_auth
from src.internal.error import ErrorDetails
from src.internal.success import SuccessMessage
from src.internal.permissions import UserPermissions

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/ban", status_code=200,
            summary="Creates a new ban entry for a user",
            description="Creates a new ban entry for a user",
            responses={
                status.HTTP_200_OK: {"model": SuccessMessage},
                status.HTTP_400_BAD_REQUEST: {"model": ErrorDetails}
            })
@requires_auth(permissions_required=[UserPermissions.BAN_USERS])
async def ban_user(target: str, response: Response, *,
    user: User):
    
    if target == user.username:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorDetails(error=f"You cannot ban yourself", status_code=status.HTTP_400_BAD_REQUEST)
    
    if not await User.exists_by_username(target):
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorDetails(error=f"User does not exist", status_code=status.HTTP_404_NOT_FOUND)

    new_ban_history_entry = {
        "banned_by": user.username,
        "banned_at": str(user.created_at),
        "reason": None,
        "unbanned_by": None,
        "unbanned_at": None
    }

    await User.filter(username=target).update(is_banned=True, ban_history=[*user.ban_history, new_ban_history_entry])

    return SuccessMessage(success=True)