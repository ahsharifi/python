# students list
students = []

# function to show menu
def menu():
  print("""
[============| METHODS |============]
|--| 1. Add student |---------------|
|--| 2. Show student |--------------|
|--| 3. Search student |------------|
|--| 4. Remove student |------------|
|--| 5. Show number of students |---|
|--| 6. Exit the app |--------------|
[===================================]
  """)

# show menu
menu()

# get user choice
choice = input("Enter your method number: ")

# conditions for user choice
match choice:
  case "1":
    breakpoint
  case "2":
    breakpoint
  case "3":
    breakpoint
  case "4":
    breakpoint
  case "5":
    breakpoint
  case "6":
    breakpoint
  case _:
    print("Please enter valid method number.")
    menu()
    choice = input("Enter your method number: ")