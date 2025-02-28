# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score

import random
# list of questions and store the answers
questions = {
    "What is the keyword to define a function in python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for python files?": ".py",
    "Which symbol is used to comment in python?":"#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in python?":"for",
    "What is the output of 2 ** 3 in python?":"8",
    "What keyword is used to import a module in python?":"import",
    "What does the len() function return?":"length",
    "What is the result of 10 // 3 in python?":"3"
}

def trivia_game():
    # Randomly pick question
    questions_list = list(questions.keys())
    total_question = 5
    score = 0

    selected_questions = random.sample(questions_list, total_question)
    
    # Format the question
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        # user answer
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]
        
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong. The Correct answer is:{correct_answer}.\n")

    print(f"Game Over! Your Final Score is : {score}/{total_question}" )
       
trivia_game()