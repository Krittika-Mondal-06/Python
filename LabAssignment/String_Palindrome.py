def is_palindrome(string):
  """Checks if a string is a palindrome.

  Args:
    string: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  # Remove spaces and convert to lowercase for case-insensitive comparison
  string = string.replace(" ", "").lower()

  # Compare the string with its reverse
  return string == string[::-1]

# Get input from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
  print(string, "is a palindrome.")
else:
  print(string, "is not a palindrome.")