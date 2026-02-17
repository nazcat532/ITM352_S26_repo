def isLeapYear(year):
    """
    Determine if a year is a leap year using if-statements.
    
    Returns: "Leap year" or "Not a leap year"
    
    Leap year rules:
    1. If divisible by 400 → Leap year
    2. If divisible by 100 (but not 400) → Not a leap year
    3. If divisible by 4 (but not 100) → Leap year
    4. Otherwise → Not a leap year
    """
    if year % 400 == 0:
        return "Leap year"
    if year % 100 == 0:
        return "Not a leap year"
    if year % 4 == 0:
        return "Leap year"
    return "Not a leap year"


def test_leap_years():
    """
    Test the isLeapYear() function with various test cases.
    """
    test_cases = [
        # (year, expected_result, description)
        (1996, "Leap year", "Regular leap year (divisible by 4, not 100)"),
        (2004, "Leap year", "Regular leap year (divisible by 4, not 100)"),
        (2024, "Leap year", "Regular leap year (divisible by 4, not 100)"),
        (1900, "Not a leap year", "Century year not divisible by 400"),
        (2000, "Leap year", "Century year divisible by 400"),
        (2100, "Not a leap year", "Century year not divisible by 400"),
        (1997, "Not a leap year", "Not divisible by 4"),
        (2001, "Not a leap year", "Not divisible by 4"),
        (2025, "Not a leap year", "Not divisible by 4"),
        (2006, "Not a leap year", "Birth year example (not leap)"),
        (2008, "Leap year", "Closest leap year to 2006"),
    ]
    
    print("=" * 80)
    print("LEAP YEAR FUNCTION TEST USING IF-STATEMENTS")
    print("=" * 80)
    print("\nFunction: isLeapYear(year)")
    print("Returns: 'Leap year' or 'Not a leap year'")
    print("\nLogic flow (if-statements):")
    print("1. If year % 400 == 0 → Leap year")
    print("2. If year % 100 == 0 → Not a leap year")
    print("3. If year % 4 == 0 → Leap year")
    print("4. Otherwise → Not a leap year")
    print("\n" + "-" * 80)
    
    all_passed = True
    for year, expected, description in test_cases:
        result = isLeapYear(year)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result != expected:
            all_passed = False
        print(f"{status} | Year {year}: {result:20} | {description}")
    
    print("-" * 80)
    
    # Test with birth year
    print("\nBIRTH YEAR EXAMPLE (2006):")
    print("-" * 80)
    birth_year = 2006
    birth_result = isLeapYear(birth_year)
    print(f"Year {birth_year}: {birth_result}")
    
    if birth_result == "Leap year":
        non_leap_year = birth_year + 1
        non_leap_result = isLeapYear(non_leap_year)
        print(f"Non-leap year test {non_leap_year}: {non_leap_result}")
    else:
        # Find nearest leap year
        leap_year = 2008  # Next leap year after 2006
        leap_result = isLeapYear(leap_year)
        print(f"Nearest leap year {leap_year}: {leap_result}")
    
    print("-" * 80)
    
    if all_passed:
        print("\n✓ All tests passed! The if-statement logic is working correctly.")
    else:
        print("\n✗ Some tests failed. Review the logic.")
    
    return all_passed


# Run the tests
if __name__ == "__main__":
    test_leap_years()