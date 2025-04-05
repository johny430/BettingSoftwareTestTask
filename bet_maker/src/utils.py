import json
from typing import Any


def safe_json_loads(value: Any):
    try:
        return json.loads(value)
    except Exception:
        return None
