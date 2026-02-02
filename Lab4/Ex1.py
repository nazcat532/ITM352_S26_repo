# String manipulation example

first = input("Enter the first name: ")
middleIn = input("Enter the middle initial: ")
last = input("Enter the last name: ")

full_name = first + " " + middleIn + ". " + last
print("Your full name is:", full_name)

print(f"Your full name is: {first} {middleIn}. {last}")

full_name = "%s %s. %s" % (first, middleIn, last)
print("Your full name is:", full_name)

txt = "Your full name is: {} {}. {}"
print(txt.format(first, middleIn, last))

full_name = " ".join([first, f"middleIn," + ".", last])
print("Your full name is:", full_name)

name_parts = [first, f"{middleIn}.", last]

full_name = "{} {} {}".format(*name_parts)
print("Your full name is:", full_name)