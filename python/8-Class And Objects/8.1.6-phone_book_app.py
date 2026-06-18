class Contact:
    phone_directory = []


    def __init__(self, name,phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.phone_directory.append(self)


    def show_contact(self):
        return f"Name: {self.name}, Contact Number: {self.phone_number}"


    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print( "No contacts in the phone book.")
        else:
            print("Phone Book Directory:")
        for contact in cls.phone_directory:
            print(contact)

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name == search_name:
                return contact.phone_number
        return "Contact not found." 

    @staticmethod
    def valid_phone_number(number):
        if len(number) == 10 and number.isdigit():
            return True
        else:
            return False    
n_contacts =int(input("Enter the number of contacts you want to add: "))
for i in range(n_contacts):
    name =input("enter the name of the contact: ")
    phone_number =input("enter the phone number of the contact: ")
    if Contact.valid_phone_number(phone_number):
        Contact(name, phone_number)   
    else:   
        print("Invalid phone number. Please enter a 10-digit number.")
        
          
#c1 =Contact("Yogesh", 1234567890)
#c2 =Contact("Krish", 9876543210)  
#c3 =Contact("Yogesh", 1111111111) # duplicate name
#c4 =Contact("Ankit", 2222222222) # new contact          
#print(Contact.phone_directory) # [<__main__.Contact object at 0x7f8c8c8c8c10>, <__main__.Contact object at 0x7f8c8c8c8c50>]


#print(c1.show_contact()) # Name: Yogesh, Contact Number: 1234567890
#print(c2.show_contact()) # Name: Krish, Contact Number: 9876543210

Contact.show_all_contacts() # Phone Book Directory: Name: Yogesh, Contact Number: 1234567890 Name: Krish, Contact Number: 9876543210

#print(Contact.search_contact("Yogesh")) # 1234567890
#print(Contact.search_contact("Ankit")) # 2222222222
#print(Contact.search_contact("Rahul")) # Contact not found.fff