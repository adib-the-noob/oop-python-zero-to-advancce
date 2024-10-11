class Student:
    session = '2021-2022'
    assigned_student = 0 # class variable
    
    def __init__(self, name, age, grade, is_good):
        self.name = name
        self.age = age
        self.grade = grade
        self.is_good = is_good
        Student.assigned_student += 1    

student1 = Student(
    'John',
    21,
    'A',
    True,
)
student2 = Student(name='Jane', age=22, grade='B', is_good=False)
student3 = Student(name='Joe', age=23, grade='C', is_good=True)
student4 = Student(name='Jack', age=24, grade='D', is_good=False)


print(student1.name)
print(Student.session)
print(Student.assigned_student)