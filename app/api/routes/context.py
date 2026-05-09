from fastapi import APIRouter

from app.memory.context import SharedContext

router = APIRouter()


@router.get("/context-demo")
async def context_demo():
    context = SharedContext(
        user_query="Compare Tesla and BYD battery strategy"
    )

    return context