#!/usr/bin/python3

import math
from sys import argv, exit, stderr


def is_prime(n):
    """
    Check if a number is prime ok.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def rsa_factors(n):
    """
    Find the prime factors p and q of n.
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            q = n // i
            if is_prime(i) and is_prime(q):
                return i, q
    return None, None


def main():
    if len(argv) != 2:
        stderr.write("Usage: ./rsa <file>\n")
        exit(1)

    try:
        with open(argv[1], "r") as f:
            n = int(f.read().strip())
    except FileNotFoundError:
        stderr.write(f"Could not find file {argv[1]}, it does not exist\n")
        exit(1)
    except ValueError:
        stderr.write("Invalid input: file must contain a single integer\n")
        exit(1)

    p, q = rsa_factors(n)
    if p and q:
        print(f"{n}={p}*{q}")
    else:
        print(f"Could not find prime factors for {n}")


if __name__ == "__main__":
    main()
