def sumDigits(n: int):
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")
    if(n < 1):
        return 0
    return (n%10) + sumDigits(n//10)

n = 2 ** 1000
print(n)
print(sumDigits(n))
