## Explanation of __Protected members__
- The property or method can be accessed within the class and by classes derived from that class.
- To define protected member prefix the menber name with a single underscore “_”.
- __Note__: The ```__init__``` method is a constructor and runs as soon as an object of a class is instantiated.

## Example Chapter 8_2.1
```bash
# Creating a base class
class Base:
	def __init__(self):
		
		# Protected member
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

# Calling protected member Outside class 
# will result in AttributeError
print(obj2.a)

```