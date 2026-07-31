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

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("""\033[93m
Select operation:
|--1. Jam
|--2. Tafrigh
|--3. Zarb
|--4. Taghsim
\033[0m  
""")

choice = input("Enter choice (1/2/3/4): ")

match choice:
  case "1":
    result = jam(number1, number2)
    print(f"\033[92mResult: {result}\033[0m")
  case "2":
    result = tafrigh(number1, number2)
    print(f"\033[92mResult: {result}\033[0m")
  case "3":
    result = zarb(number1, number2)
    print(f"\033[92mResult: {result}\033[0m")
  case "4":
    result = taghsim(number1, number2)
    print(f"\033[92mResult: {result}\033[0m")
  case _:
    print("\033[91mInvalid input\033[0m")