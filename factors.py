#!/usr/bin/python3

import math

def print_factors(number):
    """
    Prints the factorization of the given number in the format "n=p*q".
    """
    i = 2
    sqrt_n = int(math.sqrt(number))
    while i <= sqrt_n:
        if number % i == 0:
            q = number // i
            print(f"{number}={q}*{i}")
            return
        i += 1
    print(f"{number}={number}*1")

def main():
    """
    Main function to read numbers from a file and print their factorizations.
    """
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit(1)

    try:
        with open(argv[1], "r") as f:
            for line in f:
                number = int(line.strip())
                print_factors(number)
    except FileNotFoundError:
        stderr.write(f"Could not find file {argv[1]}, it does not exist\n")
        exit(1)

main()
