def count_vowels(string):
  """Counts the number of vowels in a given string.

  Args:
    string: The string to count vowels in.

  Returns:
    The number of vowels in the string.
  """

  vowels = "aeiouAEIOU"
  count = 0

  for char in string:
    if char in vowels:
      count += 1

  return count

# Get input from the user
string = input("Enter a string: ")

# Count the vowels
vowel_count = count_vowels(string)

# Print the result
print("Number of vowels:", vowel_count)