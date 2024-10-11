

class Student:
    def __init__(
            self,
            name: str,
            age: int,
    ):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name should be string")

student = Student(
    name="Rahul",
    age=20
)
print(student.name)
student.__name = "Kunal"
print(student.__name)