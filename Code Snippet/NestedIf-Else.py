num=81

if(num%9 == 0):
    num+=7
    if((num%3)==0 and (num%2)==0):
        print(num)
    else: print("not divisible by 6 after adding 7")
else: print("not divisible by 9")

#output
#not divisible by 6 after adding 7
