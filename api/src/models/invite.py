from tortoise import fields
from tortoise.models import Model
from src.models.user import User

class Invite(Model):
    id = fields.IntField(pk=True, generated=True, unique=True, null=False)
    inviter = fields.ForeignKeyField("models.User", related_name="invites")
    username = fields.CharField(max_length=255)
    inviation_code = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "invites"