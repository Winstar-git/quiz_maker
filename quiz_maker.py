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