# dictionaries are unordered, mutable and consists of key-value pairs

map = {
    "name" : "max",
    "age" : 12,
    "Male" : True
}

print(map.keys()) # prints keys as list
print(map.values()) # prints values as list

# while creating copy use deepCopy i.e; map.copy()
print(map.get("name","default_value"))

map["email"] = "hello@xyz.com"
print(map)

map.popitem() #last updated item is popped
print(map)
map.pop("name") # pair with key as name is popped
print(map)
