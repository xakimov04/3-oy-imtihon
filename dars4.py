def square(num: int)->int:
    return lambda x: x**3 if num % 2 else x**2

num = int(input("son kiriting: "))
n = square(num)
print(n(num))