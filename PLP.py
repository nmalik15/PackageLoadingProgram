# Setting global variables
package_weight = 0
total_weight_sent = 0
packages_sent = 0
unused_capacity = 0
max_unused_capacity = 0
max_unused_capacity_package = -1

# 1. Ask user for the number of items

print("\n *** PACKAGE LOADING PROGRAM *** \n")

while True:
    num_items = input("\nHow many items to pack?: ")
    if num_items.isdigit(): # checking if user entered number
        num_items = int(num_items)
        break
    else:
        print("Provide number > 0, not a string! \n")
        continue

