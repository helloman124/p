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
//simple calculator
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=input("enter the operation symbol: ")
if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    print(a/b)
elif(c=='%'):
    print(a%b)
else:
    print("invalid operation")

//cards program
import random
group=["Heatrs","Diamond","Club","Spade"]
deck=['Ace',2,3,4,5,6,7,8,9,10,"King","Queen","Jack"]
cards=[str(r)+" of "+f for f in group for r in deck]
shuffled_cards=random.shuffle(cards)
random_card=random.choice(cards)
random_sample=random.sample(cards,2)
print("Shuffled cards: \n",cards)
print()
print("\nRandom card: ",random_card)
print()
print("\nRandom sample of 2: ",random_sample)
// pattern program
a=65
for b in range(1,11,2):
    for c in range(b):
        print(chr(a),end=" ")
        a=a+1
    print()
//progran g
def length(string):
    if string == "":
        return 0
    else:
        return 1 + length(string[1:])
print(length("python programming"))

def smallest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], smallest(lst[1:]))
print(smallest(['bg','a','rab']))
def reverse(string):
    b=""
    if len(string)==0:
        return string
    else:
        return string[-1]+reverse(string[:-1])
print(reverse("hello man"))

