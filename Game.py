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
word_list=["incorrectly", "staircase", "age", "bed", "ton", "river", "comb", "fire", "breath", "hole", "nine", "needle", "envelope", "clock", "silence", "palm", "cold", "coin"]
lives= 6
chosen_word=random.choice(word_list)

display=[]
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False

while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        if lives ==0:
            game_over=True
            print("YOU LOSE !!")
    if '_' not in display:
        game_over=True
        print("YOU WIN")
    print(HANGMAN_PICS[lives])
