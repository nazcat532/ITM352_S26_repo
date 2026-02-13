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
    if spins == 0:
        return "Get going!"
    
    if hits == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    if hits_spins_ratio >= 0.5:
        if hits < spins:
            return "You win!"
    
    if hits_spins_ratio >= 0.25:
        return "Almost there!"
    
    if hits_spins_ratio > 0:
        return "On your way!"
    
    return "Get going!"


def test_determine_progress(progress_function):
    # Test case 1: spins = 0 returns "Get going!"
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed"
    
    # Test case 2: hits = 0 returns "Get going!"
    assert progress_function(0, 10) == "Get going!", "Test case 2 failed"
    
    # Test case 3: Low ratio (0 < ratio < 0.25) returns "On your way!"
    assert progress_function(2, 10) == "On your way!", "Test case 3 failed"
    
    # Test case 4: Medium ratio (0.25 <= ratio < 0.5) returns "Almost there!"
    assert progress_function(3, 10) == "Almost there!", "Test case 4 failed"
    
    # Test case 5: High ratio with hits < spins returns "You win!"
    assert progress_function(5, 9) == "You win!", "Test case 5 failed"
    
    # Test case 6: High ratio but hits >= spins returns "Almost there!"
    assert progress_function(10, 10) == "Almost there!", "Test case 6 failed"
    
    print("All tests passed!")


"""
ADVANTAGES OF USING ASSERT-BASED TESTING OVER PRINT STATEMENTS:

1. AUTOMATED VERIFICATION: With assert statements, the test automatically fails if a 
   condition is not met. With print statements, you have to manually inspect the output 
   to verify correctness—easy to miss errors.

2. REUSABILITY: The test function takes the progress_function as a parameter, so you can 
   test different versions (original, revised, etc.) without modifying the test code. 
   With print statements, you'd need to rewrite/duplicate testing code for each version.

3. CLEAR PASS/FAIL STATUS: When you call test_determine_progress(determine_progress1), 
   it either passes silently with "All tests passed!" or fails loudly with an error 
   message. With print statements, you must manually review multiple print outputs to 
   determine if the function is working correctly.

4. SCALABILITY: You can easily add or remove test cases without cluttering your main code 
   with print statements. The test results are concise and focused.

5. MAINTAINABILITY: When you revise the function, you just call the same test function 
   on the new version. There's no need to change your testing approach—the test is 
   independent of the implementation details.

Example of old approach (print-based testing):
    result1 = determine_progress1(10, 0)
    print(f"Test 1: {result1}")  # You must visually inspect this
    if result1 != "Get going!":
        print("Test 1 FAILED")  # Manual error detection
    
Example of new approach (assert-based testing):
    test_determine_progress(determine_progress1)  # Automatic verification, clean output
"""


# Run the tests
test_determine_progress(determine_progress1)
test_determine_progress(determine_progress2)