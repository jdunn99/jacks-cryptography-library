from jcl.operations import frequency, choose, coinc, corr, max_vector, shift

def vigvec(txt, m, n):
  """
  Gives the frequencies of the letters a through z in positions congruent to n (mod m)

  Parameters
  -
  """
  new_txt = choose(txt, m, n)
  freqs = frequency(new_txt)

  return [round(v / len(new_txt), 7) for k, v in freqs.items()]

def encrypt(txt: str, v: list[int]) -> str:
  """
  Gives the Vigenere encryption of txt using the vector v

  Parameters
  ---------
  txt : str
        Plaintext being encrypted
  v : list[int]
      Cipher key representing corresponding shifts

  Returns
  -------
  ciphertext : str
               The resulting ciphertext following vigenere encryption 
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

def decrypt(txt):
  """
  Given a Vigenere ciphertext, finds the key and decrypts the cipher.
  Follows the general structure
    1. Find the length of the key
      a. Finds the shift with the most coincidences with the original ciphertext

    2. Build the key
      a. For each i, 1 <= i <= n 
      b. Find the frequency vector in positions congruent to i (mod n)
      c. Apply the dot product to the alphabet frequency vector
      d. Find the max element of the resulting dot product
      e. Add the index of the max element to the key

    3. Decrypt using the negative values of the key and the encrypt function

  Parameters
  ---------
  txt : str
        Ciphertext being decrypted
 
  Returns
  -------
  plaintext : str
              The resulting plaintext following the decryption
  """
  key = []

  # Find length of key
  m = -1
  length = -1
  for i in range(1, 6):
    n = coinc(txt, i)
    if n > m:
      m = n
      length = i
  
  # Build the key
  for i in range(1, length + 1):
    vector = vigvec(txt, 15, i)
    dot_products = corr(vector)
    _, i = max_vector(dot_products)
    key.append(i)

  key = [k * - 1 for k in key]
  return encrypt(txt, key)

print(encrypt("themethodusedforthepreparationandreadingofcodemessagesissimpleintheextremeandatthesametimeimpossibleoftranslationunlessthekeyisknowntheeasewithwhichthekeymaybechangedisanotherpointinfavoroftheadoptionofthiscodebythosedesiringtotransmitimportantmessageswithouttheslightestdangeroftheirmessagesbeingreadbypoliticalorbusinessrivalsetc", [2, 14, 3, 4, 18]))