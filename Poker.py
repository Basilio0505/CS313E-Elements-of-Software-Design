#  File: Poker.py

#  Description:This program will simulate a game of poker dealing hands, checking each players hand, and deciding
# a winner.

#  Student's Name: Basilio Bazan

#  Student's UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 09/28/2018

#  Date Last Modified: 09/28/2018

import random

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

class Deck (object):
    # constructor
    def __init__ (self, n = 1):
        self.deck = []
        for i in range(n):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card (rank, suit)
                    self.deck.append (card)

    # shuffle the deck
    def shuffle (self):
        random.shuffle (self.deck)

    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker(object):
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards

        # deal all the hands
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.append(hand)

    # simulates the play of the game
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse=True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)

        # determine the type of each hand and print
        points_hand = []  # create a list to store points for each hand
        hand_type = []
        print()

        for i in range(len(self.all_hands)):
            if self.is_royal(self.all_hands[i]) !=0:
                points_hand.append(self.is_royal(self.all_hands[i]))
                print("Player " + str(i+1)+": Royal Flush")
                hand_type.append("Royal Flush")
            elif self.is_straight_flush(self.all_hands[i]) !=0:
                points_hand.append(self.is_straight_flush(self.all_hands[i]))
                print("Player " + str(i+1) + ": Straight Flush")
                hand_type.append("Straight Flush")
            elif self.is_four_kind(self.all_hands[i]) !=0:
                points_hand.append(self.is_four_kind(self.all_hands[i]))
                print("Player " + str(i+1) + ": Four of a Kind")
                hand_type.append("Four of a Kind")
            elif self.is_full_house(self.all_hands[i]) !=0:
                points_hand.append(self.is_full_house(self.all_hands[i]))
                print("Player " + str(i+1) + ": Full House")
                hand_type.append("Full House")
            elif self.is_flush(self.all_hands[i]) !=0:
                points_hand.append(self.is_flush(self.all_hands[i]))
                print("Player " + str(i+1) + ": Flush")
                hand_type.append("Flush")
            elif self.is_straight(self.all_hands[i]) !=0:
                points_hand.append(self.is_straight(self.all_hands[i]))
                print("Player " + str(i+1) + ": Straight")
                hand_type.append("Straight")
            elif self.is_three_kind(self.all_hands[i]) !=0:
                points_hand.append(self.is_three_kind(self.all_hands[i]))
                print("Player " + str(i+1) + ": Three of a Kind")
                hand_type.append("Three of a Kind")
            elif self.is_two_pair(self.all_hands[i]) !=0:
                points_hand.append(self.is_two_pair(self.all_hands[i]))
                print("Player " + str(i+1) + ": Two pair")
                hand_type.append("Two Pair")
            elif self.is_one_pair(self.all_hands[i]) != 0:
                points_hand.append(self.is_one_pair(self.all_hands[i]))
                print("Player " + str(i+1) + ": Pair")
                hand_type.append("Pair")
            else:
                points_hand.append(self.is_high_card(self.all_hands[i]))
                print("Player " + str(i+1) + ": High Card")
                hand_type.append("High Card")


        # determine winner and print
        print()

        high = 0
        for i in range(len(points_hand)):
            if points_hand[i] > high:
                high = points_hand[i]

        for i in range(len(points_hand)):
            if points_hand[i] == high:
                print("Player "+str(i+1)+" wins.")
                break

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1): #Checks if all cards are same suit
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        rank_order = True
        for i in range(len(hand)): #Checks if cards are A,K,Q,J,10
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points


    def is_straight_flush (self, hand):
        same_suit = True
        for i in range(len(hand) - 1): #Checks if all cards are same suit
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        if (not same_suit):
            return 0

        rank_order = True
        for i in range(len(hand)-1): #Checks if cards are in numerical sequence
            rank_order = rank_order and (hand[i].rank+1 == hand[i+1].rank)
        if (not rank_order):
            return 0

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    def is_four_kind (self, hand):
        count = 0
        for i in range(len(hand)-1): #checks if there is a four of a kind
            if hand[i].rank == hand[i+1].rank:
                count+=1 #Tracks amount of pair when count is 3 it means a four of a kind
        if count != 3:
            return 0

        points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    def is_full_house (self, hand):
        count1 = 0
        count2 = 0
        change = False
        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i+1].rank:
                if not change: #Makes sure there is both a pair and three of a kind no matter the order.
                    count1 += 1
                if change:
                    count2 += 1
            else:
                change = True

        if (count1 != 3 and count2 !=2) or (count1 != 2 and count2 != 3):
            return 0

        points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    def is_flush (self, hand):
        same_suit = True
        for i in range(len(hand) - 1): #Checks if all cards are same suit
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        if (not same_suit):
            return 0

        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    def is_straight (self, hand):
        rank_order = True
        for i in range(len(hand) - 1): #Checks if cards are in numerical order
            rank_order = rank_order and (hand[i].rank + 1 == hand[i + 1].rank)
        if (not rank_order):
            return 0

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    def is_three_kind (self, hand):
        three = False
        for i in range(1,len(hand) - 1):  # checks if there is a three of a kind
            if hand[i-1].rank == hand[i].rank == hand[i + 1].rank:
                three = True
                break
        if not three:
            return 0

        points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    def is_two_pair (self, hand):
        count = 0
        for i in range(len(hand) - 1):  # checks if there is a pair
            if hand[i].rank == hand[i + 1].rank:
                count += 1  # Tracks amount of pair when count is 2 it means two pair
        if count != 2:
            return 0

        points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_one_pair(self, hand):
        one_pair = False
        rank = 0
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                rank = hand[i].rank
                break
        if (not one_pair):
            return 0

        points = rank +13

        return points

    def is_high_card (self, hand):
        return hand[0].rank #Returns the rank of the high card, also used for tie breakers

def main():
    # prompt the user to enter the number of players
    num_players = int(input('Enter number of players: '))
    while ((num_players < 2) or (num_players > 6)):
        num_players = int(input('Enter number of players: '))

    # create the Poker object
    print()
    game = Poker(num_players)

    # play the game - poker
    game.play()

# do not remove this line above main()
if __name__ == '__main__':
    main()