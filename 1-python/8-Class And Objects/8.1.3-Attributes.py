class Student:
    pass
student1 = Student()
student2 = Student()

student1.name = "Yogesh"
student1.age = 28


print(student1.name) # Yogesh
print(student1.age) # 28
print(student1.__dict__) # {'name': 'Yogesh', 'age': 28}