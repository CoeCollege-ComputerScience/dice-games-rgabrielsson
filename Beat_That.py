import random

def roll_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    if roll1 > roll2:
        return str(roll1)+str(roll2)
    else:
        return str(roll2)+str(roll1)

def player_turn(first,second):

    print("")
    print(f"Player {first} starts: ")
    highest = roll_dice()
    print(f"Player {first} rolls {highest}.")


    
    new = roll_dice()
    while new > highest:
        highest = new
        new = roll_dice()
        print(f"Player {player} rolled {new}")
    return highest




def main():
    print("Let's play Beat That!")
    print("Two players will alternate turns.")
    print("The first player will roll two dice and put the numbers together (larger then smaller) to make a two digit number. For example, rolling a 3 and a 5 would yield 53.")
    print("The second player rolls both dice and tries to get a larger number.")
    print("If they succeed, continue in this manner. If they fail, the first player adds the largest number to their score.")
    print("The first player to reach 100 points wins.")

    player1_score = 0
    player2_score = 0
    while player1_score < 100 and player2_score < 100:
        




    if player1_score >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

#main()