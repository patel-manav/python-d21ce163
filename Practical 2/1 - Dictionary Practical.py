# Dictionary Practical - 1
# Write a Python script to check whether a given key already exists in a dictionary.

# Declare Dictionary
Car = {
     "Brand":"Toyota",
     "Model":"Camry",
     "Year":"2021"
}
# Define Function
def Key_Checker(x):
  # Logic
  if x in Car:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
# Call Function
Key_Checker('Brand')
Key_Checker('Modell')

################# Created By Manav Dadhaniya - D21CE163 #####################

# Dictionary Practical - 2
# Write a Python script to merge two Python dictionaries.

# Declare Dictionary
Car = {
    'Brand':"Toyota",
    "Model":"Camry",
    "Year":"2021"
}
Bike = {
    "Brandd":"Honda",
    "Modell":"Shine",
    "Yearr":"2021"
}
#Update Dictionary
Vec = Car.update(Bike)
# Print Dictionary
print(Car)

################# Created By Manav Dadhaniya - D21CE163 #####################

# Dictionary Practical - 3
# Write a Python program to sum all the items in a dictionary.

# Delcare Dictionary
Car = {
    1:10,
    2:20,
    3:30
}
# Print Dictionary Sum
print(sum(Car.values()))

################# Created By Manav Dadhaniya - D21CE163 #####################

# Dictionary Practical - 4
# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# Declare Dictionary
SampleDictionary = {
    0:10,
    1:20
}
# Add Element In Dictionary
SampleDictionary.update({2:30})
# Print Updated Dictionary
print (SampleDictionary)

################# Created By Manav Dadhaniya - D21CE163 #####################

# Dictionary Practical - 5
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Declare Dictionary
dic1 = {
    1:10,
    2:20
}
dic2 = {
    3:30,
    4:40
}
dic3 = {
    5:50,
    6:60
}
# Merge Two Dictionary In One Dictionary
dic1.update(dic2)
dic1.update(dic3)
# Print Updated Merge Dictionary
print (dic1)

################# Created By Manav Dadhaniya - D21CE163 #####################
