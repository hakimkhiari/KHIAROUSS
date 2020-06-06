class dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

d = dog("Kelb", 43)
d.set_age(22)
print(d.get_age())





class dog:
    def __int__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self):
        self.age = age

    d = dog("hugo", 23)
    print(d.get_name())
    d.set_age(11)
    print(d.get_age())



class Student:
    def __int__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class course:
    def __int__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_students(self, student):
        if len(self.students) < max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Karim", 19, 95)
s2 = Student("Hakim", 19, 80)
s3 = Student("Faouzzi", 19, 65)

course = course("Finance", 3)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)
print(course.get_average_grade())



























