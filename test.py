import pytest, pytest_benchmark

def fib(n):
    if n <= 1:
        return 1
    return fib(n - 2) + fib(n - 1)

def test_fib_10(benchmark):
    benchmark(fib, 5)

def test_fib_20(benchmark):
    benchmark(fib, 15)