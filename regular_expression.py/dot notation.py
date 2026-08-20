# By using dot(.) notation we can replace any single letter between two letters.

# let's write the code for the dot notation

import re

string = "Honey singh munariya"
pattern = "H.n"

if re.match(pattern,string):
    print("match found")
else:
    print("Match not found")
# we can only replace the one letter by using the one dot notation
