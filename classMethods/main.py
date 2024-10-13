class Student:
    total_student = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.total_student += 1
        Student.total_gpa += gpa
        
    @classmethod
    def get_total_student(cls):
        return cls.total_student
    
    @classmethod
    def get_average_gpa(cls):
        return cls.total_gpa / cls.total_student
    

student1 = Student("Alice", 3.5)
student2 = Student("Bob", 3.0)
student3 = Student("Charlie", 3.2)

print(Student.get_total_student())  # 3
print(Student.get_average_gpa())  # 3.2333333333333334

