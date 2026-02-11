from fastapi import APIRouter

router = APIRouter(prefix="/platillos")

@router.get("/")
async def listar_platillos():
    return []
