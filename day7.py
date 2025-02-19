import random

stages = ['''
   +----+
   |    |
   0    |
  /|\   |
  / \   |
        |
==========
''', '''
 +----+
   |    |
   0    |
  /|\   |
  /     |
        |
==========
''', '''
 +----+
   |    |
   0    |
  /|\   |
        |
        |
==========
''', '''
 +----+
   |    |
   0    |
  /|    |
        |
        |
==========
''', '''
 +----+
   |    |
   0    |
   |    |
        |
        |
==========
''', '''
 +----+
   |    |
   0    |
        |
        |
        |
==========
''', '''
 +----+
   |    |
        |
        |
        |
        |
==========
''']

lives = 6
words = ['avni', 'mango', 'orange', 'elephant']

chosen_word = random.choice(words)
print(f"The chosen word is: {chosen_word}")

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    print(stages[lives])  
    guess = input("Guess the letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed the letter {guess}")
        continue

    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("YOU WIN!!!")

    if lives == 0:
        game_over = True
        print("YOU LOST!!! GAME OVER")
