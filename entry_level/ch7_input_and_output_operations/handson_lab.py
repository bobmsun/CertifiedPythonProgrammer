#!/usr/bin/env python3.7

# Python implementation goes here
# Making Calculations from User Input with Python

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")      # round to the second decimal place.   
# 14.5 F is -9.72 C
