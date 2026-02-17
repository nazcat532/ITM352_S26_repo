def is_leap_year(year):
    # (Condition A AND Condition B) OR Condition C
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


# --- Test cases ---
birth_year = 2003          # replace with your actual birth year if different
closest_leap_year = 2004   # closest leap year to 2003

print(f"{birth_year} is a leap year: {is_leap_year(birth_year)}")
print(f"{closest_leap_year} is a leap year: {is_leap_year(closest_leap_year)}")