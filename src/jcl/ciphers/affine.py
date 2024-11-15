from jcl.operations import alphabet
from jcl.nt.divisibility import gcd

def encrypt(txt, m, n):
  """
  Generates an affine encrpytion of a plaintext using mx + n (mod 26)

  Parameters
  ----------
  txt : str 
        Plaintext being encrypted
  m : int
      The
  n : int
      The magnitude of the shift
  
  Returns
  -------
  result : str
           The decrpyted ciphertext
  """
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

def decrypt(txt, m, n):
  """
  Decrypts an affine encryption by solving the congruence y ≡ mx + n (mod 26)

  Parameters
  ----------
  txt : str 
        Ciphertext being decrypted
  m : int
      The
  n : int
      The magnitude of the shift
  
  Returns
  -------
  result : str
           The decrypted plaintext
  """
  x = pow(m, -1, 26) 
  y = (-n * x) % 26

  print(x, y)

  return encrypt(txt, x, y)