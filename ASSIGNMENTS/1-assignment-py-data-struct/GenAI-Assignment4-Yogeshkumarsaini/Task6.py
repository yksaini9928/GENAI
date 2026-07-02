import os

filename = input("Enter filename: ")

if os.path.exists(filename):

    file = open(filename, "r")
    print("\nFile Contents:\n")
    print(file.read())
    file.close()

else:
    print("File not found. Please check the filename.")