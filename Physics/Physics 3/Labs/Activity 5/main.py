import numpy as np


def main(name):
    problem5()


def problem0():
    print("Hello World!")


def problem1():
    h = input("From what height, in meters, is the ball dropped from? ")
    t = np.sqrt(float(h) / 4.9)
    print(f"The ball takes {t:.2f} seconds to fall.")


def problem2():
    c = 1
    n = 0
    while (c < 1e9):
        print(c)
        c = int(c * (4 * n + 2) / (n + 2))
        n += 1


def problem3():
    for n in range(1, 20):
        for k in range(n + 1):
            print(binomial(n, k), end=" ")
        print("\n")


def binomial(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return int(f)


def problem4a():
    print(catalan(100))


def catalan(n):
    if n == 1:
        return 1
    else:
        return catalan(n - 1) * (4 * n - 2) / (n + 1)


def problem4b():
    print(g(108, 192))


def g(m, n):
    if n == 0:
        return m
    else:
        return g(n, m % n)


def problem5():
    primes = [2]
    for i in range(3, 10001):
        n = int(np.ceil(np.sqrt(i)))
        j = 0
        prime = True
        while j < len(primes) and primes[j] <= n:
            if i % primes[j] == 0:
                prime = False
                break
            j += 1
        if prime:
            primes.append(i)
    print(primes)


if __name__ == '__main__':
    main('PyCharm')
