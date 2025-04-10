import os

# Create folder for quizzes and category of quizzes
category = input("Enter quiz category (e.g. math, science, anime): ")
folder_path = f"Quizzes/{category}"
os.makedirs(folder_path, exist_ok=True)

filename = input("Enter quiz filename (without .txt): ") + ".txt"
folder_path = os.path.join(folder_path, filename)

