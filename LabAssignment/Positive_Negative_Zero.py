def check_number(number):
  """Checks if a number is positive, negative, or zero.

  Args:
    number: The number to check.

  Returns:
    "Positive" if the number is positive, "Negative" if the number is negative,
    and "Zero" if the number is zero.
  """

  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

# Get input from the user
number = float(input("Enter a number: "))

# Check the number
result = check_number(number)

# Print the result
print("The number is:", result)