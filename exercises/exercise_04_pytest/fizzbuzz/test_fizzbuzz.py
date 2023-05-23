import pytest

def fizzbuzz(N):
    if (N%5 == 0) and (N%3 == 0):
        return "FizzBuzz"
    elif N%3 == 0:
        return "Fizz"
    elif N%5 == 0:
        return "Buzz"
    else: 
        return str(N)

golden_data = [
    (3, 'Fizz'),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (17, '17'),
    (15, 'FizzBuzz'),
]

@pytest.fixture(params=golden_data)
def in_out_data(request):
    return request.param

def test_fizzbuzz(in_out_data):
    N, expected_data = in_out_data
    assert fizzbuzz(N) == expected_data

