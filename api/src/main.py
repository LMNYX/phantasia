import sys
import importlib
import pkgutil
from fastapi import FastAPI
from pathlib import Path
from tortoise.contrib.fastapi import register_tortoise

from src.db.tortoise_config import TORTOISE_ORM

app = FastAPI(
    title="Phantasia API",
    description="",
    version="1.0.0"
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


@app.get("/")
async def root():
    return {"message": "Phantasia API"}


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)
