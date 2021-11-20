## Example Chapter8_2.4

```bash
# program to illustrate protected access modifier in a class

# super class
class Student:
	
	# protected data members
	_name = None
	_roll = None
	_branch = None
	
	# constructor
	def __init__(self, name, roll, branch):
		self._name = name
		self._roll = roll
		self._branch = branch
	
	# protected member function
	def _displayRollAndBranch(self):

		# accessing protected data members
		print("Roll: ", self._roll)
		print("Branch: ", self._branch)


# derived class
class Geek(Student):

	# constructor
	def __init__(self, name, roll, branch):
				# link Student object into Geek
				Student.__init__(self, name, roll, branch)
				# Student class is being inherited to Geek class
		
	# public member function, from class of Geek
	def displayDetails(self):
				
				# accessing protected data members of super class
				print("Name: ", self._name)
				
				# accessing protected member functions of super class
				self._displayRollAndBranch()

# creating objects of the derived class	
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()

```

## Output Chapter 8_2.4
```
Name:  R2J
Roll:  1706256
Branch:  Information Technology
```