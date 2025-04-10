import os

# Create folder for quizzes and category of quizzes
category = input("Enter quiz category (e.g. math, science, anime): ")
folder_path = f"Quizzes/{category}"
os.makedirs(folder_path, exist_ok=True)

filename = input("Enter quiz filename (without .txt): ") + ".txt"
folder_path = os.path.join(folder_path, filename)

# Use while loop for the number of question
while True:
    try:
        num_question = int(input("How many question would you like to input?: "))
        if num_question > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Making the quiz
question_count = 1
while question_count <= num_question:
    question = input("Enter your question.")

choices = {}
for option in ['a', 'b', 'c', 'd']:
    choices[option] = input(f"Choice {option}")

answer = input("Enter correct answer (a/b/c/d): ")

# Use dictionary to store the quiestion data
question_data ={
    "question" : question,
    "choices" : choices,
    " answer" : answer,
}