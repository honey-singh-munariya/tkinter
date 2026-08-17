# there are some meta character which we use for to create some kind of pattern
# in this lecture we are going to use "*"
# If we use the * after any letter then the letter should be use zero or more times.
import re
string = "Hoey singh munariya"
pattern = "Hon*ey"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")


# So it is for this lecture let's see you in the next one




