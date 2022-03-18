def add(number1, number2):
    print ("Sum: " + str(number1 + number2))


add(2, 8)
add(3, 5)


def add_ret(number1, number2):
    return int(number1 + number2)


print ("\n\nReturn Function: ")
print ("Sum: " + str(add_ret(2, 8)))
print ("Sum: " + str(add_ret(3, 5)))
