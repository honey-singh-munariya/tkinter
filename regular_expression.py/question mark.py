# To use any sting as a optional we use the question mark.

import re

sting = "Hone singh munariya"
pattern = "Honey?"

if re.match(pattern,sting):
    print("Match found")

else:
    print("Match not found")

    