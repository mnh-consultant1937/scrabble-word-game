from game import draw_letters, is_valid_word_online, uses_available_letters, calculate_score     
from db import init_db, save_round



def print_divider():
    print("-" * 30)

def play_round():
    print_divider()
    letters = draw_letters()
    print("Your letters:", " ".join(letters))

    word = input("Enter a word (or press Enter to skip): ").lower().strip()

    if not word:
        print("⏭️ Round skipped.")
        return 0, ""

    if not uses_available_letters(word, letters):
        print("❌ You used letters not in the rack.")
        return 0, ""

    if not is_valid_word_online(word):
        print("❌ Not a valid English word.")
        return 0, ""

    score = calculate_score(word)
    print(f"✅ '{word}' is valid! Score: {score}")
    save_round(word, score)
    return score, word

# ------------------ MAIN LOOP ------------------

def main():
    init_db()
    total_score = 0
    rounds = 0
    best_word = ""
    best_score = 0

    print("🎉 Welcome to Simple Scrabble (Online Edition) 🎉")

    while True:
        print_divider()
        score, word = play_round()
        rounds += 1
        total_score += score

        if score > best_score:
            best_score = score
            best_word = word

        print("Total score:", total_score)

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

    print_divider()
    print("Game Over!")
    print("Rounds played:", rounds)
    print("Total score:", total_score)
    print("Best word:", best_word, f"({best_score} points)")
    print("Thanks for playing! 🎉")

# ------------------ RUN ------------------

if __name__ == "__main__":
    main()




# requirements.txt file:
# Step 1: Make sure your virtual environment is active
# Step 2: Generate the file
# pip freeze > requirements.txt
# This includes everything installed, even unused packages.

# Now requirements.txt is a file that lists all Python packages the project needs, so anyone (or any server) can run:
# pip install -r requirements.txt




