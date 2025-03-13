import random

def roll_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    if roll1 > roll2:
        return str(roll1)+str(roll2)
    else:
        return str(roll2)+str(roll1)


def swap(active_player):
    if active_player == "1":
        return "2"
    else:
        return "1"


#first and second should be "1" and "2" or "2" and "1"
def round(starter):
    active_player = starter

    print("")
    print(f"Player {active_player} starts: ")
    highest = roll_dice()
    print(f"Player {active_player} rolls {highest}")


    active_player = swap(active_player)
    new = roll_dice()
    print(f"Player {active_player} rolls {new}")
    while new > highest:
        highest = new
        active_player = swap(active_player)
        new = roll_dice()
        print(f"Player {active_player} rolls {new}")
    
    #in the event of a tie, no one gets any points
    if new == highest:
        print("Tie: no one wins")
        return "0", highest

    #return the winner and the score that they gain
    active_player = swap(active_player)
    print(f"Player {active_player} wins the round.")
    return active_player, highest




def main():
    print("Let's play Beat That!")
    print("Two players will alternate turns.")
    print("The first player will roll two dice and put the numbers together (larger then smaller) to make a two digit number. For example, rolling a 3 and a 5 would yield 53.")
    print("The second player rolls both dice and tries to get a larger number.")
    print("If they succeed, continue in this manner. If they fail, the first player adds the largest number to their score.")
    print("The first player to reach 100 points wins.")

    player1_score = 0
    player2_score = 0
    active_player = "1"
    while player1_score < 100 and player2_score < 100:
        winner, round_total = round(active_player)
        if winner == "1":
            player1_score += int(round_total)
        elif winner == "2":
            player2_score += int(round_total)
        print(f"Player 1 score: {player1_score}")
        print(f"Player 2 score: {player2_score}")
        active_player = swap(active_player)


    print("")
    if player1_score >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

main()