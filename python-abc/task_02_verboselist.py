#!/usr/bin/env python3
"""VerboseList"""
from abc import ABC, abstractmethod


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
        
    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print("Popped [{}] from the list.".format(item))
            return item
        else:
            item = super().pop(index)
            print("Popped [{}] from the list.".format(item))
            return item