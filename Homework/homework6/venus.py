COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "black": "\033[30m",
    "orange": "\033[38;5;208m",
    "purple": "\033[38;5;93m",
    "pink": "\033[38;5;213m",
    "gray": "\033[90m",
    "reset": "\033[0m"
}

# add new student
def add(list, name, age):
  student_info_dic = {
    "name": name,
    "age": age
  }

  list.append(student_info_dic)
  print(f"{COLORS["green"]}Student added seccussfuly{COLORS["reset"]}")

# show students
def show(list):
  for student in list:
    print(f"""{COLORS["cyan"]}
[==========| student {list.index(student) + 1} |==========]
|---| Student name: {student["name"]}      
|---| Student age: {student["age"]}
[==========================]
    {COLORS["reset"]}""")

# search student
def search(list, name):
  # find user
  for student in list:
    if student["name"] == name:
      print(f"""{COLORS["cyan"]}
[=========| User Informations |=========]
|---| name: {student["name"]}
|---| age: {student["age"]}
[=======================================]
      {COLORS["reset"]}""")
      break

# remove student
def remove(list, name):
  # confirmation to remove
  confirm = input(f"Are you sure you want to remove {name}? (y/n)")

  # check confirmation
  if confirm == "y" or "":
    for student in list:
      if student["name"] == name:
        list.remove(student)
        print(f"{COLORS["red"]}{name} removed.")
  else:
    pass