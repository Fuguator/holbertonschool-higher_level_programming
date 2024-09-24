#!/usr/bin/env python3
"""module with animal class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Dog"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat"""
    def sound(self):
        return "Meow"
