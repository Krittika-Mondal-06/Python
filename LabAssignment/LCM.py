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

def lcm(a, b):
  """Calculates the least common multiple (LCM) of two numbers using the formula LCM(a, b) = (a * b) / GCD(a, b).

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The LCM of a and b.
  """

  return (a * b) // gcd(a, b)

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the LCM
lcm_result = lcm(num1, num2)

# Print the result
print("The LCM of", num1, "and", num2, "is", lcm_result)