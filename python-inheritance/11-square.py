#!/usr/bin/python3
"""BaseGeometry"""
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
