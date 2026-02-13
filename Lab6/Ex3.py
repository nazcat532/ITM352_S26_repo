def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress


def determine_progress2(hits, spins):
    """
    Version 2: Using early returns with simple if statements (no nesting, elif, or else).
    Each return statement handles one specific condition.
    """
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    if hits_spins_ratio <= 0:
        return "Get going!"
    
    if hits_spins_ratio >= 0.5 and hits < spins:
        return "You win!"
    
    if hits_spins_ratio >= 0.25:
        return "Almost there!"
    
    return "On your way!"


def determine_progress3(hits, spins):
    """
    Version 3: Using if-elif conditions for clarity and readability.
    Flattened logic without deep nesting.
    """
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    # Check if no progress or zero ratio
    if hits_spins_ratio <= 0:
        return "Get going!"
    # Check if ratio is high and hits < spins (winning condition)
    elif hits_spins_ratio >= 0.5 and hits < spins:
        return "You win!"
    # Check if ratio is at least 0.25
    elif hits_spins_ratio >= 0.25:
        return "Almost there!"
    # Default case: some progress but less than 0.25
    else:
        return "On your way!"


def test_determine_progress(progress_function):
    """
    Test function that uses assert to verify all possible return values
    of the determine_progress1 function.
    """
    
    # Test case 1: spins = 0 returns "Get going!"
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed"
    
    # Test case 2: hits = 0 (ratio = 0) returns "Get going!"
    assert progress_function(0, 10) == "Get going!", "Test case 2 failed"
    
    # Test case 3: ratio between 0 and 0.25 (e.g., 0.2) returns "On your way!"
    assert progress_function(2, 10) == "On your way!", "Test case 3 failed"
    
    # Test case 4: ratio = 0.25 returns "Almost there!"
    assert progress_function(5, 20) == "Almost there!", "Test case 4 failed"
    
    # Test case 5: ratio between 0.25 and 0.5 (e.g., 0.3) returns "Almost there!"
    assert progress_function(3, 10) == "Almost there!", "Test case 5 failed"
    
    # Test case 6: ratio = 0.5 with hits < spins returns "You win!"
    assert progress_function(5, 10) == "You win!", "Test case 6 failed"
    
    # Test case 7: ratio > 0.5 with hits < spins returns "You win!"
    assert progress_function(7, 10) == "You win!", "Test case 7 failed"
    
    # Test case 8: ratio s= 0.5 with hits = spins returns "Almost there!" (hits NOT < spins)
    assert progress_function(5, 5) == "Almost there!", "Test case 8 failed"
    
    print("All tests passed!")

# Run the tests
print("Testing determine_progress1:")
test_determine_progress(determine_progress1)

print("\nTesting determine_progress2:")
test_determine_progress(determine_progress2)

print("\nTesting determine_progress3:")
test_determine_progress(determine_progress3)

print("\n" + "="*70)
print("COMPARISON OF ALL VERSIONS")
print("="*70)
print("""
VERSION 1 (Deeply Nested If):
- Uses nested if statements within if statements
- Harder to read and understand the logic flow
- Condition order is tightly coupled
- More prone to logic errors when modifying
- Variable 'progress' is reassigned multiple times
- Difficult to trace through complex nesting

VERSION 2 (Simple If with Early Returns):
- Uses simple if statements (no nesting, elif, or else)
- Each condition is independent and clearly separated
- Early returns make intent obvious
- Very easy to read and follow
- Good for straightforward logic flow
- No unnecessary variable assignments

VERSION 3 (If-Elif-Else):
- Uses flat if-elif-else structure
- Each condition is evaluated in order
- Very clear logical progression
- Easy to read and understand
- More conventional Python style
- Follows natural decision tree patterns

BEST PRACTICES RANKING:
1. VERSION 2 & 3 (Tie) - Both are excellent
   - Version 2 is slightly simpler/more direct
   - Version 3 is more conventional/traditional
2. VERSION 1 - Should be avoided
   - Difficult to maintain
   - Easy to introduce bugs

RECOMMENDATION: Use Version 2 for simple linear logic, Version 3 for
complex conditional logic that naturally forms a decision tree.
""")