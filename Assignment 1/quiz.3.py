# Quiz game. Second version.
# Name: Nazca Taniguchi
# Date: Feb 24, 2026
# Make a list with the question and correct answers.
# Makw QUESTIONS a dictionary, to influde answer options and the correct choice. 

QUESTIONS = {
    "What is the airspeed of an unladen swallow? in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "San Antonio", "Dallas", "Houston"],
    "The Last Supper was painted by which artist?": [ "Da Vinci", "Van Gogh", "Picasso", "Raphael"],
}

for question, options in QUESTIONS.items():
    correct_answer = options[0]  # The first option is the correct answer
    for alternative in sorted(options):
        print(f" - {alternative}")
    
    answer = input(question + ": ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r} not {answer!r}")