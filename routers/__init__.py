from aiogram import Router
from .start import router as start_router
from .filters import router as filters_router


router = Router()

router.include_router(start_router)
router.include_router(filters_router)

