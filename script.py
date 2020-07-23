player_1 = input("What Is The Name Of Player 1? ")

player_2 = input("What Is The Name Of Player 2? ")

current_round = int(input("What Is The Current Round? "))

print("Game On!")

print(f"Player 1: {player_1}")

print(f"Player 2: {player_2}")

print("--------------")

print(f"Round {current_round}!")

player_1_score = int(input(f"What Is {player_1} Score? "))

player_2_score = int(input(f"What Is {player_2} Score? "))

if player_1_score > player_2_score:
    print(f"{player_1} Wins!")
elif player_1_score < player_2_score:
    print(f"{player_2} Wins!")
else:
    print("It's A Draw!")

print("-----------------------")
