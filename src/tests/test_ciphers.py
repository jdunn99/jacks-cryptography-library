import pytest
import jcl.ciphers
from random import randint

def test_affine_encryption():
  assert jcl.ciphers.affine.encrypt("cleopatra", 7, 8) == "whkcjilxi"

def test_affine_decryption():
  assert jcl.ciphers.affine.decrypt("mzdvezc", 5, 12) == "anthony"

def test_vigenere_encryption():
  assert jcl.ciphers.vigenere.encrypt("themethodusedforthepreparationandreadingofcodemessagesissimpleintheextremeandatthesametimeimpossibleoftranslationunlessthekeyisknowntheeasewithwhichthekeymaybechangedisanotherpointinfavoroftheadoptionofthiscodebythosedesiringtotransmitimportantmessageswithouttheslightestdangeroftheirmessagesbeingreadbypoliticalorbusinessrivalsetc", [2, 14, 3, 4, 18]) == "vvhqwvvrhmusgjgthkihtssejchlsfcbgvwcrlryqtfsvgahwkcuhwauglqhnslrljshbltspisprdxljsveeghlqwkasskuwepwqtwvspgoelkcqyfnsvwljsniqkgnrgybwlwgoviokhkazkqkxzgyhcecmeiujoqkwfwvefqhkijrclrlkbienqfrjljsdhgrhlsfqtwlauqrhwdmwlgusgikkflryvcwvspgpmlkassjvoqxeggveyggzmljcxxljsvpaivwikvrdrygfrjljslveggveyggeiapuuisfpbtgnwwmuczrvtwglrwugumnczvile"

def test_vigenere_decryption():
  assert jcl.ciphers.vigenere.decrypt("vvhqwvvrhmusgjgthkihtssejchlsfcbgvwcrlryqtfsvgahwkcuhwauglqhnslrljshbltspisprdxljsveeghlqwkasskuwepwqtwvspgoelkcqyfnsvwljsniqkgnrgybwlwgoviokhkazkqkxzgyhcecmeiujoqkwfwvefqhkijrclrlkbienqfrjljsdhgrhlsfqtwlauqrhwdmwlgusgikkflryvcwvspgpmlkassjvoqxeggveyggzmljcxxljsvpaivwikvrdrygfrjljslveggveyggeiapuuisfpbtgnwwmuczrvtwglrwugumnczvile") == "themethodusedforthepreparationandreadingofcodemessagesissimpleintheextremeandatthesametimeimpossibleoftranslationunlessthekeyisknowntheeasewithwhichthekeymaybechangedisanotherpointinfavoroftheadoptionofthiscodebythosedesiringtotransmitimportantmessageswithouttheslightestdangeroftheirmessagesbeingreadbypoliticalorbusinessrivalsetc"

def test_hill_encryption():
  return

def test_hill_decryption():
  return

def test_rsa_encryption():
  return

def test_rsa_decryption():
  return

def test_diffie_hellman_keygen():
  public_key = jcl.ciphers.dh.generate_public_keys()

  alice = randint(1, 100)
  bob = randint(1, 100)

  A = jcl.ciphers.dh.generate_base(alice, public_key)
  B = jcl.ciphers.dh.generate_base(bob, public_key)

  s_a = jcl.ciphers.dh.generate_shared_secret(B, alice, public_key)
  s_b = jcl.ciphers.dhgenerate_shared_secret(A, bob, public_key)

  assert(s_a == s_b)

