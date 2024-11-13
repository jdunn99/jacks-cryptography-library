from .primes import euler_phi, factor_integer

def mod(a: int, n: int) -> int:
  """
  Computes the value of a (mod n)

  Parameters:
  """
  return a % b

def power_mod(a: int, b: int, n: int) -> int:
  return pow(a, b, n)


# Vadim (https://math.stackexchange.com/users/26767/vadim), Finding a primitive root of a prime number, URL (version: 2012-04-19): https://math.stackexchange.com/q/133720
def primitive_root(n):
  """
  Finds the primitive root of the prime n

  A good overview of how this is achieved can be found here:
  Vadim (https://math.stackexchange.com/users/26767/vadim), 
    Finding a primitive root of a prime number, URL (version: 2012-04-19): 
    https://math.stackexchange.com/q/133720
  """
  s = euler_phi(n)
  prime_factors = [x[0] for x in factor_integer(s)]
  powers = [n // x for x in prime_factors]

  roots = []

  i = 2
  while i < n:
    for j in range(len(powers)):
      result = pow(i, powers[j], n)
      if result == 1:
        i += 1
        break

      if j == len(powers) - 1:
        roots.append(i)
        i += 1

  return roots

# def chinese_remainder_theorem():