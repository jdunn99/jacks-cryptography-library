import pytest
import jcl.ciphers

def test_affine_encryption():
  assert jcl.ciphers.affine.encrypt("cleopatra", 7, 8) == "whkcjilxi"

def test_affine_decryption():
  assert jcl.ciphers.affine.decrypt("mzdvezc", 5, 12) == "anthony"
