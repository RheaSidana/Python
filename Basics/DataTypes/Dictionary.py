percentage = {"ali": 99.9, "karan": 95.7}

print ("Dictionary : " + str(percentage))

print ("Percentage of Ali: " + str(percentage["ali"]))
percentage["ali"] = 99.3
print ("Percentage of Ali: (after modification): " + str(percentage["ali"]))
print("Keys: " + str(percentage.keys()))
print("Values: " + str(percentage.values()))
del(percentage["karan"])
print ("After deleting Karan: " + str(percentage))
percentage.clear()
print ("After clearing the content: " + str(percentage))
del percentage
# print ("After deleting the dictionary: " + str(percentage))
