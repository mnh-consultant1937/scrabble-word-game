# game_logic.py
import random
from collections import Counter

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

LETTER_SCORES = {
    'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,
    'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,
    'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,
    'y':4,'z':10
}

LETTER_DISTRIBUTION = {
    'a':9,'b':2,'c':2,'d':4,'e':12,'f':2,'g':3,'h':2,
    'i':9,'j':1,'k':1,'l':4,'m':2,'n':6,'o':8,'p':2,
    'q':1,'r':6,'s':4,'t':6,'u':4,'v':2,'w':2,'x':1,
    'y':2,'z':1
}

def create_letter_bag():
    bag = []
    for letter, count in LETTER_DISTRIBUTION.items():
        bag.extend([letter] * count)
    random.shuffle(bag)
    return bag

# def draw_letters(bag, n=7):
#     return [bag.pop() for _ in range(min(n, len(bag)))   ]
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

# def uses_available_letters(word, rack):
#     return not (Counter(word) - Counter(rack))
def uses_available_letters(word, letters):
    letter_list = list(letters)

    for letter in word:
        if letter in letter_list:
           letter_list.remove(letter)
        else:
            return False

    return True

# def calculate_score(word):
#     return sum(LETTER_SCORES[c] for c in word)
def calculate_score(word):
    score = 0

    for letter in word:
        if letter in LETTER_SCORES:
            score += LETTER_SCORES[letter]

    return score
