# make foods list
foods_list = ["kebab", "chicken", "pizza", "sandwich", "cheese burgur"]
print(foods_list)

# add new food to the list
foods_list.append("pasta")
print(foods_list)

# remove 3rd food of list
foods_list.remove(foods_list[2])
print(foods_list)

print("=============================")

# [================ Factorial ================]

# get number from user
number = int(input("Enter your number: "))

if number < 0:
  print("Factorial is not defined for negative numbers.")
else:
# user entered number
  factorial = number

  # find factorial of number
  for i in range(1, number):
    factorial *= (number - i)

  print(factorial)

print("=============================")

# [================ Fibonachi ================]

# get number of fibonachies from user
fibonachi_numbers = int(input("Enter number of fibonachi numbers: "))

if fibonachi_numbers <= 0:
  print("Please enter a positive integer.")
else:

  # set starter numbers [0, 1]
  old_num = 0
  new_num = 1

  # find fibonachies
  for i in range(fibonachi_numbers):
    print(old_num)

    # set new values in 2 types:
    # 1)
    # temp = old_num
    # old_num = new_num
    # new_num = old_num + new_num
    # 2)
    old_num, new_num = new_num, old_num + new_num