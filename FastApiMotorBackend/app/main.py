from fastapi import FastAPI
from app.routers import user_route

app = FastAPI()

app.include_router(user_route.router, prefix="/api", tags=["user"])

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
