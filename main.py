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

#Write your code below this line 👇

items = [rock, paper, scissors]
results = [["Draw","Win", "Lose"],["Lose", "Draw", "Win"],["Win", "Lose", "Draw"]]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(items[your_choice])

com_choice = random.randint(0, 2)
print("Computer choose:")
print(items[com_choice])

result = results[com_choice][your_choice]
if your_choice >= 3 or your_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
  print(f"You {result}!")

