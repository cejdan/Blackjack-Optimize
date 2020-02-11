
import random

class Blackjack:
    
    def __init__(self):
        self.cardTypes = ["A","K","Q","J",10,9,8,7,6,5,4,3,2]
        self.cardSuits = ["Spade","Heart","Diamond","Club"]
        self.cardDeck = []
        
        for z in range(0,5):
            for x in range(0,13):
                for y in range(0,4):
                    self.cardDeck.append([self.cardTypes[x],self.cardSuits[y]])
                    
        random.shuffle(self.cardDeck)
    
    def reshuffle(self):
        #This method exists because we might want to re-shuffle after depleting too many cards.
        #The criteria for when to shuffle will be deployed in the main code.
        # ( <40 cards remain or something)
        
        #We just completely re-create a fresh 5-deck deck (260 cards) and shuffle it.
        #Need to clear the old deck 1st!!! Not implemented!!
        
        for z in range(0,5):
            for x in range(0,13):
                for y in range(0,4):
                    self.cardDeck.append([self.cardTypes[x],self.cardSuits[y]])
                    
        random.shuffle(self.cardDeck)
    
    
    def deal(self):
        #Deals a card to the player, then then dealer, then the player, then the dealer again, from the top of the deck.
        
        playerHand = [self.cardDeck.pop(0)]
        dealerHand = [self.cardDeck.pop(0)]
        
        playerHand.append(self.cardDeck.pop(0))
        dealerHand.append(self.cardDeck.pop(0))
        
        return playerHand, dealerHand
    
    def hit(self, hand):
        #This method adds a card to the hand, then returns the new hand.
        
        hand.append(self.cardDeck.pop(0))
        return hand
    
    def stand(self, hand): #Lol, pretty silly method. But I want it anyway because it will make the main method more readable.
        return hand
    
    def split(self, hand): #You are allowed to split if your first two cards are the same (a pair). 
        #If this method is called, and you do have two identical first cards, first it seperates the cards, and
        #draws a new pair for both of them.
        #They can then be played seperately, as normal.
        
        if (hand[0][0] != hand[1][0]):
            print ("I'm sorry, you are not allowed to split this hand!")
            return hand
        else:
            hand1 = []
            hand1.append(hand[0])
            hand1.append(self.cardDeck.pop(0))
            hand2 = []
            hand2.append(hand[1])
            hand2.append(self.cardDeck.pop(0))
            return hand1, hand2
            
        
    def calculateHand(self, hand):
        #Provided the current player or dealer's hand, calculate its value
        
        handValue = 0
        
        # len(hand) gives the current number of cards in the hand.
        
        #We deal with all non-Aces FIRST.
        for x in range (0, len(hand)):
            if (hand[x][0] != "A"): #If the first card isn't an Ace, we want to calculate it.
                if (hand[x][0] == "K" or hand[x][0] == "Q" or hand[x][0] == "J"): #If its a King, Queen, or Jack, we need to add 10 to value.
                    handValue = handValue + 10
                else: #If it's not a A, K, Q, or J, it is a number. We simply add the number to the value.
                    handValue = handValue + hand[x][0]
                
        #We deal with the Aces LAST.
        for x in range (0, len(hand)):
            if (hand[x][0] == "A" and handValue > 10): #The 10 here is to avoid busting. Basically, if a hand value is 11, and you add 11, you get 22. We don't want that.
                handValue = handValue + 1
            elif (hand[x][0] == "A" and handValue <= 10):
                handValue = handValue + 11
                
        #print("Hand value: ", handValue)
        return handValue
    
    def resolve(self, playerHand, dealerHand): #This method returns 0 if you Lose, 1 if you Win, 2 if you Push

        
        #do this in one loop, no print statements.
        resolved = False
        
        while(resolved == False):
            #3 options
            #if dealer busts
            #if dealer stands
            #if dealer hits
            
            #Option 1, dealer busts.
            if(self.calculateHand(dealerHand) > 21):
                resolved = True
                return 1
            
            #Option 2, dealer stands
            if(self.calculateHand(dealerHand) >= 17 and self.calculateHand(dealerHand) <= 21):
                #check if player or dealer won
                if (self.calculateHand(playerHand) > self.calculateHand(dealerHand)):
                    resolved = True
                    return 1
                elif (self.calculateHand(playerHand) == self.calculateHand(dealerHand)):
                    resolved = True
                    return 2
                elif (self.calculateHand(playerHand) < self.calculateHand(dealerHand)):
                    resolved = True
                    return 0
            
            #Option 3, dealer hits.
            else:
                self.hit(dealerHand)



    def playBlackjack(self, setWager = 0, hand = [], dealHand = []):
        
        if(setWager == 0):
            print("Welcome to the Hacklahoma 2020 Blackjack table!")
    
        playerChips = 1000
        leftCasino = False
        handComplete = False
        wager = setWager
        
        
        while leftCasino == False:
            
            if(len(hand) != 0): #This helps us Leave the Casino if we choose to split.
                leftCasino = True
            
            
            if(setWager == 0): #If we have a wager preselected (for split) then skip wager selection.
                handComplete = False
                print("You have", playerChips, "chips remaining.")
                if (playerChips == 0):
                    print ("So sorry, you lost all your money! Probably time to go home... :(")
                    leftCasino = True
                    break
                wager = input("How much would you like to wager on this hand? (type q to quit) ")
                if (wager == "q"):
                    leftCasino = True
                    if (playerChips > 1000):
                        print ("Great job, you won! You walked away with", playerChips, "chips!!")
                    elif (playerChips == 1000):
                        print ("You broke even! Not bad. You walked away with exactly", playerChips, "chips!")
                    else:
                        print ("Sorry, the casino took your money. You walked away with", playerChips, "chips. :(")
                        break
                try:
                    wager = int(wager)            
                except:
                    print("Sorry, the input was not an integer.")
                    continue
                if (wager > playerChips):
                    print ("Sorry, you don't have enough chips for that! You have ", playerChips, " chips remaining.") 
                    continue
                
            playerHand = hand
            dealerHand = dealHand
            
            if(len(playerHand) == 0): #Skip the deal phase if you pre-supply a hand (for split)
                playerHand, dealerHand = self.deal()
            
                
            
            initialHand = [playerHand[0], playerHand[1]] #Adding this variable as a convienient reference, to check if you got a natural blackjack.

            print("Player hand: ", playerHand)
            print("Dealer hand: ", dealerHand[0], ", ???")
    
            while handComplete == False:
     
                if (self.calculateHand(playerHand) == 21):
                    if (self.calculateHand(initialHand) == 21):
                        print ("Blackjack!!")
                        if(self.calculateHand(dealerHand) != 21):
                            print("Dealer shows:")
                            print(dealerHand)
                            print ("You win! You won 1.5x extra chips! You won ", wager * 1.5, "chips!")
                            playerChips = playerChips + (wager * 1.5)
                            break
                        elif(self.calculateHand(dealerHand) == 21):
                            print("Dealer shows:")
                            print(dealerHand)
                            print ("Unlucky! Dealer also has a Natural Blackjack! It's a push! You keep your money.")
                            break
                    else:
                        print ("21!")
                    if(self.resolve(playerHand, dealerHand) == 1):
                        print("Dealer shows:")
                        print(dealerHand)
                        print ("You win! You won", wager, "chips!")
                        playerChips = playerChips + wager
                        break
                    else:
                        print("Dealer shows:")
                        print(dealerHand)
                        print ("It's a push! You keep your money.")
                        break
            
                    handComplete = True
                    break
            
                if (playerHand[0][0] == playerHand[1][0]):
                    player_choice = input("What would you like to do? Your options are: \nSplit\nHit\nStand\nDouble\nSurrender\n")
                elif (len(playerHand) == 2):
                    player_choice = input("What would you like to do? Your options are:\nHit\nStand\nDouble\nSurrender\n")
                else:
                    player_choice = input("What would you like to do? Your options are:\nHit\nStand\n")
    
                if (player_choice.isalpha()):
                    if (player_choice == "Split" or player_choice == "split" or player_choice == "sp" and playerHand[0][0] == playerHand[1][0]):
                        playerHand1, playerHand2 = self.split(playerHand)
                        self.playBlackjack(setWager = wager, hand = playerHand1, dealHand = dealerHand)
                        self.playBlackjack(setWager = wager, hand = playerHand2, dealHand = dealerHand)
                        #At this point, both hands must have resolved to get back to this line. So the hand is complete.
            
                    if (player_choice == "Hit" or player_choice == "hit" or player_choice == "h"):
                        playerHand = self.hit(playerHand)
                        print ("Your new hand is: ", playerHand)
                        if (self.calculateHand(playerHand) <= 21):
                            continue
                        else:
                            print("You bust, sorry!")
                            playerChips = playerChips - wager
                            handComplete = True
                
                
                    if (player_choice == "Stand" or player_choice == "stand" or player_choice == "s"):
                        playerHand = self.stand(playerHand)
                        #Need to resolve the game here. No more options exist for the player.
                        #I want to turn this into a method! 
                        # self.resolve(playerHand, dealerHand) --> returns 0, 1, or 2. 0 means you lose, 1 means you win, 2 means push.
                        if(self.resolve(playerHand, dealerHand) == 0):
                            print("Dealer shows:")
                            print(dealerHand)
                            print ("So sorry, the dealer wins. You lost ", wager, "chips.")
                            playerChips = playerChips - wager
                        elif(self.resolve(playerHand, dealerHand) == 1):
                            print("Dealer shows:")
                            print(dealerHand)
                            print ("You win! You won", wager, "chips!")
                            playerChips = playerChips + wager
                        else:
                            print("Dealer shows:")
                            print(dealerHand)
                            print ("It's a push! You keep your money.")
                
                        handComplete = True
            
                    if (player_choice == "Double" or player_choice == "double" or player_choice == "d" and len(playerHand) == 2):
                        wager = wager * 2
                        #You only get one more card at this point. Then we evaluate the dealer, then resolve the game.
                        playerHand = self.hit(playerHand)
                        print ("Your new hand is: ", playerHand)
                
                        #Need to check if you bust before you resolve the game.
                
                        if(self.calculateHand(playerHand) > 21):
                            print("You bust, sorry!")
                            playerChips = playerChips - wager
                            
                        else:
                
                            if(self.resolve(playerHand, dealerHand) == 0):
                                print("Dealer shows:")
                                print(dealerHand)
                                print ("So sorry, the dealer wins. You lost ", wager, "chips.")
                                playerChips = playerChips - wager
                            elif(self.resolve(playerHand, dealerHand) == 1):
                                print("Dealer shows:")
                                print(dealerHand)
                                print ("You win! You won", wager, "chips!")
                                playerChips = playerChips + wager
                            else:
                                print("Dealer shows:")
                                print(dealerHand)
                                print ("It's a push! You keep your money.")
                    
                        handComplete = True
            
                    if (player_choice == "Surrender" or player_choice == "surrender" or player_choice == "su"):
                        wager = int(wager / 2)
                        playerChips = playerChips - wager
                        self.resolve(playerHand, dealerHand)
                        print("Dealer shows:")
                        print(dealerHand)
                        print("but you surrendered! You lost ", wager, "chips")
                
                
                    handComplete = True
            
                else:
                    print("Sorry, you didn't input a valid string")





                
###################################################################################


#MAIN METHOD BEGINS HERE
        
            # Known bugs:
            # If you get a natural Blackjack, you can push incorrectly. In the casino, the dealer only checks for a push if they are
            # showing an A or a 10, J, Q, or K. You win if they don't also have a natural blackjack.
            # Game will crash if played too many times. Need to implement reshuffle()
            # reshuffle() right now doesn't clear the old deck, just appends on a new 5 decks. Not intended!
            # You can win a Blackjack and recieve decimal chips. due to the 1.5x. Need to add a rounding feature.
            
            




myGame = Blackjack()
myGame.playBlackjack()


#print (myGame.cardDeck) #cheat code


