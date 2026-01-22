# gui.py
import tkinter as tk
from tkinter import messagebox

from game import (
    draw_letters,
    is_valid_word_online,
    uses_available_letters,
    calculate_score
)
from db import init_db, save_round, get_game_stats


class ScrabbleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Scrabble")
        self.root.geometry("420x320")
        self.root.resizable(False, False)

        init_db()

        self.letters = []
        self.total_score = 0

        self.create_widgets()
        self.new_round()

    # ------------------ UI ------------------

    def create_widgets(self):
        tk.Label(
            self.root,
            text="🎉 Simple Scrabble 🎉",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.letters_label = tk.Label(
            self.root,
            text="Letters:",
            font=("Arial", 12)
        )
        self.letters_label.pack(pady=5)

        self.word_entry = tk.Entry(self.root, font=("Arial", 12))
        self.word_entry.pack(pady=5)

        tk.Button(
            self.root,
            text="Submit Word",
            command=self.submit_word
        ).pack(pady=5)

        self.message_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11)
        )
        self.message_label.pack(pady=5)

        self.score_label = tk.Label(
            self.root,
            text="Total Score: 0",
            font=("Arial", 12, "bold")
        )
        self.score_label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="New Round", command=self.new_round).pack(side="left", padx=10)
        tk.Button(frame, text="Quit", command=self.root.quit).pack(side="left")

    # ------------------ GAME LOGIC ------------------

    def new_round(self):
        self.letters = draw_letters()
        self.letters_label.config(
            text="Letters: " + " ".join(self.letters).upper()
        )
        self.word_entry.delete(0, tk.END)
        self.message_label.config(text="")

    def submit_word(self):
        word = self.word_entry.get().lower().strip()

        if not word:
            self.message_label.config(text="⏭️ Round skipped.")
            return

        if not uses_available_letters(word, self.letters):
            self.message_label.config(text="❌ Letters not available.")
            return

        if not is_valid_word_online(word):
            self.message_label.config(text="❌ Not a valid English word.")
            return

        score = calculate_score(word)
        self.total_score += score
        save_round(word, score)

        self.message_label.config(
            text=f"✅ '{word}' accepted! Score: {score}"
        )
        self.score_label.config(
            text=f"Total Score: {self.total_score}"
        )


# ------------------ RUN APP ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrabbleApp(root)
    root.mainloop()
