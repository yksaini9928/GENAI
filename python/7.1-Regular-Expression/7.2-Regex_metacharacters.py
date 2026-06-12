import re

message = "The current python version is 3.10.5 and the latest version is 3.11.0"

match_object = re.search("[0-9][0-9]", message)


print(match_object)