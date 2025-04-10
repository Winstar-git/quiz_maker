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
 ██████╗ ██╗   ██╗██╗███████╗     ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║██║   ██║██║  ███╔╝     ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝
██║▄▄ ██║██║   ██║██║ ███╔╝      ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝╚██████╔╝██║███████╗    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
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
loading("Booting up Quiz Creator...")
typewriter("🧠 Ready to build your quiz...\n")

# Create folder for quizzes and category of quizzes
category = input(Fore.CYAN + "📁 Enter quiz category (e.g. math, science, anime): " + Style.RESET_ALL)
folder_path = f"Quizzes/{category}"
os.makedirs(folder_path, exist_ok=True)

filename = input(Fore.CYAN + "📝 Enter quiz filename (without .txt): " + Style.RESET_ALL) + ".txt"
file_path = os.path.join(folder_path, filename)

# Use while loop for the number of question
while True:
    try:
        num_question = int(input(Fore.CYAN + "🔢 How many question would you like to input?: " + Style.RESET_ALL))
        if num_question > 0:
            break
        else:
            print(Fore.RED + "❌ Please enter a number greater than 0." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "❌ Invalid input. Please enter a valid number." + Style.RESET_ALL)

# Making the quiz
question_count = 1
while question_count <= num_question:
    console.print(f"\n[bold yellow]📌 Question #{question_count}[/bold yellow]")
    question = input(Fore.YELLOW + "❓Enter your question: " + Style.RESET_ALL)

    choices = {}
    for option in ['a', 'b', 'c', 'd']:
        choices[option] = input(Fore.BLUE + f"👉 Choice {option}: " + Style.RESET_ALL)

    answer = input(Fore.BLUE + "✔ Enter correct answer (a/b/c/d): " + Style.RESET_ALL).lower()
    while answer not in ['a', 'b', 'c', 'd']:
        print(Fore.RED + "❌ Invalid input. Please enter a, b, c, or d only." + Style.RESET_ALL)
        answer = input(Fore.GREEN + "✔ Enter correct answer (a/b/c/d): " + Style.RESET_ALL).lower()

# Print to check the question data if correct
    console.print("\n[bold green]📄 Preview:[/bold green]")
    print(Fore.MAGENTA + f"{question}")
    for option in ['a', 'b', 'c', 'd']:
        print(Fore.CYAN + f"{option}) {choices[option]}")
    print(Fore.GREEN + f"✔ Correct Answer: {answer.upper()}")

    # Use dictionary to store the quiestion data
    question_data ={
        "question" : question,
        "choices" : choices,
        " answer" : answer,
    }
# Saving the question data 
    save = input(Fore.YELLOW + "\n💾 Save this question? (y/n): " + Style.RESET_ALL).lower()
    if save == 'y':
        try:
            with open(file_path, 'a', encoding="utf-8") as text:
                text.write(f"Question: {question_data['question']}\n")
                for option, choice in question_data["choices"].items():
                    text.write(f"{option}) {choice}\n")
                text.write(f"Answer: {question_data[' answer'].upper()}\n")
                text.write("################\n\n")
            print(Fore.GREEN + "✅ Question saved!\n")
        except Exception as e:
            print(Fore.RED + f"❌ Error saving question: {e}")
        question_count += 1
    else:
        print(Fore.YELLOW + "⏩ Skipped saving the question.")

# Ask if the user wants to continue or stop
    if question_count > num_question:
        console.print("\n[bold cyan]✅ All questions inputted! Quiz creation complete![/bold cyan]")
        break
    another_one = input(Fore.CYAN + "\n➕ Add another question? (y/n): " + Style.RESET_ALL).lower()
    if another_one != 'y':
        console.print("\n[bold cyan]✅ Quiz creation complete! Goodbye, Quiz Master![/bold cyan]")
        break