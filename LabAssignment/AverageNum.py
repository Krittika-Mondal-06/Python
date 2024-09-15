def calculate_average(numbers):
  """Calculates the average of a list of numbers.

  Args:
    numbers: The list of numbers.

  Returns:
    The average of the numbers.
  """

  if not numbers:
    return None  # Handle empty list

  sum_of_numbers = sum(numbers)
  average = sum_of_numbers / len(numbers)
  return average

# Get input from the user
numbers = input("Enter the numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Calculate the average
average = calculate_average(numbers)

# Print the result
if average is not None:
  print("The average of the numbers is:", average)
else:
  print("The list is empty.")