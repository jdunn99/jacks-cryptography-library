"""
This is a temporary file while I build out the more complex cryptographic operations found in the textbook.
Once everything works and is tested, I will port into their own modules
"""

import numpy
from number_theory import gcd, modular

# def addell(xy, uv, b, c, n)
# def affinecrypt(txt, m, n)
# [x] def allshifts(txt)
# def choose(txt, m, n)
# def coinc(txt, n)
# def corr(v)
# def frequency(txt)
# def lfsr(c, k, n)
# def lfsrlength(v, n)
# def lfsrsolve(v, n)
# def multsell(xy, m, b, c, n)
# def num_to_text_0(n)
# def num_to_text(n)
# [x] def shift(txt, n)
# def txt_to_num_0(txt)
# def txt_to_num(txt)
# def vigenere(txt, v)
# def vigvec(txt, m, n)

# Helper for shifting  text
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift(plaintext: str, n: int) -> str:
  """
  Shifts a text by n

  Parameters:
  plaintext (str): The text being shifted
  n (int): The amount to shift (mod 26)

  Returns:
  (str): The shifted text
  """

  result = ""
  for text in plaintext:
    if text == " ":
      continue

    num = ((ord(text) - 97) + n) % 26
    result += alphabet[num]
  return result

def all_shifts(txt: str):
  """
  Gives all 26 shifts of the text

  Parameters:
  txt (str): The text being shifted 
  """

  for i in range(0, 26):
      print(shift(txt, i))

def affinecrypt(txt: str, m: int, n: int) -> str:
  """
  Generates an affine encrpytion of a plaintext using mx + n (mod 26)
  
  Parameters:
  txt (str): Plaintext we are encrypting
  m (int): 
  n (int): The magnitude of the shift

  Returns:
  result (str): The encrypted cipher
  """

  # Make sure that m is coprime with the length of the alphabet
  if gcd(m, 26) != 1:
    return None

  result = ""
  for char in txt:
    if char == " ":
      continue
    x = ((ord(char) - 97)) % 26

    new_pos = ((m * x) + n) % 26
    result += alphabet[new_pos]
  
  return result
    
def frequency(txt: str) -> dict[str, int]:
  """
  Lists the number of occurences of each letter a through z in the plaintext.

  Paramters:
  txt (str): The plaintext we are mapping

  Returns:
  freq (dict[str, int]): The frequency map counting characters
  """
  freq = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
    "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
    "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0
  }
  for char in txt:
    # skip spaces
    if char == " ":
      continue
    freq[char] = freq.get(char, 0) + 1
  return freq

def coinc(txt: str, n: int) -> int:
  """
  Calculates the number of matches between the plaintext and plaintext shifted by n
  """
  c = 0

  for i in range(n, len(txt)):
    if txt[i] == txt[i - n]:
      c += 1

  return c

def choose(txt, m, n):
  """
  Lists the characters in txt in positions congruent to n (mod m)
  """
  pos = n % m
  result = ""

  for i in range(0, len(txt)):
    if (i + 1) % m == pos:
      result += txt[i].lower()

  return result

def vigvec(txt, m, n):
  """
  Gives the frequencies of the letters a through z in positions congruent to n (mod m)
  """
  new_txt = choose(txt, m, n)
  freqs = frequency(new_txt)

  return [round(v / len(new_txt), 7) for k, v in freqs.items()]
  
def corr(v):
  """
  Calculates the dot product of the vector v with the 26 shifts of the alphabet frequency vector
  """

  # Found this online. TODO: Add the source
  freqs = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 
           0.020, 0.061, 0.070, 0.0015, 0.0077, 0.040, 
           0.024, 0.067, 0.075, 0.019, 0.00095, 0.060, 
           0.063, 0.090, 0.028, 0.0098, 0.024, 0.0015, 
           0.020, 0.00074]
  
  dot_products = []

  # Calculate the 26 shifts
  for i in range(26):
    shifted = freqs[-i:] + freqs[:-i]

    dot_product = round(sum(v[j] * shifted[j] for j in range (len(v))), 7)
    dot_products.append(dot_product)

  return dot_products

def vigenere(txt, v):
  """
  Gives the Vigenere encryption of txt using the vector v
  """
  l = len(v)
  i = 0
  result = ""
  for char in txt:
    if(char == " "):
      continue

    s = v[i % l]
    result += shift(char, s)
    i += 1
  
  return result
    
def lfsr(c, k, n):
  """
  Gives the sequence of n bits produced by the recurrence that has coefficients given by the vector c.
  The initial values of the bits are given by the vector k
  """
  result = k
  positives = [i for i in range(len(c)) if c[i] == 1]
  
  for i in range(n - len(k)):
    new_bit = 0
    for j in positives:
      new_bit ^= result[i + j]
    result.append(new_bit)

  return result

def lfsr_length(v, n):
  """
  Given a guess n for the length of the recurrence relationthat generates the binary
  vector v, it computes the coefficients of the recurrence.
  """

  result = []

  for m in range(1, n + 1):
    matrix = []
    for i in range(m):
      row = v[i: i + m]
      if len(row) < m:
        break
      matrix.append(row)

    # HACK: I used numpy because matrices are a lot of work. :(
    # TODO: Write it myself!
    matrix = numpy.array(matrix) 
    det = round(numpy.linalg.det(matrix)) % 2
    result.append((m, det))

  return result