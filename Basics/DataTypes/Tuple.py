# final datatype : once created can not be modified i.e, immutable
chocolates = ("5 star", "dairy milk", "silk", "5 star", "bubblee", "sneakers", "5 star", "munch", "perk")

print ("Tuple: " + str(chocolates))

print ("Occurrence count: " + str(chocolates.count("5 star")))
print ("Index of : " + str(chocolates.index("Silk".lower())))
print ("Length : " + str(chocolates.__len__()))
print ("")
print ("Index at 4 : " + str(chocolates[4]))
print ("Index at 7 : " + str(chocolates[7]))
# Range does not include the last element, here 7th element
print ("Range [4:7] : " + str(chocolates[4:7]))
