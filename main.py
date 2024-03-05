from fastapi import FastAPI
import uvicorn
from routers import users

app = FastAPI()


app.include_router(users.router, prefix="/api", tags=["Users"])


if __name__ == "__main__":
    uvicorn.run("main:routers",host="localhost", reload=True)