str1 = " String 1 "
str2 = " String 2 "

print ("Addition: " + str1 + str2)
# print ("Subtraction: " + str(str1 - str2))
# print ("Multiplication: " + str(str1 * str2))
# print ("Division: " + str(str2 / str1))
# print ("Modulus: " + str(str1 % str2))
# print ("Power: " + str(str1 ** str2))
# print ("Division without decimal value: " + str(str2 // str1))

print("All Lower: " + (str1+str2).lower())
print("All Upper: " + (str1+str2).upper())
print("Count (ing): " + str((str1+str2).count("ing")))
print("Find (ing): " + str((str1+str2).find("ing")))
print("Replace: " + (str1+str2).replace("1", "2"))
print("Split: " + str((str1+str2).split("1")))
print("Partition: " + str((str1 + str2).partition("1")))
print("")
print("Checks for alphnum: "+ str(str1.isalnum()))
print("Checks for digit: "+ str(str1.isdigit()))
print("Checks for space: "+ str(str1.isspace()))
