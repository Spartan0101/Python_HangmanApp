import random
import art
import words
#import os
from replit import clear

#def cls():
    #os.system('cls' if os.name == 'nt' else 'clear')


print(art.logo)

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#print(chosen_word)

display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()

    clear()

    if guess_letter in display:
        print(f"You've already guessed {guess_letter}")

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess_letter}")
        if letter == guess_letter:
            display[position] = letter

    if guess_letter not in chosen_word:
        print(f"{guess_letter} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(art.stages[lives])