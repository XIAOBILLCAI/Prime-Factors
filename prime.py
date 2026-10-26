
def generate_prime_factors(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Input must be an integer")

    factors = []
    divisor = 2

    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor

        divisor += 1

    return factors
