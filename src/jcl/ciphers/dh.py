from jcl.nt.primes import next_prime
from jcl.nt.modular import primitive_root
import random

"""
Diffie-Hellman key exchange protocol

"""

def generate_public_keys():
  
  # Find a random prime modulus p and a primitive root base g 
  p = next_prime(random.randint(2, 1024))
  roots = primitive_root(p)

  # Select a random primitive root
  g = roots[random.randint(0, len(roots))]

  return p, g

def generate_base(secret_integer, public_key):
  p, g = public_key
  return pow(g, secret_integer, p)

def generate_shared_secret(base, secret_integer, public_key):
  p, _ = public_key
  return pow(base, secret_integer, p)

public_key = generate_public_keys()

alice = 3
bob = 4

A = generate_base(alice, public_key)
B = generate_base(bob, public_key)

s_a = generate_shared_secret(B, alice, public_key)
s_b = generate_shared_secret(A, bob, public_key)

assert(s_a == s_b)
