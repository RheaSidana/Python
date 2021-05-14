import re

txt = "New Year is a time of year, when every know-up is the treasure of passion for the moment of the new year, it is a day to adopt. "
x = re.sub("\s", "3", txt)
x = re.findall(r"\bt\w+", txt)
print(x)

#output:
#['time', 'the', 'treasure', 'the', 'the', 'to']
