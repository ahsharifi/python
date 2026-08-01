import venus

# students list
students = []

# function to show menu
def menu():
  print(f"""{venus.COLORS["yellow"]}
[============| METHODS |============]
|--| 1. Add student |---------------|
|--| 2. Show student |--------------|
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
    choice = input("Enter your method number: ").strip()

    # conditions for user choice
    match choice:
        case "1":
          print("|===| Enter New Student Information |===|")

          # get new student name and age
          student_name = input("Enter new student name: ")
          student_age = input("Enter new student age: ")

          # validate age
          if not is_num(student_age):
              print("Please enter valid age.")

          # check age
          elif int(student_age) <= 0:
              print("Please enter valid age.")

          else:
              venus.add(
                  students,
                  student_name,
                  int(student_age)
              )

        case "2":
          print("|===| Students List |===|")

          # show students list
          venus.show(students)

        case "3":
            print("|===| Search Student |===|")

            # get student name
            student_name = input("Enter student name: ")

            # show student information
            venus.search(students, student_name)

        case "4":
            print("|===| Remove Student |===|")
            
            # get student name
            student_name = input("Enter student name: ")
            
            # remove student
            venus.remove(students, student_name)

        case "5":
            pass

        case "6":
            print("Goodbye!")
            break

        case _:
            print("Please enter valid method number.")