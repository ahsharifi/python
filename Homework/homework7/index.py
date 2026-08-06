import venus

# function to show menu
def menu():
  print(f"""{venus.COLORS["yellow"]}
[============| METHODS |============]
|--| 1. Add student |---------------|
|--| 2. Show students |-------------|
|--| 3. Search student |------------|
|--| 4. Remove student |------------|
|--| 5. Show number of students |---|
|--| 6. Exit the app |--------------|
[===================================]
  {venus.COLORS["reset"]}""")

# check age
def is_num(num: str):
  try:
    int(num)
    return True
  except:
    return False

while True:
    # show menu and input after case
    menu()
    choice = input(f"{venus.COLORS["blue"]}Enter your method number: {venus.COLORS["reset"]}").strip()

    # conditions for user choice
    match choice:
        case "1":
          print(f"{venus.COLORS["gray"]}\n|===| Enter New Student Information |===|{venus.COLORS["reset"]}")

          # get new student name and age
          student_name = input("Enter new student name: ").capitalize()
          student_age = input("Enter new student age: ")

          # validate age
          if not is_num(student_age):
              print("Please enter valid age.")

          # check age
          elif int(student_age) <= 0:
              print("Please enter valid age.")

          else:
              venus.add(
                  student_name,
                  int(student_age)
              )

        # case "2":
        #   print(f"{venus.COLORS["gray"]}\n|===| Students List |===|{venus.COLORS["reset"]}")

        #   # show students list
        #   venus.show()

        # case "3":
        #     print(f"{venus.COLORS["gray"]}\n|===| Search Student |===|{venus.COLORS["reset"]}")

        #     # get student name
        #     student_name = input("Enter student name: ").capitalize()

        #     # show student information
        #     venus.search(student_name)

        # case "4":
        #     print(f"{venus.COLORS["gray"]}\n|===| Remove Student |===|{venus.COLORS["reset"]}")
            
        #     # get student name
        #     student_name = input("Enter student name: ").capitalize()
            
        #     # remove student
        #     venus.remove(student_name)

        # case "5":
        #     print(f"{venus.COLORS["gray"]}\n|===| Numbers Of Students |===|{venus.COLORS["reset"]}")

        #     # show numbers of students
        #     venus.length()  

        case "6":
            print(f"{venus.COLORS["pink"]}\nGoodbye!{venus.COLORS["reset"]}")
            break

        case _:
            print(f"{venus.COLORS["red"]}\nPlease enter valid method number.{venus.COLORS["reset"]}")