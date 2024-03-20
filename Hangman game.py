#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

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

word_list = ["incorrectly", "staircase", "age", "bed", "ton", "river", "comb", "fire", "breath", "hole", "nine",
             "needle", "envelope", "clock", "silence", "palm", "cold", "coin"]

hint_list = {
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

lives = 6

chosen_word = random.choice(word_list)

display = ['_'] * len(chosen_word)

print(display)

game_over = False

hint_used = False  

print("Welcome to Hangman! Type 'hint' during the game to receive a hint about the word.")

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    
    if guessed_letter == "hint" and not hint_used:
        hint_used = True
        print("Hint:", hint_list[chosen_word])
        
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = guessed_letter
        
        print(display)
        
        if guessed_letter not in chosen_word:
            lives -= 1
            if lives == 0:
                game_over = True
                print("YOU LOSE !!")
        
        if '_' not in display:
            game_over = True
            print("YOU WIN")
        
        print(HANGMAN_PICS[lives])

