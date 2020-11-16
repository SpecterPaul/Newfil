import re 
from itertools import chain
new = []
f = open("assignment.txt", "r")

for line in f:
    number = re.findall('[0-9]+',line)
    if number:
        new.append(number)
        print(new[-1])
           
           
            
    
