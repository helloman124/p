import util
celsius=float(input("enter temp in celsius:"))
fahrenheit=util.celsius_to_fahrenheit(celsius)
print("celsius in fahrenheit is:",fahrenheit)
fahrenheit=float(input("enter temp in fahrenheit:"))
celsius=util.fahrenheit_to_celsius(fahrenheit)
print("fahrenheit in celsius is:",celsius)
