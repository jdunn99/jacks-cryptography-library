from jcl.operations import frequency, choose

def vigvec(txt, m, n):
  """
  Gives the frequencies of the letters a through z in positions congruent to n (mod m)

  Parameters
  -
  """
  new_txt = choose(txt, m, n)
  freqs = frequency(new_txt)

  return [round(v / len(new_txt), 7) for k, v in freqs.items()]


def vigenere(txt, v):
  """
  Gives the Vigenere encryption of txt using the vector v
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