#operator overloading
class overload:
	def __init__(self,var):
		self.var = var
	def __lt__(self, other):   #lt is overload with < operator
		if(self.var < other.var):
			return "object1 values is less than object2"
		else:
			return "object 2 is less tahn object1"

				
obj1 = overload(10)
obj2 = overload(20)
print("passed values :", obj1.var, obj2.var)
print(obj1 < obj2)


