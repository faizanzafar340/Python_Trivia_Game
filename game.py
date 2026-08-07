import random

questions = {
    "what is the keyword to define a function in python?": "def",
    "Which data type in python use to store True or False valuess?": "boolean",
    "Which symbol is used to comment in python? " : "#",
    "What is the correct file extension for python files?" : ".py",
    "How do you start for loop in python" : "for",
    "How does the len() function return" : "Length",
    "what funtion is used to get the user input in python" : "input"
    }

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0
    
    selected_questions = random.sample(questions_list, total_questions)
    while True: 
        for idx, question in enumerate(selected_questions):
            print(f"{idx + 1}. {question} ")
            user_answer = input("Your answer: ").lower().strip()
            correct_answer = questions[question]
            
            if user_answer == correct_answer.lower():
                print("Correct!\n ")
                score += 1
            else:
                print(f"Wrong. Correct answer is {correct_answer}.\n")
                    
        print(f"Your score is {score}/{total_questions}")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()

        if play_again == "no":
            print("Thanks for playing!")
            break
        
        elif play_again != "yes":
            print("Invalid input. Game ending.")
            break
         
python_trivia_game() 