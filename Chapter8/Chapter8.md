# Object-Oriented Programming(OOP)

- Object-oriented Programming is a programming paradigm that uses objects and classes in programming.
- The main concept of OOPs is to bind the data and the functions that works on that together as a single unit so that no other part of the code can access this data

# Main Concepts of Object-Oriented Programming
* Class
* Objects
* Polymorphism
* Encapsulation
* Inheritance

Some basic keywords that will used while working with objects and classes.

The self
- Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
- If we have a method that takes no arguments, then we still have to have one argument.

When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) - this is all the special self is about.

The ```__init__``` method
- It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

1. Class
    - A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. 
    - It is a logical entity that contains some attributes and methods.

    Some points on Python class:
    - Classes are created by keyword class.
    - Attributes are the variables that belong to a class.
    - Attributes are always public and can be accessed using the dot(.) operator. Eg.: Myclass.Myattribute

2. Objects
    - The object is an entity that has a state and behavior associated with it.
    - Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.

    An object consists of:
    - State: It is represented by the attributes of an object. It also reflects the properties of an object.
    - Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
    - Identity: It gives a unique name to an object and enables one object to interact with other objects.

3. Inheritance
    - Inheritance is the capability of one class to derive or inherit the properties from another class. 
    - The class that derives properties is called the derived class or base class and the class from which the properties are being derived is called the base class or parent class.
    - The benefits of inheritance are:
        * It represents real-world relationships well.
        * It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
        * It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

4. Polymorphism
    - Polymorphism simply means having many forms.
    - For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.

5. Encapsulation
    - Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
    - It describes the idea of wrapping data and the methods that work on data within one unit.
    - This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
    - To prevent accidental change, an object’s variable can only be changed by an object’s method.
    - Those types of variables are known as private variables.
    