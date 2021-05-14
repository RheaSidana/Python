#!/usr/bin/python
import operator
import math
a=5
b=9

c= operator.truediv(b,a)
print "truediv \t",c

c= operator.floordiv(b,a)
print "floordiv \t",c

c= math.ceil(operator.truediv(b,a))
print "ceil(truediv) ",c

c=b//a
print "b//a \t\t",c

#output
#$python main.py
#truediv 	1.8
#floordiv 	1
#ceil(truediv)  2.0
#b//a 		1
