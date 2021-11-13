
## Chapter 6, 1&2 Explain usage of __main__

```__main__``` is to ensure which file is running the main code.

Due to there can be function imported from somewhere and same function name 

it makes whole code hardly differenciate which is the main code when run certain python function

Below is the example: 

## Example Chapter6_1
```bash
from Chapter6_2 import function_three #1
 
print("File one __name__ is set to: {}" .format(__name__))
# __name__ show __main__ when run Chapter6_1.py
# __name__ show Chapter6_2 when run Chapter6_2.py

def function_one():
  print("Function one is executed")
 
def function_two():
  print("Function two is executed")

# __name__ is equal to __main__ when run python Chapter6_1.py
# __name__ is not equal to __main__ when run python Chapter6_2.py
if __name__ == "__main__": 
  print("File one executed when ran directly")
  function_two()
  function_three()
else:
  print("File one executed when imported")
```

## Example Chapter6_2
```bash
print("File two __name__ is set to: {}" .format(__name__)) 
# __name__ show __main__ when run Chapter6_2.py
 
def function_three():
  print("Function three is executed")
 
def function_four():
  print("Function four is executed")

# __name__ is equal to __main__ when run python Chapter6_2.py
if __name__ == "__main__":
  print("File two executed when ran directly")
else:
  print("File two executed when imported") #2
```

## Output

- [X] [Output: python Chapter6_1.py] 

```
File two __name__ is set to: Chapter6_2
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed
Function three is executed
```

- [X] [Output: python Chapter6_1.py] 
```
Output: python Chapter6_2.py
File two __name__ is set to: __main__
File two executed when ran directly
```
