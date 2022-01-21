import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock-Paper-Scissors!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

computer_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == computer_choice:
  print("It\'s a tie. play again")
elif user_choice == 0 and computer_choice == 1:
  print("Paper Covers Rock. You lose!")
elif user_choice == 0 and computer_choice == 2:
  print("Rock Crushes Scissors. You Win!")
elif user_choice == 1 and computer_choice == 2:
  print("Scissors Cuts Paper. You lose!")




