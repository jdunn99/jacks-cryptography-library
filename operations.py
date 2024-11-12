# import code
import readline
from typing import Optional
# This is a test of some operations involving number theory and cryptography.
# Mainly writing my own methods from Mathematics / MATLAB / Maple.
# This is learning excersice but I will make it into a library with abstraction

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Cipher functions
def shift(plaintext: str, n: int) -> str:
    result = ""
    for text in plaintext:
        num = ((ord(text) - 97) + n) % 26
        result += alphabet[num]
    return result

def all_shifts(txt: str):
    for i in range(0, 26):
        print(shift(txt, i))

# addell[{x, y}, {u, v}, b, c, n] - finds the sum of the points {x, y} and {u, v} on the elliptic curve y^2 \equiv x^3 + bx + c (mod n)
# TODO: implement
# def addell():
#     return

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def extended_euclidean(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # old_r is the gcd, and (old_s, old_t) are the coefficients
    return old_r, old_s, old_t

def extended_euclidean_n(*args):
    # Start with the first element as the gcd and its coefficient as 1
    g = args[0]
    coefficients = [1] + [0] * (len(args) - 1)

    # Iterate through each subsequent number in args
    for i in range(1, len(args)):
        a_i = args[i]

        # Apply the Extended Euclidean Algorithm to g and a_i
        g, x_g, x_i = extended_euclidean(g, a_i)

        # Update all coefficients based on x_g
        for j in range(i):
            coefficients[j] *= x_g
        # Add the new coefficient for a_i
        coefficients[i] = x_i

    return g, coefficients



def relative_prime(numbers: tuple[int, ...]):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if gcd(numbers[i], numbers[j]) != 1:
                return False
    return True

def chinese_remainder_theorem(remainders: tuple[int, ...], mods: tuple[int, ...]) -> Optional[int]:
    if len(remainders) != len(mods):
        return None

    # Check if the moduli are relatively prime
    if not relative_prime(mods):
        return None


    # Calculate the product of all moduli (N)
    x = 0
    N = 1
    for mod in mods:
        N *= mod

    # Calculate partial product
    for i in range(len(remainders)):
        N_i = N // mods[i]
        inverse_i = pow(N_i, -1, mods[i])
        x += remainders[i] * N_i * inverse_i

    return x % N

def euler_phi(n: int) -> int:
    # number of positive integers less than 'n' that are relatively prime to n
    x = 0
    for i in range(1, n):
        pair = (i, n)
        if relative_prime(pair):
            x += 1

    return x

def extended_gcd(numbers: tuple[int, ...]) -> int:
    values = []
    x = numbers[0]
    for n in numbers:
        x = gcd(x, n)
        print(x)

    return x

def main():
    while True:
        try:
            line = input(">>> ")
            result = eval(line)
            if result is not None:
                print(result)
        except Exception as e:
            print(e)


main()
