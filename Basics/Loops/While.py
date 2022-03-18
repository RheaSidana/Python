fruits = ["apple", "banana", "cherry", "dragon", "orange", "grapes", "mango"]

print ("List: " + str(fruits))

print ("\nLooping using while loop")
loopCount = 0
while loopCount < len(fruits):
    print (str(loopCount + 1) + ". " + fruits[loopCount].capitalize())
    loopCount += 1