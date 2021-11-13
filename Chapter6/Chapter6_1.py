# This Chapter is to differenciate when __name__ is detected
# Will highly require Chapter6_2 for further explaination

from Chapter6_2 import function_three #1
 
print("File one __name__ is set to: {}" .format(__name__))
 
def function_one():
  print("Function one is executed")
 
def function_two():
  print("Function two is executed")
 
if __name__ == "__main__":
  print("File one executed when ran directly")
  function_two()
  function_three()
else:
  print("File one executed when imported")

# when run python Chapter6_1.py:
"""
File two __name__ is set to: test_chapter6_2
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed
Function three is executed
"""