import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
    #Makes sure your bet was above 0
    print("------------------")
    print("Let's play coin flip!")
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0
    num = random.randint(1, 2)
    if num==1:
        val="Heads"
    else:
        val= "Tails"
    print ("You are betting "+ str(bet)+ " dollars to "+ guess)
    print ("The result of the coin has been "+ val)
    if (val==guess):
        print ("You have win "+ str(bet)+ " dollars!")
        return bet
    else:
        print ("You have lost -" +str(bet)+ " dollars!")
        return -bet

def cho_han (guess,bet):
    print("------------------")
    print("Let's play cho han!")
    #Makes sure your bet was above 0
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0
    
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    sum= dice1+dice2
    if sum%2 ==0:
        val="Even"
    else:
        val="Odd"
    print ("You are betting "+ str(bet)+ " dollars to "+ guess)
    print ("The result of the coin has been "+ val)
    if (val==guess):
        print ("You have win "+ str(bet)+ " dollars!")
        return bet
    else:
        print ("You have lost -" +str(bet)+ " dollars!")
        return -bet

def higher_card(bet):
    print("------------------")
    print("Let's play a game of cards!")
    #Makes sure your bet was above 0
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0
    
    mine=random.randint(1, 10)
    theirs=random.randint(1, 10)
    print ("You are betting "+ str(bet)+ " dollars!")
    print("Your card was " + str(mine))
    print("Their card was " + str(theirs))
    if(mine<theirs):
        print ("You have lost "+ str(bet)+ " dollars!")
        return bet
    elif(mine>theirs):
        print ("You have win "+ str(bet)+" dollars!")
        return -bet
    else:
        print("the game is a tie")
        return 0

def roulette(guess, bet):
    print("------------------")
    print("Let's play the roulette!")
    #Makes sure your bet was above 0
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0
    print ("You are betting "+ str(bet)+ " dollars to "+ str(guess))

    result = random.randint(0, 37)
    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on " + str(result))

    if guess == "Even" and result % 2 == 0 and result != 0:
        print(str(result) + " is an even number.")
        print("You won " + str(bet)+" dollars!")
        return bet

    elif guess == "Odd" and result % 2 == 1 and result != 0:
        print(str(result) + " is an odd number.")
        print("You won " + str(bet)+" dollars!")
        return bet

    elif guess == result:
        print("You guessed " + str(guess) + " and the result was " + str(result))
        print("You won " + str(bet * 35)+" dollars!")
        return bet * 35

    else:
        print("You lost " + str(bet)+" dollars!")
        return -bet


money += coin_flip("Heads", 10)
money += higher_card(5)
money += cho_han("Even", 2)
money += roulette("Even", 10)
money += roulette(3, 1)
money += roulette("Odd", money)
print("Your total amount of money is " + str(money))

