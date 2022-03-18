import math

print ("\nAll directory methods: ")
i = 1
for fn in dir(math):
    print (str(i) + ": " + str(fn) + "()")
    i += 1

print ("\n\n")
print (math.pow(3, 2))
print (math.sqrt(9))

print ("\n\n")

from math import sqrt, pow

print (pow(3, 2))
print (sqrt(9))
