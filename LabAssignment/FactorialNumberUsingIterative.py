def factorial_iterative(n):
  """Calculates the factorial of a number using an iterative approach.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """

  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial

number = int(input("Enter a number: "))
result = factorial_iterative(number)
print("The factorial of", number, "is", result)