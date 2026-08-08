class Student():
  def __init__(self, name, age, grade, major, status):
    self.name = name
    self.age = age
    self.grade = grade
    self.major = major
    self.status = status

  def getName(self):
    return self.name
  
  def getAge(self):
    return self.age
  
  def getGrade(self):
    return self.grade
  
student = Student("Amir", 18, 12, "Math", True)
  
print(student.name)
print(student.age)
print(student.grade)
print(student.major)
print(student.status)
print(student.getName())
print(student.getAge())
print(student.getGrade())