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

  # Convert to numbers
  numerical = ""
  for char in txt:
    if char == " ":
      continue
    numerical += str(alpha_to_num(char) % 26)

  print(numerical)

  return pow(int(numerical), e, n)

def decrypt(txt, private_key):
  n, d = private_key
  numerical = str(pow(txt, d, n))

  return result

public, private = generate_keys()
# print("KEYS: ", public, private)
ciphertext = encrypt("hello", (3233, 17))
print("CIPHERTEXT: ", ciphertext)
print(decrypt(ciphertext, (3233, 413)))


