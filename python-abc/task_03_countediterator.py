#!/usr/bin/env python3
"""ountedIterator"""
from abc import ABC, abstractmethod


class CountedIterator(iter):
    """CountedIterator"""
    def __init__(self, iter_obj):
        self.iter_obj = iter(iter_obj)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count
