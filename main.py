from fastapi import FastAPI
import uvicorn
from routers import users, products

app = FastAPI()


app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(products.router, prefix="/api", tags=["Products"])


if __name__ == "__main__":
    uvicorn.run("main:routers",host="localhost", reload=True)