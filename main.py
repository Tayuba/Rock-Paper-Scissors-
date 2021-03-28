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
print("Welcome 'Rock', 'Paper', 'Scissors' game. ")



import random
rand_g = random.randint(0, 2)
select_ch = input("Please select '1' for Rock, '2' for Paper and '3' for scissors \n")
if (select_ch) <= '0' or  (select_ch)  >= '4' :
  print("Invalid entry, you lose.")
  
elif int(select_ch) <= 0 or  int(select_ch)  >= 4 :
 print("Invalid entry, you lose.")


else:
  select_g = [rock, paper, scissors]
  select_ch1 = int(select_ch)
  select = select_g[select_ch1-1]
  rand_s = random.choice(select_g)

  print("You choose")
  print(select)
  print("Computer choose")
  print(rand_s)


  # print(type(select_ch))

  if select_ch == '1' and len(rand_s)  == 79:
   print("It draw, play again.")

  elif select_ch == '2' and len(rand_s)  == 101:
   print("It draw, play again.")

  elif select_ch == '3' and len(rand_s) == 92:
   print("It draw, play again.")

  elif select_ch == '1' and len(rand_s) == 101:
   print("You lose")

  elif select_ch == '1' and len(rand_s) == 92:
   print("You won")
  elif select_ch == '2' and len(rand_s) == 79:
   print("You won")
  elif select_ch == '2' and len(rand_s) == 92:
   print("You lose")
  elif select_ch == '3' and len(rand_s) == 79:
   print("You lose")
  elif select_ch == '3' and len(rand_s) == 101:
   print("You won")