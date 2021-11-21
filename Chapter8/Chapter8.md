# Object-Oriented Programming(OOP)

- Object-oriented Programming uses **objects** and **classes**
- Purpose is to **bind the data and the functions that works on that together as a single unit** so that no other part of the code can access this data

# Main Concepts of Object-Oriented Programming
* Class
* Objects
* Polymorphism
* Encapsulation
* Inheritance

Before explanation, Some basic keywords that will used while working with objects and classes.

**self**
- Class methods **must have an extra first parameter called self** in the method definition. 
- We **do not assign a value for self parameter during the call of the method**, as **self represent the current class property**
- When we call a method of this object as myobject.method(arg1, arg2), 
- it will automatically converted into MyClass.method(myobject, arg1, arg2) or MyClass.method(self, arg1, arg2), so myobject = self.

The **```__init__```** method
- It is run as soon as an **object of a class is instantiated. (constructor)**
- 

1. **Class**
    - A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. 
    - It is a logical entity that contains some attributes and methods.

    Some points on Python class:
    - Classes are created by keyword class.
    - Attributes are the variables that belong to a class.
    - Attributes are always public and can be accessed using the dot(.) operator. Eg.: Myclass.Myattribute

2. **Objects**
    - The object is an **entity that has a state and behavior** associated with it.
    - Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.

    An object consists of:
    - **State**: It is represented by the attributes of an object. It also reflects the properties of an object.
    - **Behavior**: It is represented by the methods of an object. It also reflects the response of an object to other objects.
    - **Identity**: It gives a unique name to an object and enables one object to interact with other objects.

3. **Inheritance**
    - Inheritance is the capability of **one class to derive or inherit the properties from another class**, from base class to derived class. 
    - The class that derives properties is called the **derived class or base class** (one that take inherited class). 
    - while the class from which the **properties are being derived is called the base class or parent class**(inherited class itself).
    - The benefits of inheritance are:
        * It represents real-world relationships well.
        * It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
        * It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
    ```Python
    # A Python program to demonstrate inheritance 
    # Base or Super class. Note object in bracket.
    # In Python 3.x "class Person" is equivalent to "class Person(object)"
    class Person(object): #base class or parent class
        # Constructor
        def __init__(self, name):
            self.name = name

        # To get name
        def getName(self):
            return self.name

        # To check if this person is an employee
        def isEmployee(self):
            return False

    # Person class Inherited (Note Person in bracket)
    class Employee(Person): # derived class
        # Here we return true, so replace inherited Person class isEmployee method 
        def isEmployee(self):
            return True

    # Driver code
    emp = Person("Geek1")  # An Object of Person
    print(emp.getName(), emp.isEmployee()) #Geek1 False

    emp = Employee("Geek2") # An Object of Employee
    print(emp.getName(), emp.isEmployee()) #Geek2 True
    ```

4. **Polymorphism**
    - Polymorphism simply means having many forms.
    - In Programming, it means the **same function name (but different signatures) being used for different types**.
    ```Python
    # Python program to demonstrate in-built poly-
    # morphic functions

    # len() being used for a string
    print(len("geeks")) #5

    # len() being used for a list, same name as above but different usage 
    print(len([10, 20, 30])) # 3
    ```

5. **Encapsulation**
    - This describes the idea of wrapping data and the methods that work on data within one unit.
    - This puts **restrictions on accessing variables and methods directly and can prevent the accidental modification of data**.
    - To prevent accidental change, an **object’s variable can only be changed by an object’s method, and these variables called private variables**.
    - We can either convert to **private variable or protected variable** from public variable.
    - A class is an example of encapsulation as **it encapsulates all the data that is member functions, variables**
    ```Python 
    # Python program to demonstrate protected members

    # Creating a base class
    class Base:
        def __init__(self):
            self._a = 2 # Protected member

    # Creating a derived class   
    class Derived(Base):
        def __init__(self):
            # Calling constructor of Base class
            Base.__init__(self)
            print("Calling protected member of base class: ")
            print(self._a)

    obj1 = Derived() # called __init__ method from Derived class
    obj2 = Base() # called __init__ method from Base class

    # Calling protected member Outside class will result in AttributeError
    print(obj2.a) # this become error as cannot direct assign obj2.a direct to base class as it against encapsulation rule
    ```
