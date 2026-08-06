import re

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

# create students file
def createFile(name: str = "students"):
  file = open(f"{name}.txt", "x")

# read file
def readFile(name: str = "students"):
  return open(f"{name}.txt", "r")

# write file
def appendFile(name: str = "students"):
  return open(f"{name}.txt", "a")

# define next id
def getNextId(file_name: str = "students"):
  try:
    with readFile(file_name) as file:
      lines = file.readlines()
      if lines:
        last_line = lines[-1]
        last_id = re.search(r"ID: (\d+)", last_line)
        
        if last_id:
          return int(last_id.group(1)) + 1
  except:
    pass

  return 1

# add new student
def add(file_name, name, age):
  ID = getNextId(file_name)
  file = appendFile(file_name)
  with file as f:
    f.write(f"ID: {ID} | Name: {name} | Age: {age}\n") 
  
  print(f"{COLORS["green"]}Student added seccussfuly{COLORS["reset"]}")

# show students
def show(file_name):
  file = readFile(file_name)
  with file as f:
    for line in f:
      student_id = re.search(r"ID: (\d+)", line).group(1)
      student_name  = re.search(r"Name: ([^|]+)", line).group(1).strip()
      student_age = re.search(r"Age: (\d+)", line).group(1)

      print(f"""{COLORS["cyan"]}
[==========| student {student_id} |==========]
|---| Student name: {student_name}      
|---| Student age: {student_age}
[==========================]
    {COLORS["reset"]}"""
      )

# search student
def search(file_name, ID):
  file = readFile(file_name)
  with file as f:
    for line in f:
      student_ID = re.search(r"ID: (\d+)", line).group(1)
      if student_ID == ID:
        student_name = re.search(r"Name: ([^|]+)", line).group(1)
        student_age = re.search(r"Age: (\d+)", line).group(1)

        print(f"""{COLORS["cyan"]}
[==========| student {student_ID} |==========]
|---| Student name: {student_name}      
|---| Student age: {student_age}
[==========================]
    {COLORS["reset"]}"""
        )

# # remove student
# def remove(name):
#   # confirmation to remove
#   confirm = input(f"Are you sure you want to remove {name}? (y/n)")

#   # check confirmation
#   if confirm == "y" or "":
#     for student in list:
#       if student["name"] == name:
#         list.remove(student)
#         print(f"{COLORS["red"]}{name} removed.")

# # numbers of students
# def length():
#   print(f"{COLORS["cyan"]}numbers of students: {len(list)}{COLORS["reset"]}")