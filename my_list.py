# Creating an empty list
my_list = []

# Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Inserting an element at a specific index
my_list.insert(1, 15)
print(my_list)

# Extending the list with another list
my_list.extend([50, 60, 70])
print(my_list)

# Removing last element
my_list.pop()
print(my_list)

# Sort list in ascending order
my_list.sort()
print(my_list)

# Find and print the index of 30
print(f"The index of 30 is: {my_list.index(30)}")

