#!/usr/bin/python3
"""Declaration of class Rectangle"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of class"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of class to print"""
        return ("" + (
            self.__width * str(self.print_symbol) + '\n'
            ) * self.__height).rstrip('\n')

    def __repr__(self):
        """Returns string representation of class to eval it"""
        c = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return c

    def __del__(self):
        """Prints message when class is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
