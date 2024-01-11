def fact(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

num = int(input("son kiriting: "))
result = fact(num)
print(result)
