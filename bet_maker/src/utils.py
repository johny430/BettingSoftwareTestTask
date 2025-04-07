import json
from typing import Any


def safe_json_loads(value: Any) -> Any:
    try:
        return json.loads(value)
    except ValueError:
        return None
