# Function that checks a single purchase against a budget
def check_budget(purchase, limit):
    if purchase > limit:
        return "Over budget"
    else:
        return "Within budget"

# List of recent purchases
recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50

# Iterate through the list and print results
for purchase in recent_purchases:
    result = check_budget(purchase, budget)
    print(f"Purchase ${purchase:.2f}: {result}")

# --- Test Cases ---
def test_check_budget():
    # Test case 1: purchase under budget
    assert check_budget(25, 50) == "Within budget", "Test case 1 failed"
    # Test case 2: purchase exactly at budget
    assert check_budget(50, 50) == "Within budget", "Test case 2 failed"
    # Test case 3: purchase over budget
    assert check_budget(75, 50) == "Over budget", "Test case 3 failed"
    print("All test cases passed!")

# Run the test function
test_check_budget()