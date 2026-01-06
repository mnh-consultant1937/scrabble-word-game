import random
# import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

LETTER_SCORES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2,
    'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10,'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}

# print(LETTER_SCORES['z'])

# Generating Random Letters
# def draw_letters():
#   # alphabet = "abcdefghijklmnopqrstuvwxyz"
#   letters = []
#   number_of_letters = 7

#   for count in range(number_of_letters):
#     letter = random.choice(alphabet)
#     letters.append(letter)
#     # letters = random.choices(string.ascii_lowercase, k=7)
  
#   return letters

def draw_letters():
    letters = []
    number_of_letters = 7

    # Step 1: Add at least 3 vowels
    for count in range(3):
        letter = random.choice(VOWELS)
        letters.append(letter)

    # Step 2: Add the remaining consonants
    for count in range(number_of_letters - 3):
        letter = random.choice(CONSONANTS)
        letters.append(letter)

    # Step 3: Shuffle letters so vowels aren't grouped
    random.shuffle(letters)

    return letters

# print(draw_letters())

# Checking If Word Uses Given Letters
def uses_available_letters(word, letters):
    letter_list = list(letters)

    for letter in word:
        if letter in letter_list:
           letter_list.remove(letter)
        else:
            return False

    return True

# Testing:
# word = "book"
# letters = "boko"
# print(uses_available_letters(word, letters))


# Load a Small Word List (Later, you can load thousands of words from a file)

def load_dictionary(filename):
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


# VALID_WORDS = {
#     "cat", "dog", "hat", "rat", "bat",
#     "tree", "read", "dear", "tea", "till"
# }
VALID_WORDS = load_dictionary("words.txt")

def is_valid_word(word):
    return word in VALID_WORDS


# Calculating Word Score
def calculate_score(word):
    score = 0

    for letter in word:
        if letter in LETTER_SCORES:
            score += LETTER_SCORES[letter]

    return score


def print_divider():
    print("-" * 30)

# Playing One Round
def play_round():
    print_divider()
    letters = draw_letters()
    # print("\nYour letters:", letters)
    print("Your letters:", " ".join(letters))
    word = input("Enter a word (or press Enter to skip): ").lower().strip()

    if not word:
        print("⏭️ Round skipped.")
        return 0

    if not uses_available_letters(word, letters):
        print("❌ You used letters not in the generated letters.")
        return 0

    if not is_valid_word(word):
        print("❌ Not a valid word.")
        return 0

    score = calculate_score(word)
    print(f"✅ {word}' is valid! Score: {score}")
    return score


def main():
    total_score = 0
    rounds = 0
    best_word = ""
    best_score = 0

    print("🎉 Welcome to Simple Scrabble 🎉")
  
    while True:
        score = play_round()
        rounds += 1
        total_score += score
        
        if score > best_score:
            best_score = score
            best_word = score
      
        print("Total score:", total_score)
        # print(f"Total score: {total_score}")

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! 🎉")
            break

    print_divider()
    print("Game Over!")
    print("Rounds played:", rounds)
    print("Total score:", total_score)
    print("Thanks for playing! 🎉")


main()



# enhance the game













