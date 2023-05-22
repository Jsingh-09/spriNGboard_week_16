import pytest

def fizzbuzz(N):
    if N%5 == 0 and N%3 == 0:
        return "FizzBuzz"
    elif N%3 == 0:
        return "Fizz"
    elif N%5 == 0:
        return "Buzz"
    else: 
        return str(N)

def test_fizzbuzz():
    pass

