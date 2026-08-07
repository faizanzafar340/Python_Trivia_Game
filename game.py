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
    print(selected_questions)

python_trivia_game()