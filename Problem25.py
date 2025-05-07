def countDigits(n: int):
    ret = 0
    while(n>0):
        n//= 10
        ret += 1
    return ret

def main():
    counter = 3
    prev1 = 1
    prev2 = 1
    num = 2
    while(countDigits(num) < 1000):
        prev1 = prev2
        prev2 = num
        num = prev1 + prev2
        counter += 1
        print(num)
        print(counter)
    pass

main()