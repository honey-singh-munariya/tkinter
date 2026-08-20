# if you want a string must start with something specific.
# Then we use the caret "^" method

import re

string = "91-038238429"

pattern = r"^91"

if re.match(pattern,string):
    print("Match found")
else:
    print("Match not found")

# we use the caret sign in the starting of the pattern.



