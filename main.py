from fastapi import FastAPI
import uvicorn


app = FastAPI()




if __name__ == "__main__":
    uvicorn.run("main:routers",host="localhost", reload=True)