from number_theory import divisibility
import math
import random

def relative_prime(*args) -> bool:
  """
  Calculates if the given numbers are relatively prime.
  Useful for operations such as Chinese Remainder Theorem and Euler's Totient Function

  Paramters:
  *args: Integers we are checking the relativity

  Returns:
  bool
  """

  for i in range(len(args)):
    for j in range(i + 1, len(args)):
      if divisibility.gcd(args[i], args[j]) != 1:
        return False
  return True

def euler_phi(n: int) -> int:
  """
  Calculates Euler's totient function, 
  which determines the number of positive integers less than n 
  that are relatively prime to n.

  WARNING: Using large integers will cause this program to hang since it's computationally heavy.
  TODO: Look into a more efficient way to implement this

  Parameters:
  n (int): The value we are applying the totient function to

  Returns:
  (int): The number of positive integers relatively prime to n
  """
  x = 0
  for i in range(1, n):
    if relative_prime(i, n):
      x += 1
  return x


def factor_integer(n: int):
  """
  Computes the prime factorization of an integer n

  Paramters:
  n (int): The integer being factored

  Returns:
  Tuple containing the prime factors and their corresponding exponents
  """
  factors = {}

  # Find the number of 2's
  while n % 2 == 0:
    factors[2] = factors.get(2, 0) + 1
    n //= 2

  # Now check all other primes up to sqrt(n). Skipping all even elements.
  for i in range(3, int(math.sqrt(n) + 1), 2):
    
    while n % i == 0:
      factors[i] = factors.get(i, 0) + 1
      n //= i 

  # Check if the remaining digit is a prime factor
  if (n > 2):
    factors[n] = factors.get(n, 0) + 1

  return tuple(factors.items())

def is_prime(n: int, k: int) -> bool:
  """
  Determines if a given number n is prime using the Miller-Rabin test.

  Follows the pseudo-code from Wikipedia - https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

  let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
  repeat k times:
      a ← random(2, n − 2)  # n is always a probable prime to base 1 and n − 1
      x ← ad mod n
      repeat s times:
          y ← x2 mod n
          if y = 1 and x ≠ 1 and x ≠ n − 1 then # nontrivial square root of 1 modulo n
              return “composite”
          x ← y
      if y ≠ 1 then
          return “composite”
  return “probably prime”

  Parameters:
  n (int): The number being check for primality
  k (int): The number of rounds of testing to perform

  Returns:
  (bool): Whether or not n is prime
  """

  if n < 2:
      return False

  s = 0
  d = n - 1

  # factor powers of 2 from n
  while d % 2 == 0:
      d //= 2
      s += 1

  for _ in range(k):
    a = random.randint(2, n - 2)

    # a^d (mod n)
    x = pow(a, d, n)

    for _ in range(s):
      # x^2 (mod n)
      y = pow(x, 2, n)

      if y == 1 and x != 1 and x != n - 1:
        return False
      
      x = y
    if x != 1:
      return False

  return True

def next_prime(n: int) -> int:
  """
  Finds the closest prime p such that p > n.
  Checks all odd numbers 

  Parameters:
  n (int): The base we are finding the next prime from

  Returns:
  (int): The next prime
  """
  # Check if n is even we increment
  if n % 2 == 0:
    n += 1
  else:
    n += 2

  while not is_prime(n, 10):
    n += 2

  return n


