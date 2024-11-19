import numpy
from jcl.nt.divisibility import gcd
from jcl.operations import alphabet
from fractions import Fraction
from math import lcm

def encrypt(txt, m):
  """
  Encrypts the plaintext txt using a matrix m via Hill cipher.
  """
  matrix = numpy.array(m)
  v = [((ord(c) - 97)) % 26 for c in txt]
  result =  numpy.matmul(v, matrix) % 26
  return "".join(alphabet[x] for x in result)
  

def decrypt(v, m):
  """
  """
  # Find the inverse
  # TODO Write my own inverse function (later for learning purposes)
  matrix = numpy.array(m)
  inverse = numpy.linalg.inv(matrix)

  # Reduce the matrix with the LCM and find the inverse mod 26
  flattened = inverse.flatten()
  fractions = [Fraction(x).limit_denominator(1000) for x in flattened]
  reduction_value = lcm(*(f.denominator for f in fractions))
  inverse *= reduction_value
  inverse = inverse * pow(reduction_value, -1, 26) % 26

  # Partition the key
  chunk = len(inverse)
  partitions = [v[i : i + chunk] for i in range(0, len(v), chunk)]
  
  # Multiply the chunk by the inverse matrix mod 26
  keys = [round(x) for p in partitions for x in (numpy.matmul(numpy.array(p), inverse)) % 26]

  # Convert the numerical keys to text
  return "".join(alphabet[key] for key in keys)