#High Low Game
import random
import os
from game_data import data
from art import logo, vs

score = 0
def increment_score():
 global score 
 score += 1

def clear_score():
  global score
  score = 0

def game(correct_index = -1, first_run = True):
  if correct_index == -1 and first_run == False:
    return 0

  message = ""
  global score

  def get_record():
    return random.choice(data)

  if correct_index == -1:
    data_a = get_record()
  else:
    data_a = data[correct_index]
    increment_score()
    message = f"Correct! Current Score: {score}"

  data_b = get_record()
  while data_a == data_b:
    data_b = get_record()


  def get_answer():  
    return input("Who has more followers? Type 'A' or 'B': ").lower()

  def get_correct_data(a, b):
    if a["follower_count"] > b["follower_count"]:
      return a
    else:
      return b

  os.system("clear")
  print(logo)
  print(message)
  print(f"Compare A: {data_a['name']}, {data_a['description']}, from {data_a['country']}")
  print(vs)
  print(f"Against B: {data_b['name']}, {data_b['description']}, from {data_b['country']}")

  player_answer = get_answer()
  if player_answer == "a":
    if data_a == get_correct_data(data_a, data_b):
      game(correct_index = data.index(data_a), first_run = False)
    else:
      clear_score()
      game(correct_index = -1, first_run = False)      
  elif player_answer == "b":
    if data_b == get_correct_data(data_a, data_b):
      game(correct_index = data.index(data_b), first_run = False)
    else:
      clear_score()
      game(correct_index = -1, first_run = False)


game()