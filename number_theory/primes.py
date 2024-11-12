from number_theory import divisibility

def relative_prime(*args) -> bool:
  """
  Calculates if the given numbers are relatively prime.
  Useful for operations such as Chinese Remainder Theorem and Euler's Totient Function

  Paramters:
  *args: Inte

  Returns:
  bool
  """

  for i in range(len(args)):
    for j in range(i + 1, len(numbers)):
      if divisibility.gcd(numbers[i], numbers[j]) != 1:
        return False
  return True

def euler_phi(n: int) -> int:
  """
  Calculates Euler's totient function, 
  which determines the number of positive integers less than n 
  that are relatively prime to n

  Parameters:
  n (int): The value we are applying the totient function to

  Returns:
  (int): The number of positive integers relatively prime to n
  """
   
