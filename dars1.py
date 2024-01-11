def my_sum(list1: list)->list:
    my_sum = 0
    for i in list1:
        my_sum += i
    return my_sum
    
list1 = [1,2,3,4,5]
print(my_sum(list1))