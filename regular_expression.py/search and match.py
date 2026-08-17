import re

string = "Honey singh munariya"
pattern = "Honey"
pattern_2 = "singh"


if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

# as we saw that the result is match found because the match method
# chech the pattern from the start.
# If we change the pattern with the singh than result would be not found.

if re.search(pattern_2,string):
    print("search found")

else:
    print("Search not found")

# search has been found because the search method searh throughout the entire string
# capitle and small latter can be the cause of error.


























