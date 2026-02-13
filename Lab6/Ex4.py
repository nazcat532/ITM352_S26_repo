# Leap Year Conditional Logic: (Condition A AND Condition B) OR Condition C

def is_leap_year(year):
    """
    Leap year rule: (year % 4 == 0 AND year % 100 != 0) OR (year % 400 == 0)
    Parentheses ensure correct evaluation order (AND evaluated before OR).
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("="*70)
print("LEAP YEAR LOGIC: (A AND B) OR C")
print("="*70)
print("Expression: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)")
print("Parentheses matter: ensures correct evaluation order\n")

# Test various years
test_years = [1900, 2000, 2004, 2006, 2100, 2400]
print(f"{'Year':<6} {'Leap?':<8} {'(% 4==0 & % 100!=0)':<20} {'% 400==0':<12} {'Result':<8}")
print("-" * 70)

for year in test_years:
    cond_ab = (year % 4 == 0 and year % 100 != 0)
    cond_c = year % 400 == 0
    result = is_leap_year(year)
    print(f"{year:<6} {str(result):<8} {str(cond_ab):<20} {str(cond_c):<12} ({cond_ab} or {cond_c})")

# Test with birth year (2006 is not a leap year)
birth_year = 2006
print(f"\nBirth year {birth_year}: {'Leap year ✓' if is_leap_year(birth_year) else 'Not leap year ✗'}")
print(f"Next leap year: {[y for y in range(birth_year, birth_year + 10) if is_leap_year(y)][0]}")

