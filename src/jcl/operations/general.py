alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def alpha_to_num(char: str) -> int:
  return ord(char) - 97

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

    num = (alpha_to_num(text) + n) % 26
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

def max_vector(v):
  """
  Finds the max value and position from a vector.
  """
  m = max(v)
  i = v.index(m)

  return (m, i)