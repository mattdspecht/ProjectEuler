# Problem 12

def triangular_number(n):
    return n * (n + 1) // 2

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2
    if int(n**0.5) ** 2 == n:
        count -= 1
    return count

def find_triangular_number_with_divisors(min_divisors):
    n = 1
    while True:
        tri_num = triangular_number(n)
        if count_divisors(tri_num) > min_divisors:
            return tri_num
        n += 1

if __name__ == "__main__":
    min_divisors = 500
    result = find_triangular_number_with_divisors(min_divisors)
    print(f"The first triangular number with more than {min_divisors} divisors is: {result}")