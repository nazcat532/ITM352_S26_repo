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
    
    # Test case 8: ratio = 0.5 with hits = spins returns "Almost there!" (hits NOT < spins)
    assert progress_function(5, 5) == "Almost there!", "Test case 8 failed"
    
    print("All tests passed!")

# Run the test 