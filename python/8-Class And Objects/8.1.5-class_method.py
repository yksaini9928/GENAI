class Welcome:
    def greet(cls):
        print(cls)
        print("Welcome to Python programming!")

w1 =Welcome()
w1.greet() # <class '__main__.Welcome'> Welcome to Python programming!
print(Welcome) # <function Welcome.greet at 0x7f8c8c8c8c10>        
