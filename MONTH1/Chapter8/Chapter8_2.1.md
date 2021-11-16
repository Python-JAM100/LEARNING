## Explanation of __Private members__
- Private members are similar to protected members, the difference is that the property or method can ONLY be accessed within the class.
- To define a private member prefix the member name with double underscore “__”.
- __Note__: Python’s private and protected member can be accessed outside the class through python name mangling.

## Example Chapter 8_2.1
```bash
class Test:

    def __init__(self, foo):    
        self.__foo = foo    
        # __foo is private member

    # private function
    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)
    # cannot call private object, because this is not within the class.


if __name__ == "__main__":
    main()
```