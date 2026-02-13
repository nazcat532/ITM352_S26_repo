# Program: Check list size and print appropriate message
# Tests lists with varying lengths using if/elif/else control logic

# Define test cases as a list of tuples: (test_name, test_list)
test_cases = [
    ("List with 1 element (fewer than 5)", [42]),
    ("List with 3 elements (fewer than 5)", [10, "hello", 3.14]),
    ("List with 4 elements (fewer than 5)", [10, "hello", 3.14, True]),
    ("List with 5 elements (boundary: exactly 5)", ["apple", "banana", "cherry", "date", "elderberry"]),
    ("List with 7 elements (between 5 and 10)", [1, 2, 3, "four", 5.0, True, None]),
    ("List with 10 elements (boundary: exactly 10)", list(range(10))),
    ("List with 11 elements (more than 10)", list(range(11))),
    ("List with 15 elements (more than 10)", [x for x in range(15)]),
    ("List with 20 elements (more than 10)", list(range(20))),
]

# Test each case
print("=" * 80)
print("TESTING LIST SIZE CONDITIONS")
print("=" * 80)

for test_name, test_list in test_cases:
    print(f"\n{test_name}")
    print(f"List: {test_list}")
    print(f"Length: {len(test_list)}")
    
    if len(test_list) < 5:
        print("Message: This list has fewer than 5 elements.")
    elif len(test_list) <= 10:
        print("Message: This list has between 5 and 10 elements (inclusive).")
    else:
        print("Message: This list has more than 10 elements.")
    print("-" * 80)
