from fastapi import APIRouter

from src.web.v1.line_router import line_router

router = APIRouter()
router.include_router(line_router, prefix='/events')
