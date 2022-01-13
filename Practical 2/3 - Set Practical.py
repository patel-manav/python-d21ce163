# Set Practical - 1
# Write a Python program to add member(s) in a set and clear a set

# Declare Set
set = {10,20,30,40}
# Add One Element In Set
set.add(50)
# Print Set
print(set)
# Clear All Element In Set
set.clear()
# Print Set
print(set)

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 2
# Write a Python program to remove an item from a set if it is present in the set.

# Declare Set
set = {10,20,30,40}
# Declare Default Variable
x=50
c=0
# Logic
for y in set:
    if x==y:
        print('X is available in set');
        c=1
if c==0:
    print('X is not available in set')

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 3
# Write a Python program to create an intersection, Union, difference of sets.

# Declare Set
set1 = {0, 2, 4, 6, 8}
set2 = {1, 2, 3, 4, 5}
# Union,Intersectino & Difference Operation Perform On Set
print("Union :", set1 | set2)
print("Intersection :", set1 & set2)
print("Difference :", set1 - set2)

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 4
# Write a Python program to find maximum and the minimum value in a set.

# Declare Set
set = {10,20,30,40,50}
# Find Minimum Value & Print Minimum Value
print('Minimum Value of Set = ', min(set))
# Find Maximum Value & Print Maximum Value
print('Maximum Value of Set = ', max(set))

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 5
# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

# Delcare list
list=['Cars', 'Cars', 'Flowers', 'Cars','Cats']
# Declare tuple
tuple = (1,2,3,4,5,1,3,1,1)
# Declare Dictionary
Car = {
     "Brand":"Toyota",
     "Model":"Camry",
     "Year":"2021",
     "Brand":"Toyota"
 }
# Logic
from collections import Counter
l = Counter(list)
l.most_common(1)

t = Counter(tuple)
t.most_common(1)

d = Counter(Car)
d.most_common(1)
# Print Common Element In List
print ("",l.most_common(1))
# Print Common Element In Tuple
print ("",t.most_common(1))
# Print Common Element In Dictionary
print ("",d.most_common(1))

################# Created By Manav Dadhaniya - D21CE163 #####################
