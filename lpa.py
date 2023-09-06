string = input("Enter a string of 4 characters: ")
result = ""
for char in string:
    if char.isalpha():
        if char == 'z':
            result += 'a'
        elif char == 'Z':
            result += 'A'
        else:
            result += chr(ord(char) + 1)
    else:
        result += char
print("The converted stringis:",result)

