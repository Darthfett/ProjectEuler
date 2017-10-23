"""Problem 12 - Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def get_triangle_numbers():
    n = 0
    i = 0
    while True:
        i += 1
        n += i
        yield n

def get_divisors(i):
    yield 1
    for div in range(2, (i // 2) + 1):
        if i % div == 0:
            yield div
    yield i

def p12(least_divisors):
    for n in get_triangle_numbers():
        divisors = list(get_divisors(n))
        if len(divisors) > least_divisors:
            print(n)
            # print(divisors)
            return

if __name__ == '__main__':
    p12(500)