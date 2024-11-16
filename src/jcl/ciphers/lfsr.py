import numpy

def lfsr(c, k, n):
  """
  Gives the sequence of n bits produced by the recurrence that has coefficients given by the vector c.
  The initial values of the bits are given by the vector k
  """
  result = k
  positives = [i for i in range(len(c)) if c[i] == 1]
  
  for i in range(n - len(k)):
    new_bit = 0
    for j in positives:
      new_bit ^= result[i + j]
    result.append(new_bit)

  return result

def build_lfsr_matrix(v, n):
  """
  Builds the square matrix for solving lfsr linear equations
  """
  matrix = []
  for i in range(n):
    row = v[i : i + n]

      # Must be a square matrix
    if len(row) < n:
      break
    matrix.append(row)

  return numpy.array(matrix)

def lfsr_length(v, n):
  """
  Given a guess n for the length of the recurrence relationthat generates the binary
  vector v, it computes the coefficients of the recurrence.
  """

  result = []

  for m in range(1, n + 1):
    matrix = build_lfsr_matrix(v, m)
    det = round(numpy.linalg.det(matrix)) % 2
    result.append((m, det))

  return result

def lfsr_solve(v, n):
  """
  Given a guess n for the length of the recurrence that generates the binary vector v,
  it computes the coefficients of the recurrence
  """

  # Build the n x n matrix
  matrix = build_lfsr_matrix(v, n)

  # Build the vector [x_m+1, x_m+2, ... , x_2m]
  b = v[n : 2 * n]

  # Solve for coefficients (mod 2)
  # TODO: Look into writing my own for better understanding. Numpy is powerful though.
  # Originally used linalg.solve but it was giving incorrect coefficients.
  c, _, _, _ = (numpy.linalg.lstsq(matrix, b, rcond=None))
  return list(numpy.round(c).astype(int) % 2)

