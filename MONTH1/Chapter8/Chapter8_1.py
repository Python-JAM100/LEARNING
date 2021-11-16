class Student(object):

    # __init__  It is a special method used to initialize the object when it is created
    # Through this method, we can bind the two attributes name and age for the student object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s is learning %s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s is watching cartoon.' % self.name)
        else:
            print('%s is reading Manga.' % self.name)

M = Student("Margaret", 25)
T = Student("Terry", 32)
S = Student("Susan", 15)

M.study("Python")
T.watch_movie()
S.watch_movie()


# When run python Chapter8_1.py
"""
Margaret is learning Python.
Terry is reading Manga.
Susan is watching cartoon.
"""
