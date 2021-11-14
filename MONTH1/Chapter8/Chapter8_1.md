## Explanation of ```__init__``` 
The ```__init__()``` method is called the constructor in Python.

Constructors are used to initialize the object’s state.

The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created. 

A constructor also contains collection of statements(i.e. instructions) that are executed at time of Object creation.

It is run as soon as an object of a class is instantiated. 

## Explanation of self
self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments

The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

## Example Chapter 8_1
```bash
class Student(object):
# one class has object and function, constructor (constructor = init function)

    def __init__(self, name, age):
    # __init__  It is a special method used to initialize the object when it is created
        self.name = name
        self.age = age
        # Through this method, we can bind the two attributes name and age for the student object

    def study(self, course_name):
        print('%s is learning %s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s is watching cartoon.' % self.name)
            # when age of the student smaller than 18, will print the above this result
        else:
            print('%s is reading Manga.' % self.name)
            # when age of the student bigger than or equal to 18, will print the this result 

# Object instantiation
M = Student("Margaret", 25)
T = Student("Terry", 32)
S = Student("Susan", 15)

# Accessing class attributes
M.study("Python")
T.watch_movie()
S.watch_movie()

```

## Output
```
Margaret is learning Python.
Terry is reading Manga.
Susan is watching cartoon.
```