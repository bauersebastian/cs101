__author__ = 'Sebastian'

def fibonacci_iter(n):
    n1, n2 = 0, 1
    for i in range(0,n):
        n1, n2 = n2, n1 + n2
    return n1

print fibonacci_iter(36)