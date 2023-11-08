import random

def roll():
    roll = random.randint(1, 6)
    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)] #list comprehension // puts a 0 in the list for every single player we have 

while max(player_scores) < max_score:

    for player_i in range(players):
        print("\nPlayer", player_i + 1, "turn has just started\n")
        print("Your current total score is:", player_scores[player_i], "\n")
        current_score = 0 
        
        while True: 
            should_roll = input("Would you like to roll? (y/n) ").lower()
            if should_roll != 'y':
                break

            value = roll()

            if value == 1:
                print("You rolled a 1, your turn is done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
    
            print("Your score is:", current_score)

        player_scores[player_i] += current_score
        print("Your total score is:", player_scores[player_i])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player,", winning_index + 1, "is the winner with a score of:", max_score)