import random
# import string

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

LETTER_DISTRIBUTION = {
    'a': 9, 'b': 2, 'c': 2, 'd': 4,
    'e': 12,'f': 2, 'g': 3, 'h': 2,
    'i': 9, 'j': 1, 'k': 1, 'l': 4,
    'm': 2, 'n': 6, 'o': 8, 'p': 2,
    'q': 1, 'r': 6, 's': 4, 't': 6,
    'u': 4, 'v': 2, 'w': 2, 'x': 1,
    'y': 2, 'z': 1
}

def create_letter_bag():
    bag = []
    for letter, count in LETTER_DISTRIBUTION.items():
        bag.extend([letter] * count)
    random.shuffle(bag)
    return bag

def draw_letters_from_bag(bag, n=7):
    drawn = []
    for _ in range(n):
        if bag:
            drawn.append(bag.pop())
    return drawn

# Generating Random Letters
def draw_letters():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letters = []
  number_of_letters = 7

  for count in range(number_of_letters):
    letter = random.choice(alphabet)
    letters.append(letter)
    # letters = random.choices(string.ascii_lowercase, k=7)
  
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
                if word.isalpha():   # keep only clean words
                    words.add(word)
    except FileNotFoundError:
        print("❌ Dictionary file not found!")
        return set()

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


# Playing One Round
def play_round():
    letters = draw_letters()
    print("\nYour letters:", letters)

    word = input("Enter a word (or press Enter to skip): ").lower()

    if not word:
        print("Skipped.")
        return 0

    if not uses_available_letters(word, letters):
        print("❌ You used letters not in the generated letters.")
        return 0

    if not is_valid_word(word):
        print("❌ Not a valid word.")
        return 0

    score = calculate_score(word)
    print(f"✅ Valid word! Score: {score}")
    return score


def main():
    bag = create_letter_bag()
    dictionary = load_dictionary("words.txt")

    if not dictionary:
        return

    total_score = 0

    while True:
        rack = draw_letters_from_bag(bag)
        if not rack:
            print("No more letters left. Game over!")
            break

        print("\nYour letters:", rack)
        word = input("Enter a word (or press Enter to skip): ").lower()

        if not word:
            print("Skipped.")
        elif not uses_available_letters(word, rack):
            print("❌ Invalid letters.")
        elif word not in dictionary:
            print("❌ Not a valid word.")
        else:
            score = calculate_score(word)
            total_score += score
            print(f"✅ Word accepted! Score: {score}")

        print("Total score:", total_score)

        if input("Play again? (y/n): ").lower() != 'y':
            break

    print("Final score:", total_score)



main()



# enhance the game
# 🔜 Next Enhancement Options (Choose One)
# Option 2️⃣ – Load a Real Dictionary File

# ➡️ Teaches file I/O and memory efficiency

# Option 3️⃣ – Refill Rack After Each Word

# ➡️ Teaches state updates & list manipulation

# Option 4️⃣ – Computer Opponent

# ➡️ Teaches algorithms & AI thinking

# Option 5️⃣ – Bonus Tiles (Double Word, Triple Letter)

# ➡️ Teaches board modeling & 2D data structures












