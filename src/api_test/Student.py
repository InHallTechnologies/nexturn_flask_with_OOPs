class Student:
    def __init__(self, student_id, name, age,course,marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A"

        elif 60 <= self.marks < 80:
            return "B"

        elif 40 <= self.marks < 60:
            return "C"

        else:
            return "F"

    def get_details(self):
        return {
            "name":self.name,
            "age":self.age,
            "course":self.course,
            "marks":self.marks,
            "student_id": self.student_id
        }

    def update_marks(self, new_marks):
        self.marks = new_marks

    def __str__(self):
        return f"""
        {'*'*10}
        name: {self.name}
        student_id: {self.student_id},
        age:{self.age}
        course: {self.course}
        marks: {self.marks}
        """