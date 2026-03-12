import sys
import importlib
import pkgutil
import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from tortoise.contrib.fastapi import register_tortoise
from botocore.exceptions import ClientError
from src.internal.s3 import get_s3_client
from src.db.tortoise_config import TORTOISE_ORM

app = FastAPI(
    title="Phantasia API",
    description="",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(?:.+\.)?uwu\.(?:local|so)(?::\d+)?",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
ROUTERS_DIR = BASE_DIR / "routers"
ROUTERS_PACKAGE = "src.routers"

PARENT_DIR = BASE_DIR.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.insert(0, str(PARENT_DIR))


def load_routers(path: Path, package: str):
    for _, module_name, is_pkg in pkgutil.iter_modules([str(path)]):
        if module_name == "__init__":
            continue

        full_module = f"{package}.{module_name}"

        try:
            module = importlib.import_module(full_module)
            router = getattr(module, "router", None)
            if router:
                app.include_router(router)
                print(f"Loaded: {full_module}")
        except Exception as e:
            print(f"Failed to load {full_module}: {e}")

        if is_pkg:
            load_routers(path / module_name, f"{package}.{module_name}")


load_routers(ROUTERS_DIR, ROUTERS_PACKAGE)

@app.on_event("startup")
async def startup_event():
    pass
    s3 = get_s3_client()
    s3_domain = os.getenv("S3_DOMAIN")
    bucket_name = os.getenv("S3_BUCKET_NAME")
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' already exists.")
    except ClientError as e:
        error_code = int(e.response["Error"]["Code"])
        if error_code == 404:
            s3.create_bucket(Bucket=bucket_name)
            print(f"S3 bucket '{bucket_name}' created.")
        else:
            raise RuntimeError(f"Error checking/creating bucket: {e}")
    public_read_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowPublicRead",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
            }
        ]
    }

    try:
        s3.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(public_read_policy)
        )
        print(f"Public-read policy applied to bucket '{bucket_name}'.")
    except ClientError as e:
        raise RuntimeError(f"Error applying bucket policy: {e}")

    app.state.s3_client = s3
    app.state.s3_bucket = bucket_name
    app.state.s3_domain = s3_domain


@app.get("/")
async def root():
    return {"message": "Phantasia API"}


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)