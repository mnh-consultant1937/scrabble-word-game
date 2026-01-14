import random
import requests

# ------------------ CONSTANTS ------------------

LETTER_SCORES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2,
    'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10,'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}

LETTER_POOL = (
    "eeeeeeeeeeee"
    "aaaaaaaaa"
    "iiiiiiiii"
    "oooooooo"
    "nnnnnn"
    "rrrrrr"
    "tttttt"
    "llll"
    "ssss"
    "dddd"
    "ggg"
    "bbccmmpp"
    "ffhhvvwwyy"
    "kjx"
    "qz"
)

NUMBER_OF_LETTERS = 7

# ------------------ LETTER GENERATION ------------------

# def draw_letters():
#     return random.sample(LETTER_POOL, NUMBER_OF_LETTERS)

def draw_letters():
  letters = []

  for count in range(NUMBER_OF_LETTERS):
    letter = random.choice(LETTER_POOL)
    letters.append(letter)
  
  return letters

# ------------------ ONLINE WORD VALIDATION ------------------

def is_valid_word_online(word):
    """
    Uses Datamuse API to validate words in real-time.
    """
    try:
        url = "https://api.datamuse.com/words"
        params = {
            "sp": word,
            "max": 1
        }
        response = requests.get(url, params=params, timeout=3)
        data = response.json()

        return len(data) > 0 and data[0]["word"] == word

    except requests.exceptions.RequestException:
        print("⚠️ Internet connection error.")
        return False

# ------------------ VALIDATION ------------------


def uses_available_letters(word, letters):
    letter_list = list(letters)

    for letter in word:
        if letter in letter_list:
           letter_list.remove(letter)
        else:
            return False

    return True

# ------------------ SCORING ------------------

def calculate_score(word):
    score = 0

    for letter in word:
        if letter in LETTER_SCORES:
            score += LETTER_SCORES[letter]

    return score

# ------------------ GAME PLAY ------------------

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
    return score, word

# ------------------ MAIN LOOP ------------------

def main():
    total_score = 0
    rounds = 0
    best_word = ""
    best_score = 0

    print("🎉 Welcome to Simple Scrabble (Online Edition) 🎉")

    while True:
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

main()





# Multiple save slots → you can save/load different boards.

# Persistent storage → board and generation survive program restart.

# Listing slots → see all saved games.

# Auto-save on exit → choose slot name.











  

