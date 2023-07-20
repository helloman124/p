util.py
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius
import util
celsius=int(input("enter temp in celsius:"))
fahrenheit=util.celsius_to_fahrenheit(celsius)
print("celsius in fahrenheit is:")
fahrenheit=int(input("enter temp in fahrenheit"))
celsius=util.fahrenheit_to_celsius(fahrenheit)
print("fahrenheit in celsius is:")
