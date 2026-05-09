from fastapi import FastAPI

app = FastAPI(
    title="Mega AI",
    description="Production-Grade Multi-Agent LLM Orchestration System",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Mega AI backend is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }