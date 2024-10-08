#!/usr/bin/python3
"""compares 2 squares"""


class Square:
    """square"""

    def __init__(self, size=0) -> None:
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("__value must be a Square")
        return self.area() == __value.area()

    def __ne__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("__value must be a Square")
        return self.area() != __value.area()

    def __lt__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("__value must be a Square")
        return self.area() < __value.area()

    def __le__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("__value must be a Square")
        return self.area() <= __value.area()

    def __gt__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("__value must be a Square")
        return self.area() > __value.area()

    def __ge__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("__value must be a Square")
        return self.area() >= __value.area()
