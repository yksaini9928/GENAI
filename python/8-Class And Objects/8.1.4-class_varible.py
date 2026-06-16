"""class variable are shared across all instances of the class. They are defined within the class but outside any instance methods. Class variables are used to store data that is common to all instances of the class.
"""
from unicodedata import name


class Student:
    # class variable
    school_name = "ABC School"
    department = ["Computer Science", "Mathematics", "Physics"]


    def __init__(self, name, roll_number, age):
        print(f"calling the initializer for {self}!")
        self.name = name  # instance variable
        self.roll_number = roll_number  # instance variable 
        self.age = age    # instance variable

    def study(self,n_hours):
        print(f"{self.name} is studying for {n_hours} hours.")

    def sports(self,sports_name):
        print(f"{self.name} is playing {sports_name}.")


student1 = Student(name="yogesh", roll_number=101, age=28)
student2 = Student(name="Krish", roll_number=102, age=32)


print(student1.__dict__) # {'name': 'yogesh', 'roll_number': 101, 'age': 28}

print(student1.department)
print(student2.department)

