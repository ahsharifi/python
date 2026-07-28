# [===============| List |===============]
fruits = ["apple", "banana", "orange"]

# [===============| Tuple |===============]
games = ("PUBG", "Minecraft", "CS2", "Dota 2", "CS2")

# [===============| Set |===============]
group_members = {"Ali", "Mamad", "Reza", "Amin"}

# [===============| Dictionary |===============]
user_data = {
  "firstname": "Amirhossein",
  "lastname": "Sharifi",
  "email": "ahsharifidev@gmail.com",
  "phone": 9038834741,
  "age": 18,
  "city": "Tabriz",
  "major": "Mathematics",
  "school": "Meraj Andisheh",
  "is_admin": True
}

# [===============| Show Informations |===============]

# get keys and values from dictionary
for key, value in user_data.items():
  # condition to show only major and school
  if key == "major" or key == "school":
    print(f"{key.capitalize()}: {value}")

# [===============| 15 Methods |===============]

# 1) copy() (List)
# 2) append() (List)
# 3) remove() (List)
# 4) clear() (List)
# 5) count() (Tuple)
# 6) discard() (Set)
# 7) pop() (Set)
# 8) items() (Dictionary)
# 9) keys() (Dictionary)
# 10) values() (Dictionary)
# 11) get() (Dictionary)
# 12) update() (Dictionary)
# 13) pop() (Dictionary)
# 14) add() (Set)
# 15) index() (List)

# List Methods
print("\n [===============| LIST |===============]")

# 1) copy() Method
copy_fruits = fruits.copy()  # copy list to another variable
print(f"\n Copied Fruits: {copy_fruits}")


# 2) append() Method
fruits.append("kiwi")  # add item to list
print(f"\n Fruits: {fruits}")


# 3) remove() Method
fruits.remove("banana")  # remove item from list
print(f"\n Fruits: {fruits}")


# 4) clear() Method
fruits.clear()  # clear all items from list
print(f"\n Fruits: {fruits}")


# Tuple Methods
print("\n [===============| TUPLE |===============]")

# 5) count() Method
print(f"\n Games Count: {games.count('CS2')}")  # get count of tuple's item


# Set Methods
print("\n [===============| SET |===============]")

# 6) discard() Method
group_members.discard("Ali")
print(f"\n Group Members: {group_members}")  # remove item from set


# 7) pop() Method
group_members.pop()  # remove first item from set
print(f"\n Group Members: {group_members}")


# Dictionary Methods
print("\n [===============| DICTIONARY |===============]")

# 8) items() Method
print(f"\n User Items: {user_data.items()}")  # get all items from dictionary


# 9) keys() Method
print("\n Keys:")  # get all keys from dictionary
for key in user_data.keys():
  print(f"- {key.capitalize()}")


# 10) values() Method
print("\n Values:")  # get all values from dictionary
for value in user_data.values():
  print(f"- {value}")


# 11) get() Method
print(f"\n User Email: {user_data.get('email')}")  # get value by key


# 12) update() Method
user_data.update({"country": "Iran"})  # add new key-value
print(f"\n User Data: {user_data}")


# 13) pop() Method
user_data.pop("phone")  # remove key from dictionary
print(f"\n User Data: {user_data}")


# 14) add() Method
group_members.add("Hossein")  # add new member to set
print(f"\n Group Members: {group_members}")


# 15) index() Method
print(f"\n Orange Index: {copy_fruits.index('orange')}")  # find item index