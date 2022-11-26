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
length = len(items) 

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(items[your_choice])

print("Computer choose:")
com_choice = random.randint(0, length - 1)
print(items[com_choice])

result = results[com_choice][your_choice]
print(f"You {result}!")

