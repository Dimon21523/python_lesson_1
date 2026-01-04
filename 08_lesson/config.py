import os


def get_base_url() -> str:
    base_url = os.getenv("YOUGILE_BASE_URL")
    if not base_url:
        raise RuntimeError("YOUGILE_BASE_URL is not set")
    return base_url.rstrip("/")


def get_token() -> str:
    token = os.getenv("YOUGILE_TOKEN")
    if not token:
        raise RuntimeError("YOUGILE_TOKEN is not set")
    return token
