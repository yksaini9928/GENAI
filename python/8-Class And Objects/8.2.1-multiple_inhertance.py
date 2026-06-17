# single level inheritance

class A:
    def state_1(self):
        print("This is state 1 of class A")

    def state_2(self):
        print("This is state 2 of class A")

    def state_3(self):
        print("This is state 3 of class A")


class B:
    def state_4(self):
        print("This is state 4 of class B")

    def state_5(self):
        print("This is state 5 of class B")


#multilavel inheritance      
class C(A, B):
    def state_6(self):
        print("This is state 6 of class C")
#multiple inheritance
a =A()
a.state_1() # This is state 1 of class A

b =B()
b.state_4() # This is state 4 of class B    

c = C()
c.state_1() # This is state 1 of class A
c.state_4() # This is state 4 of class B
c.state_6() # This is state 6 of class C
