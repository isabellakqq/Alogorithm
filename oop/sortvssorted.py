class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [
Student('john', 'A', 15),
Student('jane', 'B', 12),
Student('dave', 'B', 10),
]
new_list = sorted(student_objects, key=lambda student: student.age, reverse=True) 
  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(new_list)

