from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from typing import List

from src.models.user import User
from src.models.invite import Invite
from src.internal.authmgr import requires_auth
from src.internal.error import ErrorDetails
from src.utils.random import generate_random_string
from src.internal.permissions import UserPermissions

router = APIRouter(prefix="/invites", tags=["Invites"])

class InvitationUsed(BaseModel):
    access_key: str
    username: str

@router.patch("/use", status_code=200,
            summary="Creates a new user from an invitation code",
            description="Creates a new user from an invitation code",
            responses={
                status.HTTP_200_OK: {"model": InvitationUsed},
                status.HTTP_400_BAD_REQUEST: {"model": ErrorDetails}
            })
async def create_new_invite(invitation_code: str, response: Response):
    
    invitation_object = await Invite.filter(inviation_code=invitation_code).first()

    if not invitation_object:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorDetails(error=f"Invalid invitation code provided", status_code=status.HTTP_400_BAD_REQUEST)

    username = invitation_object.username

    if await User.exists_by_username(username):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorDetails(error=f"User already exists with username provided", status_code=status.HTTP_400_BAD_REQUEST)

    new_user = await User.create_with_token(username=username, permissions=["USER_ALL"])
    await Invite.filter(inviation_code=invitation_code).delete()

    return InvitationUsed(access_key=new_user[1], username=username)