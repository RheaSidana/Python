import string

print ("All directory methods: ")
i = 1
for fn in dir(string):
    print (str(i) + ": " + str(fn) + "()")
    i += 1
