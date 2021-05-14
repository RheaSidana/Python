import operator
import math
a=5
b=9
print "a=",a,"\tb=",b
c= math.ceil(operator.floordiv(b,a))
print "c=",c
print "a=",a,"\tb=",b
c= math.ceil(b//a)
print "c=",c

#$python main.py
#a= 5 	b= 9
#c= 1.0
#a= 5 	b= 9
#c= 1.0
