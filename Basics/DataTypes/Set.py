phones = {"j2", "j7", "m10"}

print ("Set: " + str(phones) + "\n")

phones.add("m20")
print ("After add: " + str(phones))

print ("\nFor Looping ")
for phone in phones:
    print ("Phone: " + phone)

print ("\nWhile Loop is not possible")
# i = 0
# while i < len(phones):
#     print("Phone: " + str(phones[i]))
#     i += 1

