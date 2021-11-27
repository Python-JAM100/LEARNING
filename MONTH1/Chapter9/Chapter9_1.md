## Explanation of @property decorator
@property decorator is a built-in decorator. It helpful in defining the properties. It used to return the property attributes of a class from the stated getter and setter as parameters.

## Explanation of Getters and Setters
__Getters__: -Helps to __access__ the private / protected attributes from a class.

__Setters__: -Helps to __set the value__ to private / protected attributes in a class.

## Example Chapter 9_1
```bash
class Person(object):

    # Constructor
    def __init__(self, name, age):
        self._name = name   # _name is protected member
        self._age = age     # _age is protected member

    # Accessor - getter method
    @property   # to get the value of a protected attribute without using any getter methods. 
    def name(self):
        return self._name

    # Accessor - getter method
    @property
    def age(self):
        return self._age

    # modifier - setter method
    @age.setter     # must has getter first only can run setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing badminton.' % self._name)
        else:
            print('%s is playing football.' % self._name)


def main():
    person = Person('Terry', 12)
    person.play()
    person.age = 22 # set because 22 is set to person.age and age set to _age 
    person.play()
    # person.name = 'Susan'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
```

## Output Chapter 9_1
```
Terry is playing badminton.
Terry is playing football.
```