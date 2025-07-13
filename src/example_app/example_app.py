#!/usr/bin/env python3

import argparse

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_below(maximum):
    """Print all prime numbers below the given maximum."""
    for num in range(2, maximum):
        if is_prime(num):
            print(num)

def main():
    parser = argparse.ArgumentParser(description="Print all prime numbers below a given maximum.")
    parser.add_argument("maximum", type=int, help="The upper limit (exclusive) for prime numbers.")
    args = parser.parse_args()

    list_primes_below(args.maximum)

if __name__ == "__main__":
    main()
