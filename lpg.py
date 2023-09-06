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
