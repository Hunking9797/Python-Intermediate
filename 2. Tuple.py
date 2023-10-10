# Tuple is ordered, immutable, allows duplicate elements
# different ways of creating tuple

# first
my_tuple = ("max",12,True)
print(my_tuple)

# second is using tuple(<list>)
my_tuple2 = "hello", 123 # bydefault it is considered as tuple
my_tuple3 = "hello" # this will be considered as string
print(type(my_tuple3))
my_tuple3 = ("hello",) # adding a comma makes it tuple
print(type(my_tuple3))
