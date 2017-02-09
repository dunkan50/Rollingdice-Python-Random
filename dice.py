"""
            How to rolll a dice using random
            its simple and straigh froward
            for the code use it improve it  and share
"""

print __doc__
import random
min=1
max=6
roll="yes"

while roll =="yes" or roll=="y":
    print ("Dice rolling")
    print ("Dice values are", random.randint(min,max))
    raw_input("input value of either yes or y: ")
    print ("Dice values are", random.randint(min,max))
