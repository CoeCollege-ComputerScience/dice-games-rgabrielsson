import random

def roll_dice(num_dice):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1,6)
        total += roll
    return total

def roll_bones():
    print("")
    print("Let's play Roll the Bones!")
    print("This is a one-player game.")
    print("Each round, you will enter a guess between 5 and 30.")
    print("Then, five dice will be rolled and the total will be accumulated")
    print("If the guess is less than the total, you gain your guess - 5 points.")
    print("If the guess is more than the total, you lose your guess - 5 points.")
    print("If you guess the number exactly, you get 50 points.")
    print("")

    total_points = 0
    avg_points = 0
    turn_count = 0
    done = "n"

    while done != "y":
        guess = int(input("Enter your guess (5-30): "))
        while not (5 <= guess <= 30):
            print("Invalid guess, please enter an integer between 5 and 30.")
            guess = int(input("Enter your guess (5-30): "))
        dice_total = roll_dice(5)
        print(f"The dice total was {dice_total}.")

        if guess == dice_total:
            total_points += 50
            print("You win 50 points!")
        elif guess < dice_total:
            total_points += (guess-5)
            print(f"You win {guess-5} points!")
        else:
            total_points += (5-guess)
            print(f"You lose {guess-5} points.")

        turn_count += 1
        avg_points = total_points / turn_count

        print(f"Total points: {total_points}")
        print(f"Average points per turn: {avg_points}")
        done = (input("Are you done? (y/n): ")).lower()
        while done != "n" and done != "y":
            print("Invalid input.")
            done = (input("Are you done? (y/n): ")).lower()
        print("")

roll_bones()
