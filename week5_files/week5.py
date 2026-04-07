#handle: open(read/write/close
#new line character: \n
#counting lines in a file:
fhand = open("mbox.txt")
count = 0
for line in fhand: #in operator 
    count = count + 1
print("Line Count:", count)
