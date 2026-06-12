# creating a class
class MyClass:
    pass 


#crearting an object of the class
obj1 =MyClass()
obj2 =MyClass()

# obj1 and obj2 are two different objects of the same class
l1 =[10,12,34]
print(type(l1)) # <class 'list'>
print(type(obj1)) # <class '__main__.MyClass'>
print(type(obj2)) # <class '__main__.MyClass'>