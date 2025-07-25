import hashlib
from tortoise import fields
from tortoise.models import Model
from src.models.user import User

class Upload(Model):
    id = fields.IntField(pk=True, generated=True, unique=True, null=False)
    user = fields.ForeignKeyField("models.User", related_name="uploads")
    filename = fields.CharField(max_length=255)
    mimetype = fields.CharField(max_length=255)
    file_hash = fields.CharField(max_length=255)
    internal_name = fields.CharField(max_length=255)
    views = fields.IntField(default=0)
    filesize = fields.BigIntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)

    def encrypt_file_hash(self):
        sha_signature = hashlib.sha256(self.file_hash.encode()).hexdigest()
        return sha_signature

    def get_bucket_location(self):
        return f"{self.user.username}/{self.internal_name}"

    class Meta:
        table = "uploads"