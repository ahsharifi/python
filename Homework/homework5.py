# jam function
def jam(num1: float = 0, num2: float = 0):
  return num1 + num2

# tafrigh function
def tafrigh(num1: float = 0, num2: float = 0):
  return num1 - num2

# zarb function
def zarb(num1: float = 0, num2: float = 0):
  return num1 * num2

# taghsim function
def taghsim(num1: float = 0, num2: float = 0):
  if num2 == 0:
    return "Error: Division by zero"
  return num1 / num2