# Build a quiz app
# Name: Nazca Taniguchi
# Date: March 5, 2026

import random

# Quiz questions and options
questions = {
    "What is the color of the sky": ["red", "green", "blue", "yellow"],
    "What is the city of Oahu": ["Honolulu", "Ala Moana", "Kailua", "Kahala"],
    "Barak Obama was elected in which year?": ["2012", "2008", "2016", "2020"],
    "Which continent is the largest?": ["Asia", "Africa", "North America", "South America"],
    "Which country is known for the Eiffel Tower?": ["Spain", "Germany", "Italy", "France"]
}

# Corrent answers (can have multiple correct answers)
answers = {
     "What is the color of the sky": "c",
     "What is the city of Oahu": "a",
    "Barak Obama was elected in which year?": "b",
    "Which continent is the largest?": "a",
    "Which country is known for the Eiffel Tower?": "d"
}

score = 0
fifty_fifty_used = False

def use_fifty_fifty(options, correct_indices):
    """
    Eliminate two incorrect options randomly.
    Returns a new list of options with only 2 remaining (1 correct and 1 incorrect).
    """
    indices = [0, 1, 2, 3]
    # Remove the correct answer index from the list of indices
    for i in correct_indices:
        indices.remove(i)
    # Randomly select two incorrect options to eliminate
    to_remove = random.sample(indices, 2)
    new_options = []
    for idx, opt in enumerate(options):
        if idx not in to_remove:
            new_options.append(opt)
        else:
            new_options.append("----")  # Placeholder for eliminated options
    return new_options

#Main quiz loop
for question, options in questions.items():
    print("\n" + question)
    
    #options
    options_labels = ['a', 'b', 'c', 'd']
    for label, option in zip(options_labels, options):
        print(f"{label}. {option}")
    
    #50/50
    if not fifty_fifty_used:
        use_fifty_fifty_input = input("Would you like to use 50/50? (y/n): ").lower()
        if use_fifty_fifty_input == 'y':
            # Convert letter answer to index (a=0, b=1, c=2, d=3)
            correct_index = ord(answers[question]) - ord('a')
            options = use_fifty_fifty(options, [correct_index])
            fifty_fifty_used = True
            print("\nOptions after using 50/50:")
            for label, option in zip(options_labels, options):
                print(f"{label}. {option}")

    # Get user answer
    user_answer = input("Enter your answer (a, b, c, or d): ").lower()
    while user_answer not in ['a', 'b', 'c', 'd']:
        print("Invalid input. Please enter a, b, c, or d.")
        user_answer = input("Enter your answer (a, b, c, or d): ").lower()

    #check multiple correct answers
    if user_answer == answers[question]:
        print("Correct!")
        score += 1
    else:
        correct_str =  ", ". join(answers[question])
        print(f"Incorrect. The correct answer is {correct_str}.")

print(f"\nQuiz completed! Your final score is: {score}/{len(questions)}")    

