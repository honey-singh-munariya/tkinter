# we use the curly bracket when we need  a letter for a specific times.
# For  example if we need a letter "b" for 5 times we use the curly bracket
# i.g sting = r"hubb{5}y"
# like this let's write the code
import re

string = "Honeyyyy singh munariya"

pattern = r"Honey{3}"

if re.match(pattern,string):
    print("Match found")
else:
    print("Match not found")


    