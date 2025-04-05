from fastapi import HTTPException


async def get_or_raise(result, error_code: int, error_message: str):
    if not result:
        raise HTTPException(status_code=error_code, detail=error_message)
    return result
