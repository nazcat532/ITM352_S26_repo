#Parse through the portions of an email address

# Method 1: Using split() to separete username and domain
email = input("Enter your email address: ")

parts = email.split("@")
username = parts[0]
domain = parts[1]

print("Username:", username)
print("Domain:", domain)

# Method 2: Using index() and slicing
at_symbol_index = email.index("@")
username_manual = email[:at_symbol_index]

