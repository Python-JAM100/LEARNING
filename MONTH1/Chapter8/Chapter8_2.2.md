## Explanation of __Name mangling__
- We can add _classname of infront private object to access the private object of outside the class. This method call name mangling.

## Example Chapter 8_2.2
```bash
class Test:

    # constructor
    def __init__(self, foo):
        self.__foo = foo
        # __foo is private member

    # private function 
    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    # Object instantiation
    test = Test('hello')
    # To access private object, Test must be private
    test._Test__bar()
    # To access private object, Test must be private
    print(test._Test__foo)

if __name__ == "__main__":
    main()

```

## Output Chapter 8_2.2
```
hello
__bar
hello
```