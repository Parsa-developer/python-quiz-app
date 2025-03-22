import json
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def load_questions(filename):
    """Load questions from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(Fore.RED + f"Error loading questions: {str(e)}")
        exit()

def run_quiz(questions):
    """Main quiz logic with timing"""
    score = 0
    total_questions = len(questions)
    
    print(Fore.CYAN + Style.BRIGHT + "\n=== PYTHON QUIZ ===")
    print(Fore.YELLOW + f"Total questions: {total_questions}\n")

    for idx, q in enumerate(questions, 1):
        print(Fore.BLUE + Style.BRIGHT + f"\nQuestion {idx}/{total_questions}")
        print(Fore.WHITE + q["question"])
        
        # Display options
        for i, option in enumerate(q["options"]):
            print(f"{Fore.MAGENTA}{chr(65 + i)}. {option}")
            
        # Get answer with timing
        start_time = time.time()
        user_answer = input(Fore.CYAN + 
            f"\nYou have {q['time_limit']} seconds. Enter answer (A/B/C/D): ").upper()
        elapsed = time.time() - start_time

        # Validate answer
        valid_choices = [chr(65 + i) for i in range(len(q["options"]))]
        
        if elapsed > q["time_limit"]:
            print(Fore.RED + "Time's up! ⏰")
        elif user_answer not in valid_choices:
            print(Fore.RED + "Invalid choice! ❌")
        elif user_answer == q["answer"]:
            print(Fore.GREEN + "Correct! ✅")
            score += 1
        else:
            print(Fore.RED + "Wrong! ❌")
            print(Fore.GREEN + f"Correct answer: {q['answer']}")

    # Show final results
    print(Fore.CYAN + Style.BRIGHT + "\n=== RESULTS ===")
    print(f"{Fore.YELLOW}Correct answers: {score}/{total_questions}")
    print(f"{Fore.BLUE}Percentage: {(score/total_questions)*100:.1f}%")

if __name__ == "__main__":
    questions = load_questions("questions.json")
    run_quiz(questions)