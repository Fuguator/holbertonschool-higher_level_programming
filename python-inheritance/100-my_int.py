#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    def __eq__(self, value: object) -> bool:
        return super().__ne__(value)

    def __ne__(self, value: object) -> bool:
        return super().__eq__(value)
