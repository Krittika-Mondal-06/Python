def sum_of_even_numbers(n):
  """Calculates the sum of all even numbers from 1 to n.

  Args:
    n: The upper limit.

  Returns:
    The sum of all even numbers from 1 to n.
  """

  sum = 0
  for i in range(2, n + 1, 2):
    sum += i
  return sum

# Calculate the sum of even numbers from 1 to 100
result = sum_of_even_numbers(100)
print("The sum of all even numbers from 1 to 100 is:", result)