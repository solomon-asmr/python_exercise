


"""
collection= single "Variable" used to store multiple values
List  = [] ordered and changeable. Duplicates OK
Set   = {} unordered and immutable, but Add/Remove Ok. NO duplicates
Tuple = () ordered and unchangeable. Duplicates OK. FASTER
Dictionary = a collection of {key: value} pairs ordered and changeable. No duplicates
"""
fruits = {"apple", "orange", "banana", "coconut"}
new_ek=[fr[0] for fr in fruits]
print(new_ek)
# print(fruits)
# print(help(fruits))
# print("apple" in fruits)
# print("pineapple" in fruits)
# print(fruits[1:3])  #print out elements from indices 1 to 3
# print(fruits[::-1]) #reverse the list
# fruits[0]="pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# print(fruits.index("pineapple"))
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# for fruit in fruits:
#     print(fruit)

# fruits = {"apple", "orange", "banana", "coconut"}
# print(fruits)
# # print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# fruits.add("pineapple")
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# fruits.pop()
# fruits.clear()
# print(fruits)
# fruits = ("apple", "orange", "banana", "coconut", "apple")
# print(fruits)
# print(fruits.index("apple"))
# print(fruits.count("apple"))
# for fruit in fruits:
#     print(fruit)

capitals={
    "USA": "washington D.C",
    "India": "New Delhi",
    "china": "Beijing",
    "Russia": "Moscow"
}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# print(capitals["USA"])
# capitals.update({"USA":"New York"})
# capitals.update({"Germany": "Berlin"})
# capitals.pop("India")
# capitals.popitem()
# keys=capitals.keys()
# values=capitals.values()
# for keys, values in capitals.items():
    # print(f"{keys}:{values}")