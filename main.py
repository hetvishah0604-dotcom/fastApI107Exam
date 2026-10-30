from fastapi import FastAPI
from routers.studentRouter import StudentRouter

app = FastAPI()

app.include_router(StudentRouter)


@app.get("/")
def home():
    return {
        "isSuccess": True,
        "message": "Welcome to Student Management API"
    }
