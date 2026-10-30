from fastapi import Response
from models.studentModel import Student

students = []
student_id = 0


def create_student_controller(student: Student, response: Response):
    global student_id
    student_id += 1
    student.id = student_id
    students.append(student)
    response.status_code = 201
    return {
        "isSuccess": True,
        "message": "Student created successfully",
        "student": student
    }


def get_students_controller():
    return {
        "isSuccess": True,
        "students": students
    }


def get_student_controller(student_id: int, response: Response):
    for student in students:
        if student.id == student_id:
            return {"isSuccess": True, "student": student}

    response.status_code = 404
    return {"isSuccess": False, "message": "Student not found"}


def update_student_controller(student_id: int, student: Student, response: Response):
    for i, existing_student in enumerate(students):
        if existing_student.id == student_id:
            student.id = student_id
            students[i] = student
            return {
                "isSuccess": True,
                "message": "Student updated successfully",
                "student": student
            }

    response.status_code = 404
    return {"isSuccess": False, "message": "Student not found"}


def delete_student_controller(student_id: int, response: Response):
    for i, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(i)
            return {
                "isSuccess": True,
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    response.status_code = 404
    return {"isSuccess": False, "message": "Student not found"}
