from application.utils.check_if_number_is_prime import is_prime


def generate_primes(n: int) -> list[int]:
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes
