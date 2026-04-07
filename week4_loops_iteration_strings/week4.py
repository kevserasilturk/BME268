#n = 5

#while n > 0:
#    print(n)
#    n = n - 1 

"""
for i in range(5):
    print(i)
    text = "banana"

print(len(text))
print(text[0])

count = 0
for c in text:
    if c == "a":
        count += 1

print("a count:", count)
"""

#Finding the largest value
"""
largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(largest_so_far, the_num)
print("After", largest_so_far)

"""

text = "banana"

print(len(text))
print(text[0])

count = 0
for c in text:
    if c == "a":
        count += 1

print("a count:", count)

fruit = "apple"
letter = fruit[3]
print(letter)
x = 3

w = fruit[x-1]
print(w)
#string using an index banana 012345, apple 01234

print("looping through strings")
vegetable = "carrot"
index = 0
while index < len(vegetable):
    letter = vegetable[index]
    print(index, letter)
    index = index + 1


print("slicing strings")

x = 'Monty Python'
print (x [0:4])
print (x [8:])
print (x [:])
#Monty Python 01234 5 67891011

fruit = "banana" 
"n" in fruit