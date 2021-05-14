fruits = ("apple", "banana", "cherry", "mango”)
counting = (1, 2, 3, 4)
mytuple=()
temp=()
myList=[]
for no in counting:
    for food in fruits:
        for i in range(no):
            myList.append(food)
        temp = tuple(myList)
    mytuple += temp
    myList=[]

print(mytuple[2])

#Output:
#cherry
          
print(mytuple)
#Output
#('apple', 'banana', 'cherry', 'mango', 
#'apple', 'apple', 'banana', 'banana', 'cherry', 'cherry', 'mango', 'mango', 
#'apple', 'apple', 'apple', 'banana', 'banana', 'banana', 'cherry', 'cherry', 'cherry', 'mango', 'mango', 'mango', 
#'apple', 'apple', 'apple', 'apple', 'banana', 'banana', 'banana', 'banana', 'cherry', 'cherry', 'cherry', 'cherry', 'mango', 'mango', 'mango', 'mango')          
