## Example Chapter 8_2.2
```bash
class Test:

    # constructor
    def __init__(self, foo):
        self.__foo = foo

    # private function 
    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    # Object instantiation
    test = Test('hello')
    # To access private object, Test must be private
    test._Test__bar()
    # To accedd private object, Test must be private
    print(test._Test__foo)

if __name__ == "__main__":
    main()

```

## Ouput Chapter 8_2.2
```
hello
__bar
hello
```