#!/usr/bin/env python3
"""pickle"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                student = pickle.load(file)
                return student
        except FileNotFoundError:
            print(f"file {filename} not found")
        except Exception as x:
            print(f"deserialization error: {x}")
