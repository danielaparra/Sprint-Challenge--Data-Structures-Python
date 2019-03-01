import time

start_time = time.time()ß

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# This method currently has 0(n^2) time complexity.
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# This new method has 0(2n) -> 0(n) big o time complexity.
# Initalize a dictionary and add all names from names 1 list.
dictionary = dict()
for name in names_1:
    dictionary[name] = name

# Initialize duplicates.
duplicates = []
# Check if the dict contains a name from names 2 list.
for name2 in names_2:
    # If so, add name to duplicates array.
    if dictionary.get(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

