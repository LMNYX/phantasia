import hashlib
import uuid
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
    upload_count = fields.IntField(default=0)
    twitch_user_id = fields.CharField(max_length=255, null=True)

    @classmethod
    async def create_with_token(cls, **kwargs):
        raw_token = str(uuid.uuid4())
        token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
        user = await cls.create(access_key=token_hash, **kwargs)
        return user, raw_token

    def encrypt_access_key(self):
        sha_signature = hashlib.sha256(self.access_key.encode()).hexdigest()
        return sha_signature

    def compare_access_key(self, access_key):
        sha_signature = hashlib.sha256(access_key.encode()).hexdigest()
        return sha_signature == self.access_key
    
    def has_permission(self, permission):
        return (permission in self.permissions
            or 'SUPERUSER' in self.permissions
            or 'ADMINISTRATOR' in self.permissions)

    @classmethod
    async def exists_by_access_key(cls, access_key: str) -> bool:
        hashed_key = hashlib.sha256(access_key.encode()).hexdigest()
        return await cls.filter(access_key=hashed_key).exists()
    
    @classmethod
    async def exists_by_username(cls, username: str) -> bool:
        return await cls.filter(username=username).exists()

    @classmethod
    async def find_by_id(cls, user_id: int):
        return await cls.get(id=user_id)

    @classmethod
    async def find_by_username(cls, username: str):
        return await cls.get(username=username)

    @classmethod
    async def find_by_access_key(cls, access_key: str):
        hashed_key = hashlib.sha256(access_key.encode()).hexdigest()
        return await cls.get(access_key=hashed_key)

    class Meta:
        table = "users"
