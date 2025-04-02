from fastapi import APIRouter

from web.v1.bet_router import bet_router

router = APIRouter()
router.include_router(bet_router)
