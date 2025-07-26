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

class NewInvitationCreated(BaseModel):
    inviation_code: str

@router.get("/create", status_code=201,
            summary="Creates an invitation code for a new user",
            description="Creates an invitation code for a new user",
            responses={
                status.HTTP_200_OK: {"model": NewInvitationCreated},
                status.HTTP_400_BAD_REQUEST: {"model": ErrorDetails}
            })
@requires_auth(permissions_required=[UserPermissions.INVITE_CREATE])
async def create_new_invite(username: str, response: Response, *,
    user: User):
    
    if await User.exists_by_username(username):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorDetails(error=f"User already exists with username provided", status_code=status.HTTP_400_BAD_REQUEST)

    inviation_code = generate_random_string(16)

    new_invite = await Invite.create(
        username=username,
        inviter=user,
        inviation_code=inviation_code
    )

    return NewInvitationCreated(inviation_code=inviation_code)