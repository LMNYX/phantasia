import hashlib
from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True, generated=True, unique=True, null=False)
    username = fields.CharField(max_length=255, unique=True)
    access_key = fields.CharField(max_length=255)
    permissions = fields.JSONField(default=['USER_ALL'])
    is_banned = fields.BooleanField(default=False)
    badges = fields.JSONField(default=[])
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    views = fields.IntField(default=0)
    uploads = fields.IntField(default=0)
    twitch_user_id = fields.CharField(max_length=255, null=True)

    def encrypt_access_key(self):
        sha_signature = hashlib.sha256(self.access_key.encode()).hexdigest()
        return sha_signature
    
    def compare_access_key(self, access_key):
        sha_signature = hashlib.sha256(access_key.encode()).hexdigest()
        return sha_signature == self.access_key

    class Meta:
        table = "users"
