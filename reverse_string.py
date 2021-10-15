#!/usr/bin/env python3

# main class definition
class ReverseString:
    def __init__(self, string="Hello world"):
        self._string = string
    
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        if len(string) > 0:
            self._string = string.strip()

    @property
    def reverse(self):
        arr = list(self._string)
        size = len(self._string)
        self._string = ""
        for cnt in range(size):
            self._string += arr.pop()
        
        return self._string

# class instantiation
rs = ReverseString()
rs.string=" Eat fresh "
print("String: " + str(rs.string))
rs.reverse
print("String: " + str(rs.string))
