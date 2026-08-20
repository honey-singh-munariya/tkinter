# we are going to use the some opreation like d, W,D like these with backslesh\

# \d = for digits
# \D = for string
# \w = for alphanumeric


import re

string = "Honeyyyy singh munariya"

pattern = r"\D{3}"

if re.match(pattern,string):
    print("Match found")
else:
    print("Match not found")


    