//program to next charecter of string using built in function
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
////program to next charecter of string using built in function
def next_alphabet(char):
    if char=='z':
        return 'a'
    elif char=='Z':
        return 'A'
    else:
        return chr(ord(char)+1)
    
def main():
    string=input("enter a string of 4 characters:")
    result=""
    if(len(string))!=4:
        print("invalid input")
        return 
    for char in string:
        result=result+next_alphabet(char)
    print(result)

main()

    else:
        return string[-1]+reverse(string[:-1])
print(reverse("hello man"))

