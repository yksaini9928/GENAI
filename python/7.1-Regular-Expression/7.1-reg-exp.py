import re
message ="the current python version is 3.13"

#if pyhhon is persent in message then print the message

"""print("python" in message)
print("3.13" in message)
print("3.14" in message)

print(message.find("python"))
"""

"""
re.search(pattern,string)  # it will return a match object if pattern is found else it will return None"""

match_object=re.search("python",message)
print(match_object)