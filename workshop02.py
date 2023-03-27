'''
Ejercicio utilizando diccionarios, listas, bucles como while y for y utilizando condicionales 
'''

#Initialize an empty list to store fully qualified names (List)
name_list = []

#Keep accepting names until "END" is entered (Loop while, function append, break and conditionals)
while True:
    name = input("Type a full name to finish typing END: ")
    if name == "END":
        break
    name_list.append(name)

#Create a dictionary to store the number of words in each name (Dictionary)
word_counts = {}

#Iterate through the names in the list and count the words (Loop for, function split and len)
for name in name_list:
    words = name.split()  # Divide
    num_words = len(words)  # Cuenta
    word_counts[name] = num_words  # Almacena

#Print the results (Print and loop for)
print("List of names:")
for name in name_list:
    print(name)
print()
print("Number of words in each name:")
for name, count in word_counts.items():
    print(name, "-", count)
