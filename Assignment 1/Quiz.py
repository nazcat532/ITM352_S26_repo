# Build a quiz app
# Name: Nazca Taniguchi
# Date: March 5, 2026

questions = {
    "What is the color of the sky": ["red", "green", "blue", "yellow"],
    "What is the city of Oahu": ["Honolulu", "Ala Moana", "Kailua", "Kahala"],
    "Barak Obama was elected in which year?": ["2012", "2008", "2016", "2020"],
    "Which continent is the largest?": ["Asia", "Africa", "North America", "South America"],
    "Which country is known for the Eiffel Tower?": ["Spain", "Germany", "Italy", "France"]
}

answers = {
     "What is the color of the sky": "c",
     "What is the city of Oahu": "a",
    "Barak Obama was elected in which year?": "b",
    "Which continent is the largest?": "a",
    "Which country is known for the Eiffel Tower?": "d"
}

score = 0

for question, options in questions.items():
    print("/n" + question)
    
    print("a. " + options[0])
    print("b. " + options[1])
    print("c. " + options[2])
    print("d. " + options[3])

user_answer = input("Enter your answer (a, b, c, or d): ").lower()

while user_answer not in ['a', 'b', 'c', 'd']:
    print("Invalid input. Please enter a, b, c, or d.")
    user_answer = input("Enter your answer (a, b, c, or d): ").lower()