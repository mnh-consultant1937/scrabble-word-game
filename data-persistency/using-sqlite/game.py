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















  

