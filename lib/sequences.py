#!/usr/bin/env python3

def print_fibonacci(length):
    """Print the first `length` Fibonacci numbers."""
    seq = []
    a, b = 0, 1
    for _ in range(length):
        seq.append(a)
        a, b = b, a + b
    print(seq)


print_fibonacci(10)