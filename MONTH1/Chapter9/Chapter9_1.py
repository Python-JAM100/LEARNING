class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Accessor - getter method
    @property
    def name(self):
        return self._name

    # Accessor - getter method
    @property
    def age(self):
        return self._age

    # modifier - setter method
    @age.setter
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
    person.age = 22
    person.play()
    # person.name = 'Susan'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()

# When run python Chapter9_1.py
"""
Terry is playing badminton.
Terry is playing football.
"""
