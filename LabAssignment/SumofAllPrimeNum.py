def is_prime(number):
  """Checks if a number is prime.

  Args:
    number: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if number <= 1:
    return False
  if number <= 3:
    return True
  if number % 2 == 0 or number % 3 == 0:
    return False

  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6

  return True

def sum_of_primes(n):
  """Calculates the sum of all prime numbers from 1 to n.

  Args:
    n: The upper limit.

  Returns:
    The sum of all prime numbers from 1 to n.
  """

  sum = 0
  for num in range(2, n + 1):
    if is_prime(num):
      sum += num
  return sum

# Calculate the sum of prime numbers from 1 to 100
result = sum_of_primes(100)
print("The sum of all prime numbers from 1 to 100 is:", result)