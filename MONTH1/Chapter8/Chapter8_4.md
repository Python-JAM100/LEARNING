## Example Chapter 8_4
Define a class to describe a point on the plane and provide methods for moving a point and calculating the distance to another point.

```bash
from math import sqrt   # from library math import square root function

class Point(object):

    def __init__(self, x=0, y=0):
        """initialize method
        :param x: x-coordinate (row)
        :param y: y-coordinate (column)
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """move to specify point
        :param x: new x-coordinate
        "param y: new y-coordinate
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """move the specified increment
        :param dx: increment of x-coordinate
        "param dy: increment of y-coordinate
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """counting the distance with another point
        :param other: another point
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):      # __str__ is used to print a string version
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
```

# Output Chapter 8_4
```
(3, 5)
(0, 0)
(-1, 2)
5.0
```