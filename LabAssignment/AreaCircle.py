import math

def calculate_circle_area(radius):
  """Calculates the area of a circle.

  Args:
    radius: The radius of the circle.

  Returns:
    The area of the circle.
  """

  area = math.pi * radius * radius
  return area

# Get input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = calculate_circle_area(radius)

# Print the result
print("The area of the circle is:", area)