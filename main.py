import random ,time

print("~~~Hello Welcome To BlackJack!~~~")
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
playerHand = []
dealerHand = []
def dealPlayer():
    playerHand.append(random.choice(cards))
    playerHand.append(random.choice(cards))

def dealDealer():
    dealerHand.append(random.choice(cards))
    dealerHand.append(random.choice(cards))

def hitPlayer():
    playerHand.append(random.choice(cards))

def hitDealer():
    dealerHand.append(random.choice(cards))



def main():
    wins = 0
    loss = 0
    game = True
    while game == True:
        playerHand.clear()
        dealerHand.clear()
        print("----Wins:", str(wins), "----")
        print("----Losses:", str(loss),"----")
        dealPlayer()
        dealDealer()
        print("Your cards are:" , playerHand, "~", sum(playerHand), "~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("The dealer is showing: ", "~", dealerHand[0], "~")

        choice = int(input("Please enter 1 to hit or 0 to stand: "))
        while choice != 1 and choice != 0:
            print("Please enter a valid choice of either 1 or 0: ")
            choice = int(input())



        # allow player to continue hitting until bust, 21, or stand
        while sum(playerHand) < 21 and choice == 1:
            hitPlayer()
            print("Your hand is now: ",playerHand, "~", sum(playerHand), "~")
            if sum(playerHand) > 21:
                print("You busted at ", sum(playerHand), "better luck next time!")
                loss = loss + 1
            if sum(playerHand) == 21:
                print("Congrats you got 21!!")
                wins = wins + 1
            if sum(playerHand) < 21:
                choice = int(input("Please enter 1 to hit or 0 to stand: "))

        #dealer win/lose
        if choice == 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("The dealer will now attempt to get 21")
            if sum(dealerHand)  > sum(playerHand):
                print("You lost the dealer has ~", sum(dealerHand), " ~")
                loss = loss + 1
            while sum(dealerHand) < sum(playerHand) and sum(dealerHand) < 21:
                hitDealer()
                print(dealerHand, "~", sum(dealerHand), "~")
                time.sleep(1)
                if sum(dealerHand) > sum(playerHand) and sum(dealerHand) <= 21:
                    print("You lost the final score was", sum(dealerHand), "-", sum(playerHand))
                    loss = loss + 1
                if sum(dealerHand) > sum(playerHand) and sum(dealerHand) > 21:
                    print("You won! the dealer busted at", sum(dealerHand), ".")
                    wins = wins + 1
                if sum(dealerHand) == sum(playerHand):
                    print("You lost, the house always wins on ties!")
                    loss = loss + 1
        user_input = input("Would you like to play again? yes or no: ")
        user_input = user_input.lower()
        while user_input != "yes" and user_input != "no":
            user_input = input("PLEASE only enter yes or no: ")
            user_input = user_input.lower()
        if user_input == "yes":
            game == True
        else:
            print("The final score was " , wins , " wins and " , loss , " losses!")
            if wins > loss:
                print("Looks like you came out on top.")

            if loss > wins:
                print("Looks like you didnt do so hot.")

            break


main()

