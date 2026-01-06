from collections import Counter
# import string
# print(string.ascii_lowercase)
# or,
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# random.choice(alphabet)

output = Counter("book")
print(output)

# crabble bag approach:
SCRABBLE_BAG = (
    "eeeeeeeeeeee"
    "aaaaaaaaa"
    "iiiiiiiii"
    "oooooooo"
    "nnnnnn"
    "rrrrrr"
    "tttttt"
    "llll"
    "ssss"
    "uuuu"
    "dddd"
    "ggg"
    "bbccmmpp"
    "ffhhvvwwyy"
    "kjx"
    "qz"
)

def draw_letters():
    return "".join(random.choices(SCRABBLE_BAG, k=7))