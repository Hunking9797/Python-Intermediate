# strings are ordered, immutable, text representation

from timeit import default_timer as timer

my_str = 'it\'s hello world' # '\' -> used as escape character
print(my_str)

# multiline string initialization
my_str_multiline = """Hello 
Universe\
"""
print(my_str_multiline)

# reversing string using slicing operator
subtring = my_str[::-1]
print(subtring)

my_string = "This is a sample sentence"
# creating a list from string
my_list = my_string.split(" ",2) #separator,number of times
print(my_list)

# best way to convert list to string
start = timer()
new_string = ' '.join(my_list)
stop = timer()
print(new_string, f'\ntime taken for joining {stop-start}')

# strip method for string
sample = "  Ello Mello "
print(sample.strip())

print(my_str)

new_list = [word.capitalize() for word in my_str.split()]
new_str = ' '.join(new_list)
print(new_str)

# f strings
var = 3.1425665
print(f'the value of variable is {var:.2f}')