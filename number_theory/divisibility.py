# number_theory/gcd.py

def gcd(a: int, b: int) -> int:
  """
  Calculates the greatest common divisor of two integers using the Euclidean algorithm.

  Parameters:
  a (int): The first integer.
  b (int): The second integer.

  Returns:
  int: The greatest common divisor of a a and b.
  """
  while b:
    a, b = b, a % b
  return a

def extended_euclidean(a, b):
  """
  Calculates the Extended Euclidean algorithm that computes the greatest common divisor of two numbers
  and the coefficients x and y of Bezout's identity such that ax + by = gcd

  Paramters:
  a (int): The first integer
  b (int): The second integer

  Returns:
  """
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


def extended_gcd(*args):
  """
  Calculates the Extended Euclidean Algorithm for n integers.
  Parameters:
  *args (int): Integers of length n for which we will find the gcd and coefficients for

  Returns:
  list(int, tuple(*int)): A list containing the gcd and a tuple of the corresponding coefficients
  """

  # Start with the first element as the gcd and its coefficient as 1
  g = args[0]
  coefficients = [1] + ([0] * (len(args) - 1))

  for i in range (1, len(args)):
    a_i = args[i]

    # Find the gcd and coefficients for the current gcd and the next value
    g, x_g, x_i = extended_euclidean(g, a_i)

    # Update the coefficients
    for j in range(i):
      coefficients[j] *= x_g
    coefficients[i] = x_i

  return g, coefficients
