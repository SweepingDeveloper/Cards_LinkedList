import random


# This is really a linked list, the fundamentals copied
# from others.  However, I changed the names of the elements
# to help me understand a linked list better.
class Card:
    def __init__(self, value):
        self.value = value
        self.next = None

class Deck:
    def __init__(self):
        self.topCard = None

    def addCard(self, value):
        if self.topCard is None:
            newCard = Card(value)
            self.topCard = newCard
            return

        currentCard = self.topCard

        # Go through the deck to find the last one.
        while currentCard.next is not None:
            currentCard = currentCard.next

        # Set up the new card.    
        newCard = Card(value)

        # Link that to the next card of the last one.
        currentCard.next = newCard

    # This is an attempt at making my own method of a linked list.
    # Here's hoping!
    def removeSpecCard(self, value):

        foundCard = False
        # Note to self:  First check is to see if there's an
        # empty deck (or empty list.
        if self.topCard is None:
            print ("There's no deck!")
            return

        # Oops, couldn't do it.  Oh well.  Anyway,
        # OK, first, is the card to be removed the top card?
        currentCard = self.topCard


        if currentCard.value == value:
            self.topCard = self.topCard.next

        # Go through the deck to find the specific card.
        while currentCard.next is not None:
            #print (currentCard.next.value + " = " + value + "?")
            if (currentCard.next.value == value):
                #print ("Card found")
                foundCard = True
                #print (currentCard.next.value + ", next card is " + currentCard.next.next.value)
                currentCard.next = currentCard.next.next
                #print (currentCard.next.value + ", next card is now " + currentCard.next.next.value)
            
            currentCard = currentCard.next
            if currentCard is None:
                if foundCard == False:
                    print ("Your card's not there!")
                    return

        # Now, link the current card to the one after the specific card.
        # currentCard = currentCard.next.next

        # No need to check whether the card after the specific card
        # is a none.

    def display(self):

        if self.topCard is None:
            print ("There's no deck!")
            return

        if self.topCard.next is None:
            print (self.topCard.value)
            return

        currentCard = self.topCard

        while currentCard.next is not None:
            print (currentCard.value)
            currentCard = currentCard.next
        
        print(currentCard.value)

        
    def showTopCard(self):

        if self.topCard is None:
            print("There's no deck!")
            return

        return self.topCard.value

        

        

        


cards = []
suits = ['S','C','H','D']
ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']

for s in suits:
    for r in ranks:
        cards.append(r+s)

print (cards)


def shuffle(deck):

    # Set the number of cycles to between 1000 and 5000.
    swaps = random.randint(1000,5000)
    middeck = len(deck) // 2

    # Start a cycle.
    for sw in range(0, swaps-1):

        # First, cut the cards.
        firstHalf = deck[:middeck]
        secondHalf = deck[middeck:]
        deck = secondHalf + firstHalf

        
        # Second, do a bubble sort-like swap, with
        # a coin flip determining if the elements swap.
        for a in range(0,len(deck)-1):
            willSwap = random.randint(0,1)
            if willSwap == 1:
                deck[a], deck[a+1] = deck[a+1], deck[a]

    return deck


cards = shuffle(cards)
print (cards)


myDeck = Deck()

for card in cards:
    myDeck.addCard(card)

myDeck.display()

print ("Top card is "+myDeck.showTopCard())

#Remove all the Aces.
for suit in suits:
    print ("Removing A"+str(suit))
    myDeck.removeSpecCard('A'+str(suit))

myDeck.display()

#Put the Aces back in the deck.
for suit in suits:
    myDeck.addCard('A'+str(suit))

#Plus, add some jokers.
myDeck.addCard('JOKER')
myDeck.addCard('JOKER')

myDeck.display()

#OK, now remove the top card from the deck.
print ("Removing Top Card...")

myDeck.removeSpecCard(myDeck.showTopCard())

myDeck.display()

