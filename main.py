def my_max(list1):
    my_max = 0
    for i in list1:
        if i > my_max:
            my_max = i
    return my_max

def my_min(list1):
    min1 = list1[0]
    for i in list1:
        if i < min1:
            min1 = i
    return min1

list1 = [48,2,5,8,4,9,7]

print(my_max(list1))
print(my_min(list1))