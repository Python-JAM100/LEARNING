# super class
class Student:
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
		print("Roll: ", self._roll)
		print("Branch: ", self._branch)
		
# derived class
class Geek(Student):
	def __init__(self, name, roll, branch):
            Student.__init__(self, name, roll, branch)

	def displayDetails(self):
            print("Name: ", self._name)
            self._displayRollAndBranch()

obj = Geek("R2J", 1706256, "Information Technology")
obj.displayDetails()


# When run python Chapter8_2.4.py
"""
Name:  R2J
Roll:  1706256
Branch:  Information Technology
"""
