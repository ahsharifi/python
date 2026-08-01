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

# check if input is a number
def is_number(num: str):
  try:
    float(num)
    return True
  except ValueError:
    return False

# get numbers from user
number1 = input("Enter the first number: ").replace(",", ".")
number2 = input("Enter the second number: ").replace(",", ".")

# condition to check if the inputs are valid numbers
if not is_number(number1) or not is_number(number2):
  print("\033[91mInvalid input: Please enter valid numbers\033[0m")
  exit()

# list of operations
print("""\033[93m
Select operation:
|--1. Jam
|--2. Tafrigh
|--3. Zarb
|--4. Taghsim
\033[0m  
""")

# get operation choice from user
choice = input("Enter choice (1/2/3/4): ")

# show result
match choice:
  case "1":
    result = jam(float(number1), float(number2))
    print(f"\033[92mResult: {result}\033[0m")
  case "2":
    result = tafrigh(float(number1), float(number2))
    print(f"\033[92mResult: {result}\033[0m")
  case "3":
    result = zarb(float(number1), float(number2))
    print(f"\033[92mResult: {result}\033[0m")
  case "4":
    result = taghsim(float(number1), float(number2))
    print(f"\033[92mResult: {result}\033[0m")
  case _:
    print("\033[91mInvalid input\033[0m")