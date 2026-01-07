# main.py
from db import init_db, get_or_create_user, save_score, get_top_scores
from game_logic import (
    create_letter_bag,
    draw_letters,
    uses_available_letters,
    calculate_score
)

# def load_dictionary(filename="words.txt"):
#     with open(filename) as f:
#         return {line.strip().lower() for line in f if line.strip().isalpha()}   
def load_dictionary(filename="words.txt"):
    words = set()

    try:
        with open(filename, "r") as file:
            for line in file:
                word = line.strip().lower()
              
                # ✅ FILTER HERE
                if 3 <= len(word) <= 5:
                    words.add(word)

    except FileNotFoundError:
        print(f"❌ Dictionary file '{filename}' not found.")
        exit()

    return words

def main():
    init_db()
    dictionary = load_dictionary()

    username = input("Enter your username: ").strip()
    user_id = get_or_create_user(username)

    bag = create_letter_bag()
    rack = draw_letters(bag)
    total_score = 0

    while True:
        print("\nYour rack:", rack)
        word = input("Enter a word (or press Enter to quit): ").lower()

        if not word:
            break

        if not uses_available_letters(word, rack):
            print("❌ Invalid letters.")
            continue

        if word not in dictionary:
            print("❌ Not a valid word.")
            continue

        score = calculate_score(word)
        total_score += score
        save_score(user_id, score)

        for c in word:
            rack.remove(c)
        rack.extend(draw_letters(bag, 7 - len(rack)))

        print(f"✅ +{score} points | Total: {total_score}")

    print("\n🏆 Top Scores:")
    for name, score, time in get_top_scores():
        print(f"{name}: {score} ({time})")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()


# 🔜 NEXT STEPS

# 1️⃣ Persist game state (rack & bag)
# 2️⃣ Add password-protected users
# 3️⃣ Convert to Flask web app
# 4️⃣ Package as desktop app
# 5️⃣ Add AI opponent








