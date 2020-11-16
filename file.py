import re 

int_list = []
f = open("assignment.txt", "r")
for line in f:
    number = re.findall('[0-9]+',line)
    if number:
        for i in range(0, len(number)):
            number[i] = int(number[i])
           
