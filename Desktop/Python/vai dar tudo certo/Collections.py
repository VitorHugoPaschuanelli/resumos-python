#List - ordered, changeable and allows duplicate members.
#Tuple - ordered, unchangeable and allows duplicate members.
#Set - unordered, unchangeable (but you can remove or add items (???)) and don't allows duplicate members.
#Dictionary - ordered, changeable and don't allows duplicate members.

list = [1, 2, 3]
print(f"List: {list}")
list.pop() #list is changeable
print(f"List: {list}")

tuple = (1, 3, 7)
print(f"Tuple: {tuple}")
#tuple.pop() #tuple is not changeable
#print(f"Tuple: {tuple}")

set = {7, 3, 1}
print(f"Set: {set}")
set.pop() #unchangeable (but you can remove or add items (???))
print(f"Set: {set}")

dictionary = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1969
}

print(dictionary["brand"])
print(dictionary["model"])
print(dictionary["year"])

#dictionary.pop() #dictionary is not changeable
#print(dictionary["brand"])
#print(dictionary["model"])
#print(dictionary["year"])