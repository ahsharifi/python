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

def writeFile(name: str = "students"):
  return open(f"{name}.txt", "w")

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

class Person:
  def __init__(self, name):
    self.name = name
    

class Student(Person):
  def __init__(self, name, age):
    Person.__init__(self, name)
    self.age = age

  def add(self, file_name):
    ID = getNextId(file_name)
    file = appendFile(file_name)
    with file as f:
      f.write(f"ID: {ID} | Name: {self.name} | Age: {self.age}\n") 
    
    print(f"{COLORS["green"]}Student added seccussfuly{COLORS["reset"]}")

  def showStudents(self, file_name):
    with readFile(file_name) as f:
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

  def searchStudent(self, file_name, ID):
    with readFile(file_name) as f:
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

  def removeStudent(self, file_name, ID):
    # confirmation to remove
    confirm = input(f"Are you sure you want to remove id:{ID}? (y/n)")

    if confirm == "y" or confirm == "":
      lines = []
      found = False

      try:
        with readFile(file_name) as file:
          lines = file.readlines()
        
        new_lines = []
        for line in lines:
          match = re.search(r"ID: (\d+)", line)

          if match:
            current_ID = match.group(1)
            if current_ID == str(ID):
              found = True
              continue
            
          new_lines.append(line)

        if found:
          with writeFile(file_name) as f:
            f.writelines(new_lines)
          print(f"{COLORS['red']}Student with ID {ID} removed successfully.{COLORS['reset']}")
        else:
          print(f"{COLORS['yellow']}Student with ID {ID} not found.{COLORS['reset']}")
      except:
        print(f"{COLORS['red']}Error: File not found.{COLORS['reset']}")

    else:
      print(f"{COLORS["red"]}Operation cancelled.{COLORS["reset"]}")

  def count(self, file_name):
    with readFile(file_name) as file:
      rows = len(file.readlines())

    print(f"{COLORS["cyan"]}numbers of students: {rows}{COLORS["reset"]}")
  
# numbers of students
def length(file_name):
  students = Student("", 0)
  students.count(file_name)