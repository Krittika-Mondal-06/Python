def gcd(a, b):
  """Calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The GCD of a and b.
  """

  while b != 0:
    a, b = b, a % b
  return a

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD
gcd_result = gcd(num1, num2)

# Print the result
print("The GCD of", num1, "and", num2, "is", gcd_result)