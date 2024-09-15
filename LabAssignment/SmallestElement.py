def find_smallest(numbers):
  """Finds the smallest element in a list.

  Args:
    numbers: The list of numbers.

  Returns:
    The smallest number in the list.
  """

  smallest = numbers[0]
  for num in numbers:
    if num < smallest:
      smallest = num
  return smallest

# Get input from the user
numbers = input("Enter the numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Find the smallest number
smallest_number = find_smallest(numbers)

# Print the result
print("The smallest number is:", smallest_number)