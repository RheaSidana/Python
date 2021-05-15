# Create your dictionary class
class my_dict(dict):

	# __init__ function
	def __init__(self):
		self = dict()
		
	# Function to add key:value
	def add(self, key, value='Fruit'):
		self[key] = value

# Main Function
obj = my_dict()

obj.add(1,'Orange')
obj.add(2,'Apple')
obj.add(3,'Mango')
obj.add(4,'PineApple')
obj.add(5,'WaterMelon')
obj.add(6, 'Grapes')
obj.add(7)

print(obj)

#output
# {1: 'Orange', 2: 'Apple', 3: 'Mango', 4: 'PineApple', 5: 'WaterMelon', 6: 'Grapes', 7: 'Fruit'}
