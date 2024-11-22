from jcl.nt.primes import next_prime
from jcl.nt.divisibility import lcm
from jcl.operations import alpha_to_num, alphabet
import random

def generate_keys():
  """
  Generates public and private keys using the RSA algorithm.

  Returns
  -------
  (n, e) : tuple(int, int)
           The public key
  (n, d) : tuple(int, int)
           The private key
  """

  # Choose two large prime numbers p and q
  p = next_prime(random.randint(1,1024))
  q = next_prime(random.randint(1,1024))

  if p == q:
    q = next_prime(q)

  # Compute n = pq
  n = p * q

  # Compute λ(n), where λ is Carmichael's totient function. Since n = pq, λ(n) = lcm(λ(p), λ(q)), and since p and q are prime, λ(p) = φ(p) = p − 1, and likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1)
  l = lcm(p - 1, q - 1)

  # Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime. 
  # the most commonly chosen value for e is 216 + 1 = 65537.
  e = 65537

  # Determine d as d ≡ e−1 (mod λ(n))
  d = pow(e, -1, l)

  return (n, e), (n, d)

def encrypt(txt: str, public_key: tuple[int]) -> str:
  """
  Encrypts a plaintext using RSA given the public key.

  Parameters
  ----------
  txt : str
        The plaintext being encrypted.
  public_key : tuple[int]
               The public key used in the encryption process.
  
  Returns
  -------
  ciphertext : str
               The encrypted plaintext
  """
  n, e = public_key 
  chunk_size = (n.bit_length() - 1) // 8
  txt_bytes = txt.encode("utf-8")

  ciphertext = []
  for i in range(0, len(txt_bytes), chunk_size):
    chunk = txt_bytes[i : i + chunk_size]
    encrypted_chunk = pow(int.from_bytes(chunk, 'big'), e, n)
    # Make sure all chunks are the same length
    ciphertext.append(f"{encrypted_chunk:0{len(str(n))}d}")

  return "".join(str(x) for x in ciphertext)

def decrypt(txt, private_key):
  """
  Decrypts a ciphertext back into plaintext using RSA given the private key.

  Parameters
  ----------
  txt : str
        The ciphertext to be decrypted
  private_key : tuple(int) 
                The private key used in the decryption process.
  """
  n, d = private_key

  # All chunks are n length
  chunk_length = len(str(n))

  chunks = [int(txt[i : i + chunk_length]) for i in range(0, len(txt), chunk_length)]

  ptxt_bytes = b''
  for chunk in chunks:
    decrypted_chunk = pow(chunk, d, n)
    ptxt_bytes += decrypted_chunk.to_bytes((decrypted_chunk.bit_length() + 7) // 8, "big").rstrip(b'\x00')

  return ptxt_bytes.decode('utf-8', 'ignore')
