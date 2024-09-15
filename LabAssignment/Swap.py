def swap_values(x, y):
  temp = x
  x = y
  y = temp

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Before swapping: x =", x, "y =", y)
swap_values(x, y)
print("After swapping: x =", y, "y =", x)