def find_largest(numbers):
  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest

numbers = [10, 5, 20, 3, 15]
largest_number = find_largest(numbers)
print("The largest number in the list is:", largest_number)