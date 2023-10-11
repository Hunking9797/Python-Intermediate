# sets are mutable, no duplicates allowed, unordered
my_set = {1,2,3,4,5}
print(type(my_set))

my_set.update([6,7,8]) # appending an iterable
print(my_set)

odds = {1,3,5,7,9}
evens = {2,4,6,8,10}
primes = {2,3,5,7,11}

print(odds.intersection(primes)) #this give new_set with intersection
# if intersection_update is used it will do it inplace and odd set will be edited

# gives elements which are not present in both
print(sorted(evens.difference(primes)))

# symmetric_difference will considered unique elements from both sets
print(evens.symmetric_difference(primes))

evens.discard(2) #if present will remove else nothing

try:
    evens.remove(2) #if present will remove else exception
except:
    print("error")