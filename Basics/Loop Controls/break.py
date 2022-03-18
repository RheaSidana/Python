fruits = ["apple", "banana", "cherry", "dragon", "orange", "grapes", "mango"]

print ("List: " + str(fruits))

print ("\nLooping using for loop")
loopCount = 0
for fruit in fruits:
    if fruit == "orange":
        break
    print (str(loopCount + 1) + ". " + fruit.capitalize())
    loopCount += 1
