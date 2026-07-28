# [===============| List |===============]
fruits = ["apple", "banana", "orange"]

# [===============| Tuple |===============]
games = ("chess", "soccer", "basketball")

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