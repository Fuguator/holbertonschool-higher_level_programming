#!/usr/bin/env python3
from abc import ABC, abstractmethod
""""""


class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

def Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
