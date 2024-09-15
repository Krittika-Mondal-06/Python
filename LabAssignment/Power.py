def calculate_power(base, exponent):
  """Calculates the power of a number.

  Args:
    base: The base number.
    exponent: The exponent.

  Returns:
    The result of base raised to the power of exponent.
  """

  result = base ** exponent
  return result

# Get input from the user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
power = calculate_power(base, exponent)

# Print the result
print(base, "^", exponent, "=", power)