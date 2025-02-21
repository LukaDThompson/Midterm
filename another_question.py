import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here

modified_numbers = [] # Make a new list for the modified numbers

for num in random_numbers:
    if num % 2 == 0:  # If the number is even
        modified_numbers.append(num * 2)  # Double it and add to new list
    # If the number is odd, do nothing (it gets removed)

# Step 3: Print the final list
print("Original list:", random_numbers)
print("Modified list (evens doubled, odds removed):", modified_numbers)