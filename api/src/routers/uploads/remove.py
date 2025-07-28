from fastapi import APIRouter, Response, status
from src.models.user import User
from src.models.upload import Upload
from src.internal.authmgr import requires_auth
from src.internal.success import SuccessMessage
from src.internal.error import ErrorDetails
from src.internal.permissions import UserPermissions

router = APIRouter(prefix="/uploads", tags=["Uploads"])

@router.delete("/remove", status_code=200,
            summary="Deletes a file from the file server",
            description="Deletes a file from the file server",
            responses={
                status.HTTP_200_OK: {"model": SuccessMessage},
                status.HTTP_400_BAD_REQUEST: {"model": ErrorDetails}
            })
@requires_auth(permissions_required=[UserPermissions.USER_UPLOAD])
async def delete_upload(upload_id: int, response: Response, *, 
    user: User):

    upload = await Upload.filter(id=upload_id).select_related("user").first()

    if not upload:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ErrorDetails(error=f"Invalid upload id provided", status_code=status.HTTP_400_BAD_REQUEST)

    if upload.user.id != user.id and not user.has_permission("DELETE_OTHER_UPLOADS"):
        response.status_code = status.HTTP_403_FORBIDDEN
        return ErrorDetails(error=f"You do not have permission to delete this upload", status_code=status.HTTP_403_FORBIDDEN)

    await upload.delete()

    return SuccessMessage(success=True)
