from .Student import Student
student_list = []

class StudentManager:
    def add_student(self, student_id, name, age,course,marks ):
        s1 = Student(student_id, name, age,course,marks)
        student_list.append(s1)

    def find_student_by_id(self, student_id):
        filtered_list = list(filter(lambda x: x.student_id ==  student_id, student_list))
        if len(filtered_list) != 0:
            return filtered_list[0]
        else:
            return None

    def update_student_details(self, student_id ,updates):
        student = self.find_student_by_id(student_id)
        current_stats = {
            "name":student.name,
            "age":student.age,
            "course":student.course,
            "marks":student.marks,
            "student_id": student.student_id,
            **updates
        }

        for index, student in enumerate(student_list):
            if student.student_id == student_id:
                student_list[index] = Student(
                    student_id=current_stats['student_id'],
                    name=current_stats['name'],
                    age=current_stats['age'],
                    course=current_stats['course'],
                    marks=current_stats['marks']
                )
                break

    def delete_student(self, student_id):
        to_be_deleted = -1
        for index, student in enumerate(student_list):
            if student.student_id == student_id:
                to_be_deleted = index

        if to_be_deleted != -1:
            student_list.pop(to_be_deleted)
        else:
            print("Student Id Not Found!")      

    def get_students_list(self):
        temp = map(lambda x: { "name": x.name,  "age":x.age, "course":x.course, "marks":x.marks, "student_id":x.student_id }, student_list)
        return list(temp)

    def get_passed_student_list(self):
        return list(filter(lambda x: x.calculate_grade() != "F", student_list))