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

num_correct = 0
for question, options in QUESTIONS.items():
    correct_answer = options[0]  # The first option is the correct answer
    sorted_options = sorted(options)  
    for label, alternative in enumerate(sorted_options, start=1):
        print(f" {label}. {alternative}")
    
    answer_label = int(input(question + ": "))
    answer = sorted_options[answer_label - 1]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r} not {answer!r}")