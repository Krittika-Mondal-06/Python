def count_words(string):
  """Counts the number of words in a given string.

  Args:
    string: The string to count words in.

  Returns:
    The number of words in the string.
  """

  words = string.split()
  return len(words)

# Get input from the user
string = input("Enter a string: ")

# Count the words
word_count = count_words(string)

# Print the result
print("Number of words:", word_count)