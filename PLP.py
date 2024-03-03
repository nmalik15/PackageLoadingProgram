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

for i in range(num_items): # iterating through number of items
    while True:
        try:
            weight = int(input(f"Enter the weight of item {i + 1} (0 to terminate): "))
            if weight == 0:
                break
            elif not (1 <= weight <= 10):
                print("Invalid weight. Please enter a weight between 1 and 10 kg.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    print(f"Weight of item no. {i + 1} is {weight} kg. \n")

    # checking for package weight and limits reached
    if package_weight + weight > 20:
        total_weight_sent += package_weight
        if 20 - package_weight > max_unused_capacity:
            max_unused_capacity = 20 - package_weight
            max_unused_capacity_package = packages_sent + 1
        print("Package limit reached! Current package sent. New package started.")
        package_weight = weight
        packages_sent += 1
    else:
        package_weight += weight

    if weight == 0:
        break

