# Original tuple from Exercise 3
data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

# Get user input
new_item = input("Enter a value to append to the tuple: ")

# Explain why error occurs
print("\nExplanation:")
print("Tuples are immutable in Python, so methods like append() do not exist.")
print("Using indexing also won't fix this, because you cannot assign a new value to a new index or extend the tuple.")

# Attempt to append and catch the error
try:
    data.append(new_item)  # This will raise an AttributeError
except AttributeError as e:
    print("\nError detected:")
    print(f"Attempted to append to a tuple. Error message: {e}")
    # Handle the error by creating a new tuple with the new item
    data = data + (new_item,)
    print("Handled by creating a new tuple including the new item.")

# Print the updated tuple
print("\nUpdated tuple:", data)