import random
rock = '''
     --------
---'    ______)
       (______)
       (______)
       (______)
------(______)
'''
paper = '''
     -------
-----'     ___)____
            __________)
            ___________)
            __________)
--- . ___________)
'''
scissors = '''
___'-------
      ____)___
          ______)
      __________)
      (_)
---.()
'''

game_images = [rock,paper,scissors]
user_choice = int(input("what do choose? type 0 for rock, 1 for paper or 2 for scissoes\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("computer chose:")
print(game_images[computer_choice])
if user_choice == 0 and computer_choice == 2:
 print("you win")
elif computer_choice == 1 and user_choice == 2:
    print("you lose")
elif computer_choice == 0 and user_choice == 1:
   print("you win")
elif user_choice == 2 and computer_choice == 0:
 print("you loss")
elif computer_choice == 2 and user_choice == 1:
    print("you lose")
elif computer_choice == 1 and user_choice == 0:
   print("you loss")
elif computer_choice == user_choice:
   print("it's draw")
else:
    print("please type vailed number . you loss")