def addDigit(num: int)->int:
    result = sum(map(int, str(num)))

    if result >=10:
        return addDigit(result)
    else:
        return result


num = int(input("son kiriting: "))
print(addDigit(num))