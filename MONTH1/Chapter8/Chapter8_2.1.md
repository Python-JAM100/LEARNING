## Notes to Chapter 8_2.1
__Protected members__
- Just follow the convention by prefixing the name of the member by a single underscore “_”.
- __Note__: The ```__init__``` method is a constructor [constructor = init function] and runs as soon as an object of a class is instantiated[实例化].

__Privare members__
- Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class (Parent class).
- There is no existence[存在] of __Private__ instance variables that cannot be accessed except inside a class.
- To define a private member prefix[字首] the member name with double underscore “__”.
- __Note__: Python’s private and protected member can be accessed outside the class through python name mangling[重整].

## Example Chapter 8_2.1
```bash
class Test:

    def __init__(self, foo):    
    # __foo is private object, _foo is protected
        self.__foo = foo    
        # private member

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)
    # cannot call private object


if __name__ == "__main__":
    main()
```