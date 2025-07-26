from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from typing import List

from src.models.user import User
from src.models.invite import Invite
from src.internal.authmgr import requires_auth
from src.internal.error import ErrorDetails
from src.internal.success import SuccessMessage
from src.utils.random import generate_random_string
from src.internal.permissions import UserPermissions

router = APIRouter(prefix="/invites", tags=["Invites"])

class InvitationUsed(BaseModel):
    access_key: str
    username: str

@router.delete("/remove", status_code=200,
            summary="Deletes an invitation code",
            description="Deletes an invitation code",
            responses={
                status.HTTP_200_OK: {"model": SuccessMessage},
                status.HTTP_400_BAD_REQUEST: {"model": ErrorDetails}
            })
@requires_auth(permissions_required=[UserPermissions.INVITE_DELETE])
async def create_new_invite(invitation_code: str, response: Response, *,
    user: User):
    
    invitation_object = await Invite.filter(inviation_code=invitation_code).first()

    if not invitation_object:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorDetails(error=f"Invalid invitation code provided", status_code=status.HTTP_400_BAD_REQUEST)

    await Invite.filter(inviation_code=invitation_code).delete()

    return SuccessMessage(success=True)