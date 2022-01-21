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
choices_text = ["Rock", "Paper", "Scissors"]
choices_image = [rock, paper, scissors]

print("Welcome to Rock-Paper-Scissors!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
print("you chose " + choices_text[user_choice])
print(choices_image[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose " + choices_text[computer_choice])
print(choices_image[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == computer_choice:
  print("It\'s a tie. Play again")
elif user_choice == 0 and computer_choice == 1:
  print("Computer\'s Paper covers your Rock. You Lose!")
elif user_choice == 0 and computer_choice == 2:
  print("Your Rock crushes Computer\'s Scissors. You Win!")
elif user_choice == 1 and computer_choice == 0:
  print("Your Paper covers Computer\'s Rock. You Win!")
elif user_choice == 1 and computer_choice == 2:
  print("Computer\'s Scissors cuts your Paper. You Lose!")
elif user_choice == 2 and computer_choice == 0:
  print("Computer's Rock crushes your Scissors. You Lose!")
elif user_choice == 2 and computer_choice == 1:
  print("Your Scissors cuts Computer\'s Paper. You Win!")


