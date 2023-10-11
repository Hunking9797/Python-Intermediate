# list is ordered, mutable and allows duplicate elements
myList = ["banana", 123, "apple", True]
print(myList)

# creating list with method
myList2 = list()
# later we can append to myList2

# 0 for first index
# -1 for last index
item = myList[0]
print(item)
item2 = myList[-1]
print(item2)

# printing length of the list
print(len(myList))

# append() method for appending item at back of the list
myList.append(2786)
print(myList)

# insert(<index>, <item>) for inserting element at specific position
myList.insert(1, "blueberry")
print(myList)

# pop() method to pop last element from the list
myList.pop()
print(myList)
# we can also assign the popped element to a variable like item = myList.pop()

# removing specific element from the list
myList.remove("banana")
print(myList)

# difference between sort() and sorted()
list3 = ["apple", "cherry", "blueberry", "pineapple"]
new_list = sorted(list3)
print(new_list)
# sorted is used for sorting the list and assigning to newlist
# sort is used for inplace sorting and we know list is mutable

# we can concatenate two list or more and assign to newlist
list3.reverse()
print(list3)
# similar for reverse() and reversed()

# iterating list using []
# [<starting_index>:<ending_index(not included)>:<steps>]

print(list3[1:4])
print(list3[::2]) # prints elements with steps 2
print(list3[::-1]) # a way to reverse list

# demonstrating deep copy in list
numbers = [1,2,3,4,5,6,7,8,9]
new_numbers = numbers.copy() # <or> numbers[:] <or> list(numbers) this all will do deep copy
new_numbers.append(10)
print(numbers)
print(new_numbers)

squared_numbers = [num*num for num in numbers]
# syntax for comphrended list is --expression followed by loop--
print(squared_numbers)

