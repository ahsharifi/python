class Student():
  def __init__(self, name: str, age: int, grade: int, major: str, status: bool):
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
  
print("[==============| Student Information |==============]")
print(student.name)
print(student.age)
print(student.grade)
print(student.major)
print(student.status)
print(student.getName())
print(student.getAge())
print(student.getGrade())

class Product:
  def __init__(self, name: str, count: int, price: float, status: bool):
    self.name = name
    self.count = count
    self.price = price
    self.status = status  

  def getName(self):
    return self.name
  
  def getPriceWithDiscount(self, discount: float):
    price = self.price * ((100 - discount) / 100)
    return price
  
  def getInventoryPrice(self):
    return self.count * self.price

product = Product("pen", 10, 10000, 1)

print("[==============| Product Information |==============]")
print(product.name)
print(product.getInventory())
print(product.getPriceWithDiscount(12))
print(product.getInventoryPrice())