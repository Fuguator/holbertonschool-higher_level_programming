#!/usr/bin/env python3
"""module with animal class"""
from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape"""
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """circle"""
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        return self.radius * 2 * pi

class Rectangle(Shape):
    """Rectangle"""
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(obj):
    """prints shape info"""
    area = obj.area()
    perimeter = obj.perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
