fruits = ["apple", "banana", "cherry", "dragon", "orange", "grapes", "mango"]
duplicate = fruits

if duplicate is fruits:
    print ("copied List")

duplicate = ["apple", "banana", "cherry", "dragon", "orange", "grapes", "mango"]
if duplicate is fruits:
    print ("copied List")
else:
    print ("new List")
