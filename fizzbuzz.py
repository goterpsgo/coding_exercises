#!/usr/bin/env python3

# main class definition
class Fizzbuzz:
    def __init__(self, value=100, fizz=3, buzz=4):
        self._value = value
        self._fizz = fizz
        self._buzz = buzz
    
    @property
    def value(self):
        return self._value
    
    @property
    def fizz(self):
        return self._fizz
    
    @property
    def buzz(self):
        return self._buzz

    @value.setter
    def value(self, value):
        self._value = value

    @fizz.setter
    def fizz(self, fizz):
        self._fizz = fizz

    @buzz.setter
    def buzz(self, buzz):
        self._buzz = buzz
 
    def __divisible_by(self, numerator, denominator):
        return numerator % denominator == 0

    @property
    def fizzbuzz(self):
        for cnt in range(self.value):
            print("Count: " + str(cnt))
            if self.__divisible_by(cnt, self.fizz):
                print("FIZZ") 
            if self.__divisible_by(cnt, self.buzz):
                print("BUZZ") 

# class instantiation
fb = Fizzbuzz()
print("Value: " + str(fb.value))
fb.fizz = 3
fb.buzz = 5
fb.value = 22
print("Fizz: " + str(fb.fizz))
print("Buzz: " + str(fb.buzz))
print("Value: " + str(fb.value))
fb.fizzbuzz
