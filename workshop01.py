'''
Ejercicio utilizando diccionarios, listas, bucles como while y for y utilizando condicionales 
'''

#Initialize an empty dictionary to store even and odd counts (Dictionary)
numCounts = {
    "even": 0,
    "odd": 0
}

#Initialize an empty list to store the numbers (List)
num_list = []

#Keep accepting integers until 99999 is entered (Loop while, function append, break and conditionals)
while True:
    num = int(input("Enter a number until you enter 99999 to finish: "))
    if num == 99999:
        break
    num_list.append(num)

#Count the number of even and odd integers (Loop for and conditionals)
for num in num_list:
    if num % 2 == 0:
        numCounts["even"] += 1
    else:
        numCounts["odd"] += 1

#Print the results (Print)
print("There are", numCounts["even"], "even numbers and", numCounts["odd"], "odd numbers in the list.")

'''
Ejercicio utilizando diccionarios, listas, bucle while y utilizando condicionales 
'''

from collections import Counter

#Initialize an empty list to store the numbers (List)
num_list = []

#Keep accepting integers until 99999 is entered (Loop while and conditionals)
while True:
    num = int(input("Enter an integer (99999 to stop): "))
    if num == 99999:
        break
    num_list.append(num)

#Count even and odd numbers using Counter (Function counter and lambda)
num_counts = Counter(num_list)
even_count = num_counts[lambda x: x % 2 == 0]
odd_count = num_counts[lambda x: x % 2 != 0]

#Print the results (Print)
print("There are", even_count, "even numbers and", odd_count, "odd numbers in the list.")
