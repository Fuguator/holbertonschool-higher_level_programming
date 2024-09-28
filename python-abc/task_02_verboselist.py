#!/usr/bin/env python3
""""""
from abc import ABC, abstractmethod
from typing import Iterable, SupportsIndex


class VerboseList(list):

    def append(self, object):
        print("Added [{}] to the list.".format(object))
        super().append(object)

    def extend(self, iterable):
        print("Extended the list with [{}] items.".format(iterable))
        super().extend(iterable)
    
    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        super().remove(value)
        
    def pop(self, index: SupportsIndex = -1):
        print("Popped [{}] from the list.".format(index))
        super().pop(index)