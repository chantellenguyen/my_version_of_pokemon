import random

pokemon_list = [
["fastest boiiii",840,900],
["sylvion",836,346],
["Dratini",296,830],
["Minccino",746,897]
]



#Loop through the pokemon list
print("Please choose from the below Pokemon for your battle: ")
for i in range(len(pokemon_list)):
  print(f"{i+1}. {pokemon_list[i]}")

#Make the user choose a pokemon
player1= int(input("Please give a number for your pokemon choice: "))
while(player1-1 not in range(len(pokemon_list))):
  player1 = int(input("Invalid choice, please choose from the above: "))

#Select the choice of pokemon for both players
player1 = pokemon_list[player1-1]
player2 = random.choice(pokemon_list)

#player1[0] = name,
#player1[1] = attack
#player1[2] = HP

print(f"Player 1 chose {player1[0]}")
print(f"Player 2 chose {player2[0]}")

# Game loop
while player1[2] > 0 and player2[2] > 0:
  print("Player 1's turn:")
  choice = input("Enter 'a' to attack or 'h' to heal: ")
  if choice == 'a':
    player1_attack = random.randint(1, player1[1])
    player2[2] -= player1_attack
    print(f"{player1[0]} attacks {player2[0]} for {player1_attack} damage.")

  elif choice == 'h':
    player1_heal = random.randint(10, 25)
    player1[2] += player1_heal
    print(f"{player1[0]} heals for {player1_heal} HP.")

  print(f"{player1[0]} has {player1[2]} HP left")

  if player2[2] <= 0:
        print(f"{player2[0]} fainted. Player 1 wins! with {player1[0]}")
        break


  # Player 2's turn
  print("Player 2's turn:")
  if random.choice([True, False]):  # Randomly decide whether Player 2 heals or attacks
      player2_attack = random.randint(1, player2[1])
      player1[2] -= player2_attack
      print(f"Player 2 attacks {player1[0]} for {player2_attack} damage.")
  else:
      player2_heal = random.randint(10,25)
      player2[2] += player2_heal
      print(f"Player 2 heals for {player2_heal} HP.")

  print(f"{player2[0]} has {player2[2]} HP left")


  if player1[2] <= 0:
      print(f"{player1[0]} fainted. Player 2 wins!\n")
      break

print("Game over!")
