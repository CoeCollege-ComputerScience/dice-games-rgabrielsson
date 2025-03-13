import random

def roll_die():
    return random.randint(1,6)


def player_turn(player):
    print("")
    print(f"Player {player}: ")

    turnTotal = 0
    hold = "n"
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

    player1_score = 0
    player2_score = 0
    while player1_score < 100 and player2_score < 100:
        player1_score += player_turn(1)
        print(f"Player 1 score: {player1_score}")
        if player1_score >= 100:
            break
        player2_score += player_turn(2)
        print(f"Player 2 score: {player2_score}")
    if player1_score >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

main()