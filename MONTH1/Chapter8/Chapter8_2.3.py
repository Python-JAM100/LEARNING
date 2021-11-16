# Creating a base class
class Base:
	def __init__(self):
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):
        # Calling constructor of Base class
		Base.__init__(self)
		print("Calling protected member of base class: ")
		print(self._a)

obj1 = Derived()
obj2 = Base()

print(obj2.a)
