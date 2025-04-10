import os
import time
import sys
from rich.console import Console
from rich.panel import Panel
from colorama import Fore, Style, init

init(autoreset=True)
console = Console()

# ASCII art for walcome screen
ascii_art = """
  ██████╗ ██╗   ██╗██╗███████╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
 ██╔═══██╗██║   ██║██║╚══███╔╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
 ██║   ██║██║   ██║██║  ███╔╝     ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
 ██║▄▄ ██║██║   ██║██║ ███╔╝      ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
 ╚██████╔╝╚██████╔╝██║███████╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
  ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
# Typewiter effect
def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Loading effect
def loading(message="Loading...", delay=2.5):
    with console.status(f"[bold green]{message}"):
        time.sleep(delay)

# Welcome Screen 
console.print(Panel.fit(ascii_art, border_style="bright_yellow"))
loading("Booting up Quiz Maker...")
typewriter(" Ready to build your quiz...\n")

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

    # Use dictionary to store the quiestion data
    question_data ={
        "question" : question,
        "choices" : choices,
        " answer" : answer,
    }
# Saving the question data 
    save = input("Save this question? (y/n): ").lower()
    if save == 'y':
        try:
            with open(file_path, 'a', encoding="utf-8") as text:
                text.write(f"Question: {question_data['question']}")
                for option, choice in question_data["choices"].items():
                    text.write(f"{option}) {choice}")
                text.write(f"Answer: {question_data[' answer'].upper()}")
            print("Question saved!")
        except Exception as e:
            print(f"Error saving question: {e}")
        question_count += 1
    else:
        print("Skipped saving the question.")

# Ask if the user wants to continue or stop
    if question_count > num_question:
        print("All questions inputted! Quiz creation complete!")
        break
    another_one = input("Add another question? (y/n): ").lower()
    if another_one != 'y':
        print("Quiz creation complete! Goodbye!!")
        break