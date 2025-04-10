import os

# Create folder for quizzes and category of quizzes
category = input("Enter quiz category (e.g. math, science, anime): ")
folder_path = f"Quizzes/{category}"
os.makedirs(folder_path, exist_ok=True)

filename = input("Enter quiz filename (without .txt): ") + ".txt"
file_path = os.path.join(folder_path, filename)

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
    question = input("Enter your question: ")

    choices = {}
    for option in ['a', 'b', 'c', 'd']:
        choices[option] = input(f"Choice {option}: ")

    answer = input("Enter correct answer (a/b/c/d): ")

# Print to check the question data if correct
    print(f"{question}")
    for option in ['a', 'b', 'c', 'd']:
        print(f"{option}) {choices[option]}")
    print(f"Correct Answer: {answer.upper()}")

# Saving the question data 
    save = input("Save this question? (y/n): ").lower()
    if save == 'y':
        try:
            with open(file_path, 'a', encoding="utf-8") as text:
                text.write(f"Question: {question}")
                for option in ['a', 'b', 'c', 'd']:
                    text.write(f"{option}) {choices[option]}")
                text.write(f"Answer: {answer}")
            print("Question saved!")
        except Exception as e:
            print(f"Error saving question: {e}")
    else:
        print("Skipped saving the question.")
# Use dictionary to store the quiestion data
question_data ={
    "question" : question,
    "choices" : choices,
    " answer" : answer,
}