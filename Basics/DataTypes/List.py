fruits = ["apple", "banana", "cherry", "dragon", "orange", "grapes", "mango"]

print ("List: " + str(fruits))

print ("List Before: " + str(fruits))
fruits.sort()
print ("After Sorting: " + str(fruits))
fruits.append("litchi")
print ("After appending: " + str(fruits))
print ("Index of : " + str(fruits.index("orange")))
fruits.insert(7, "pineapple")
print ("After inserting: " + str(fruits))
fruits.remove("dragon")
print ("After removing: " + str(fruits))
print ("After popping: " + fruits.pop(5))
print ("List: " + str(fruits))
