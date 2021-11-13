# This Chapter is to differenciate when __name__ is detected
# Will highly require Chapter6_1 for further explaination

print("File two __name__ is set to: {}" .format(__name__)) #1

def function_three():
   print("Function three is executed")

def function_four():
   print("Function four is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported") #2

# when run python Chapter6_2.py:
"""
File two __name__ is set to: __main__
File two executed when ran directly
"""