def reverse_string(string):
  """Reverses a given string.

  Args:
    string: The string to reverse.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

# Get input from the user
string = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(string)

# Print the result
print("The reversed string is:", reversed_string)