def power_two(num: int)->bool:
    if num == 1:
        return True
    elif num % 2 or num == 0:
        return False
    
    return power_two(num//2)

num = int(input("son kiriting: "))
print(power_two(num))



