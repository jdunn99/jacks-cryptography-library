from jcl.nt.primes import next_prime
from jcl.nt.divisibility import lcm
from jcl.operations import alpha_to_num, alphabet
import random

def generate_keys():
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

def encrypt(txt, public_key):
  n, e = public_key 
  chunk_size = (n.bit_length() - 1) // 8
  txt_bytes = txt.encode("utf-8")

  ciphertext = []
  for i in range(0, len(txt_bytes), chunk_size):
    chunk = txt_bytes[i : i + chunk_size]
    ciphertext.append(pow(int.from_bytes(chunk, 'big'), e, n))

  return ciphertext

def decrypt(txt, private_key):
  n, d = private_key
  chunk_size = (n.bit_length() - 1) // 8
  
  ptxt_bytes = b''
  for chunk in txt:
    ptxt_bytes += pow(chunk, d, n).to_bytes(chunk_size, 'big').rstrip(b'\x00')

  return ptxt_bytes.decode('utf-8')

public, private = generate_keys()
ciphertext = encrypt("howdy partner", public)
print(ciphertext)
plaintext = decrypt(ciphertext, private)
print(plaintext)


