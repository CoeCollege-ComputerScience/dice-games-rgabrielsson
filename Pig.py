import random

def roll_die():
    return random.randint(1,6)


def player_turn(player):
    print("")
    print(f"Player {player}: ")

    #setup
    turnTotal = 0
    hold = "n"
    
    #roll dice and add the score to the round total as long as the player doesn't hold or roll a 1
    while hold != "y":
        roll = roll_die()
        if roll == 1:
            print("Sorry, you rolled a 1.")
            return 0
        else:
            turnTotal += roll
            print(f"You rolled a {roll}. Your turn total is now {turnTotal}.")
            hold = (input("Would you like to hold? (y/n): ")).lower()
    return turnTotal


def main():
    print("Let's play Pig!")
    print("Two players will alternate turns.")
    print("During a player's turn, they will repeatedly roll the die until they decide to hold (keep the current total) or roll a 1.")
    print("The first player to reach a score of 100 wins.")

    #setup
    player1_score = 0
    player2_score = 0
    required_score = 100

    #alternate player turns as long as neither player attains the score required to win
    while player1_score < required_score and player2_score < required_score:
        player1_score += player_turn(1)
        print(f"Player 1 score: {player1_score}")
        if player1_score >= required_score:
            break
        player2_score += player_turn(2)
        print(f"Player 2 score: {player2_score}")
    
    #declare a winner
    if player1_score >= required_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

main()