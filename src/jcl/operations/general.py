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


