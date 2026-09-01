from flask import Flask, request
from .StudentManager import StudentManager
from uuid import uuid4

app = Flask(__name__)
manager = StudentManager()

@app.get('/')
def handle_root():
    return {"message": "Flask API is running on Vercel", "status": 200, "success": True}

@app.post('/students')
def handle_add_student():
    body_params = request.json
    manager.add_student(
        name=body_params['name'],
        age=body_params['age'],
        marks=body_params['marks'],
        course=body_params['course'],
        student_id=str(uuid4())
    )
    return {"message":"Student Added Successfully", 'status':201, "success":True}, 201


@app.get('/students')
def get_all_students():
    return manager.get_students_list()


@app.get("/students/<student_id>")
def get_student_by_id(student_id):
    found_item = manager.find_student_by_id(student_id)
    if not found_item:
        return "NOT FOUND", 404
    else:
        return {
            "name":found_item.name,
            "age":found_item.age,
            "marks":found_item.marks,
            "course":found_item.course,
            "student_id":found_item.student_id
        }

@app.get("/test")
def handle_test():
    return "WORKING"

if __name__ == "__main__":
    app.run(debug=True, port=8000)