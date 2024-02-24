import random
game_over = False
lives = 0
logo = """


   _____                                                                            ___  
  / ____|                                                                          |__ \ 
 | |     __ _ _ __    _   _  ___  _   _    __ _ _   _  ___  ___ ___   _ __ ___   ___  ) |
 | |    / _` | '_ \  | | | |/ _ \| | | |  / _` | | | |/ _ \/ __/ __| | '_ ` _ \ / _ \/ / 
 | |___| (_| | | | | | |_| | (_) | |_| | | (_| | |_| |  __/\__ \__ \ | | | | | |  __/_|  
  \_____\__,_|_| |_|  \__, |\___/ \__,_|  \__, |\__,_|\___||___/___/ |_| |_| |_|\___(_)  
                       __/ |               __/ |                                         
                      |___/               |___/                                          """

def check_number(random_num, guess_num):
  global game_over, lives
  if random_num == guess_num:
    game_over = True
    return f"You got it! the number is {guess_num}"
  elif random_num > guess_num:
    lives -= 1
    return "Too low"
  else:
    lives -= 1
    return "Too high"


def play_game():
  global game_over, lives
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100 what it is?")
  difficulty = input("Choose a difficulty (easy or hard): ")
  if difficulty == "easy":
    lives = 10
  else:
    lives = 5
  random_num = random.randint(1, 100)
  while not game_over:
    print(f"You have {lives} attempts left.")
    guess_num = int(input("Enter your Guess: "))
    print(check_number(random_num, guess_num))
    if lives == 0:
      game_over = True
      print("Game Over you have 0 attempts left.")
      print("The number was", random_num)

play_game()


