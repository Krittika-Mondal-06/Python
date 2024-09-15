def generate_multiplication_table(number):
  """Generates a multiplication table for a given number.

  Args:
    number: The number for which to generate the multiplication table.
  """

  for i in range(1, 21):
    product = number * i
    print(number, "x", i, "=", product)

# Get input from the user
number = int(input("Enter a number: "))

# Generate the multiplication table
generate_multiplication_table(number)