contacts = [["Sheena",[9082231195,9022717994]]];
person = ["Paakhi",[5674450922]]

contacts.append(person)

person = [["tina",[7447878490]],["Vinay",[2344789034]]]
contacts.extend(person)

for people in contacts:
    print people

#['Sheena', [9082231195, 9022717994]]
#['Paakhi', [5674450922]]
#['tina', [7447878490]]
#['Vinay', [2344789034]]
