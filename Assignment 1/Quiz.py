# Multiple Choice Quiz Game
# Name: Nazca Taniguchi
# Date: March 4, 2026

# Quiz questions with options (correct answer is always first)
QUESTIONS = {
    "What is the airspeed of an unladen swallow? (in miles/hr)": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "San Antonio", "Dallas", "Houston"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Van Gogh", "Picasso", "Raphael"],
    "What is the largest planet in our solar system?": ["Jupiter", "Saturn", "Neptune", "Earth"],
    "Which programming language is known for web development?": ["Python", "Java", "C++", "Assembly"],
}

def run_quiz():
    """Run the multiple choice quiz and return score."""
    num_correct = 0
    total_questions = len(QUESTIONS)
    
    print("=" * 50)
    print("WELCOME TO THE MULTIPLE CHOICE QUIZ!")
    print("=" * 50)
    print()
    
    for question_num, (question, options) in enumerate(QUESTIONS.items(), start=1):
        print(f"Question {question_num} of {total_questions}:")
        print(question)
        print()
        
        correct_answer = options[0]  # First option is always correct
        sorted_options = sorted(options)  # Shuffle options alphabetically
        
        # Display options
        for label, option in enumerate(sorted_options, start=1):
            print(f"  {label}. {option}")
        print()
        
        # Get user answer
        while True:
            try:
                answer_choice = int(input("Enter your answer (1-4): "))
                if 1 <= answer_choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Check answer
        user_answer = sorted_options[answer_choice - 1]
        if user_answer == correct_answer:
            print("✓ Correct!\n")
            num_correct += 1
        else:
            print(f"✗ Incorrect. The correct answer is: {correct_answer}\n")
    
    # Display results
    print("=" * 50)
    print("QUIZ COMPLETE!")
    print("=" * 50)
    percentage = (num_correct / total_questions) * 100
    print(f"Your Score: {num_correct} out of {total_questions}")
    print(f"Percentage: {percentage:.1f}%")
    print("=" * 50)
    
    return num_correct, total_questions

if __name__ == "__main__":
    run_quiz()
