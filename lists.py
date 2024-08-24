# Lists are ordered and mutable, allows duplicate elements
myColors = ["red", "yellow", "green"]
print(myColors)

item = myColors[1]
print(item)

for x in myColors:
    print(x)

if "blue" in myColors:
    print("yes")
else:
    print("no")

len(myColors)
print(len(myColors))

myColors.append("blue") #This adds blue to the list of colors
print(myColors)

myColors.pop() # This removes blue from the list
print(myColors)

item = myColors.remove("red") # This is another way to remove something from the list
print(myColors)

numbers_list = [1, 2, -1, -2, 0, 4, 3]
new_numbers_list = sorted(numbers_list)
print(numbers_list)
print(new_numbers_list)

mixed_list = new_numbers_list + myColors
print(mixed_list)

positive_numbers = new_numbers_list[2:7] # This prints out a section of the array
print(positive_numbers)

positive_numbers.append(5)
print(positive_numbers)
