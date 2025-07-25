from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "invites" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL,
    "inviation_code" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "inviter_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        ALTER TABLE "users" ADD "twitch_user_id" VARCHAR(255);
        ALTER TABLE "users" RENAME COLUMN "uploads" TO "upload_count";
        CREATE TABLE IF NOT EXISTS "uploads" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "filename" VARCHAR(255) NOT NULL,
    "mimetype" VARCHAR(255) NOT NULL,
    "file_hash" VARCHAR(255) NOT NULL,
    "internal_name" VARCHAR(255) NOT NULL,
    "views" INT NOT NULL DEFAULT 0,
    "filesize" BIGINT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME COLUMN "upload_count" TO "uploads";
        ALTER TABLE "users" DROP COLUMN "twitch_user_id";
        DROP TABLE IF EXISTS "uploads";
        DROP TABLE IF EXISTS "invites";"""
