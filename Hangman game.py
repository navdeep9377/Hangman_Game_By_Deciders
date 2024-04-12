import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    HANGMAN_PICS = ['''
     +---+
     O   |
    /|\  |
    / \  |
        ===     ''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===        ''', '''
    +---+
    O   |
   /|\  |
        |
       ===        ''', '''
    +---+
    O   |
   /|   |
        |
       ===     ''', '''
    +---+
    O   |
    |   |
        |
       ===       ''', '''
    +---+
    O   |
        |
        |
       ===      ''', '''
    +---+
        |
        |
        |
       ===          ''']

    def __init__(self, master):
        self.master = master
        self.master.title("Hangman")
        
        self.word_list = ["incorrectly", "staircase", "age", "bed", "ton", "river", "comb", "fire", "breath", "hole", "nine",
             "needle", "envelope", "clock", "silence", "palm", "cold", "coin"]
        
        self.hint_list = {
            "incorrectly": "This adverb describes an action performed wrongly.",
            "staircase": "It's a series of steps arranged in a sequence to reach different levels of a building.",
            "age": "It refers to the length of time that a person or thing has existed.",
            "bed": "It's a piece of furniture for sleeping or resting.",
            "ton": "It's a unit of weight equal to 2,000 pounds.",
            "river": "It's a natural flowing watercourse, usually freshwater, flowing towards an ocean, sea, lake or another river.",
            "comb": "It's a strip with a row of narrow teeth that are used to untangle or arrange hair.",
            "fire": "It's the rapid oxidation of a material in the exothermic chemical process of combustion.",
            "breath": "It's the process of taking air into the lungs and expelling it, especially as a physiological process.",
            "hole": "It's an opening or hollow place in or through a solid body or surface.",
            "nine": "It's the number that comes after eight and before ten.",
            "needle": "It's a slender, pointed device used for sewing or surgical suturing.",
            "envelope": "It's a flat, usually rectangular-shaped paper container for a letter.",
            "clock": "It's an instrument for measuring and displaying time.",
            "silence": "It's the absence of sound.",
            "palm": "It's the inner surface of the hand between the wrist and fingers.",
            "cold": "It's the absence of heat or warmth.",
            "coin": "It's a flat, usually round piece of metal or other material used as money."
        }
        
        self.chosen_word = random.choice(self.word_list)
        self.guessed_letters = set()
        self.lives = 6
        self.hint_used = False
        
        self.display = tk.StringVar()
        self.display.set(self.get_display())
        
        self.word_label = tk.Label(self.master, textvariable=self.display, font=("Courier", 24))
        self.word_label.grid(row=0, column=0, columnspan=2)
        
        self.guess_label = tk.Label(self.master, text="Guess a letter:", font=("Courier", 18))
        self.guess_label.grid(row=1, column=0, sticky=tk.E)
        
        self.guess_entry = tk.Entry(self.master, font=("Courier", 18))
        self.guess_entry.grid(row=1, column=1)
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.guess_letter)
        self.guess_button.grid(row=2, column=0, columnspan=2)
        
        self.hint_button = tk.Button(self.master, text="Hint", command=self.show_hint)
        self.hint_button.grid(row=3, column=0, columnspan=2)
        
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.grid(row=4, column=0, columnspan=2)
        
        self.draw_hangman()

        # Virtual keyboard
        self.keyboard_frame = tk.Frame(self.master)
        self.keyboard_frame.grid(row=5, column=0, columnspan=2)
        self.create_keyboard()

    def get_display(self):
        return ''.join(letter if letter in self.guessed_letters else '_ ' for letter in self.chosen_word)
    
    def draw_hangman(self):
        self.canvas.delete("all")  # Clear the canvas
        self.canvas.create_text(150, 40, text=self.HANGMAN_PICS[self.lives], font=("Courier", 14))
        self.canvas.create_text(150, 120, text="Lives Left: {}".format(self.lives), font=("Courier", 14))
    
    def guess_letter(self):
        guessed_letter = self.guess_entry.get().lower()
        
        if len(guessed_letter) != 1:
            messagebox.showwarning("Warning", "Please enter only one letter.")
            return
        
        if guessed_letter in self.guessed_letters:
            messagebox.showinfo("Info", "You've already guessed that letter.")
        else:
            self.guessed_letters.add(guessed_letter)
            self.display.set(self.get_display())
            if guessed_letter not in self.chosen_word:
                self.lives -= 1
                self.draw_hangman()
                if self.lives == 0:
                    messagebox.showinfo("Game Over", "You ran out of lives! The word was: {}".format(self.chosen_word))
                    self.master.destroy()
                    return
        
        if self.display.get() == self.chosen_word:
            messagebox.showinfo("Congratulations", "You've guessed the word: {}".format(self.chosen_word))
            self.master.destroy()
            return
    
    def show_hint(self):
        if self.hint_used:
            messagebox.showinfo("Hint", "You've already used the hint.")
            return
        
        messagebox.showinfo("Hint", self.hint_list[self.chosen_word])
        self.hint_used = True
    
    def create_keyboard(self):
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        row_num = 0
        col_num = 0
        for i, letter in enumerate(alphabet):
            if i % 7 == 0 and i != 0:
                row_num += 1
                col_num = 0
            btn = tk.Button(self.keyboard_frame, text=letter, font=("Courier", 14), width=3, height=1, command=lambda l=letter: self.guess_from_keyboard(l))
            btn.grid(row=row_num, column=col_num, padx=2, pady=2)
            col_num += 1

    def guess_from_keyboard(self, letter):
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.insert(tk.END, letter)
        self.guess_letter()

def main():
    root = tk.Tk()
    HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()