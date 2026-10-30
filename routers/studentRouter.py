from fastapi import APIRouter, Response
from models.studentModel import Student

from controller.studentController import (
    create_student_controller,
    get_students_controller,
    get_student_controller,
    update_student_controller,
    delete_student_controller
)

StudentRouter = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@StudentRouter.post("/")
def create_student(student: Student, response: Response):
    return create_student_controller(student, response)


@StudentRouter.get("/")
def get_students():
    return get_students_controller()


@StudentRouter.get("/{student_id}")
def get_student(student_id: int, response: Response):
    return get_student_controller(student_id, response)


@StudentRouter.put("/{student_id}")
def update_student(student_id: int, student: Student, response: Response):
    return update_student_controller(student_id, student, response)


@StudentRouter.delete("/{student_id}")
def delete_student(student_id: int, response: Response):
    return delete_student_controller(student_id, response)
