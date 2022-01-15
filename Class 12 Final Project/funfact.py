""""This script gives a random chemistry related fun fact"""

import random

#Pulling data from text file

f=open("funfacts.txt","r")
lines=f.readlines()
f.close()

#Removing /n from end of line

for a in range(len(lines)):
    lines[a]=lines[a].strip()

#Function for random fun fact

def funfact():
    x=random.choice(lines)
    print (x)
