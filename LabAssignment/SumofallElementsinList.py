def sum_of_list(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum

numbers = [1, 2, 3, 4, 5]
result = sum_of_list(numbers)
print("The sum of the elements in the list is:", result)