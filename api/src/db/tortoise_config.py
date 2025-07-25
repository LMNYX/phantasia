import os

def find_model_modules(base_package="src.models", base_path="src/models"):
    modules = []
    for filename in os.listdir(base_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # strip .py
            modules.append(f"{base_package}.{module_name}")
    return modules

model_modules = find_model_modules()

TORTOISE_ORM = {
    "connections": {
        "default": os.environ["DATABASE_URL"],
    },
    "apps": {
        "models": {
            "models": model_modules + ["aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}
