import random

#roll dice and count how many of each outcome
def roll_dice(num_dice):
    outcomes = [0,0,0,0,0,0]
    for i in range(num_dice):
        roll = random.randint(1,6)
        outcomes[roll-1] += 1
    return outcomes

def swap(active_player):
    if active_player == "1":
        return "2"
    else:
        return "1"
    



def multiples_stay():
    print("Let's play Multiples Stay!")
    print("This game is played with two players and ten dice.")
    print("A Player starts by rolling all ten dice. Count the number of times each outcome was rolled. The player is allowed to select any one outcome that occurred more than once.")
    print("The dice that match that outcome are removed and the remaining dice are rerolled by the next player.")
    print("The game ends and you lose when you can no longer remove multiples from the roll.")
    print("")
    
    #setup
    active_player = "1"
    num_dice = 10
    while True:
        print(f"Player {active_player}'s turn.")

        #get outcomes and show them to the players
        options = []
        outcomes = roll_dice(num_dice)
        #print(outcomes)
        for i in range(len(outcomes)):
            if outcomes[i] > 1:
                print(f"There are {outcomes[i]} dice with the number {i+1}.")
                options.append(i+1)
        
        #end condition -- no options to remove
        if options == []:
            print(f"No multiples were rolled. Player {active_player} loses.")
            active_player = swap(active_player)
            print(f"Player {active_player} wins!")
            break
        
        #multiples exist -- ask player for input and remove the appropriate multiples
        dice_to_remove = int(input("Enter which number you would like to remove: "))
        while dice_to_remove not in options:
            print("Invalid number. Please select a number with multiple rolls.")
            dice_to_remove = int(input("Enter which number you would like to remove: "))
        
        num_dice = num_dice - outcomes[dice_to_remove - 1]
        print(f"{num_dice} dice remain.")
        active_player = swap(active_player)
        print("")
        

multiples_stay()
