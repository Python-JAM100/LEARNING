## Example Chapter 8_1
```brash
class Student(object):
# one class has object and function, constructor (constructor = init function)

    def __init__(self, name, age):
    # __init__  It is a special method used to initialize the object when it is created
        self.name = name
        self.age = age
        # Through this method, we can bind the two attributes name and age for the student object

    def study(self, course_name):
        print('%s is learning %s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
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