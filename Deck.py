import random;

# Initializing Varibles
p1_Score = p2_Score = 0;
p1_Card = p2_Card = ["","",""];
numbers = "2 3 4 5 6 7 8 9 10 Jack Queen King Ace".split();
suits = " Diamonds Hearts Clubs Spades".split();
deck = ["Red Joker", "Black Joker"];

# Builds Deck
for n in numbers:
  for suit in suits:
    deck.append(n + " of " + suit);

# Shuffles Deck
random.shuffle(deck);

# Functions
def switchNumber(x): # Changes Cards to Number, so it is easier to compare
  return{
    "Ace" : 14,
    "King" : 13,
    "Queen" : 12,
    "Jack" : 11,
    "10" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
  }[x]

def switchSuit(x): # Changes Suit to Number so it is easier to compare 
  return{
    "Diamonds" : 1,
    "Hearts" : 2,
    "Clubs" : 3,
    "Spades" : 4
  }[x]

def compare_Card():
  if(p1_Card[1] == "Joker" and p2_Card[1] == "Joker"): # If Both Players have Joker, it is a tie
    print("Draw");
    return 0;
  elif(p1_Card[1] == "Joker"): # P1 with Joker only 
    print("Player 1 Wins!");
    return 1;
  elif(p2_Card[1] == "Joker"): # P2 with Joker only
    print("Player 2 Wins!");
    return -1;
  else:
    # Converts Card to Numbers
    p1_Card[0] = switchNumber(p1_Card[0]);
    p2_Card[0] = switchNumber(p2_Card[0]);
    
    if(p1_Card[0] == p2_Card[0]): # If Number is same, Baises Winner on Suit
      p1_Card[2] = switchSuit(p1_Card[2]);
      p2_Card[2] = switchSuit(p2_Card[2]);
      if(p1_Card[2] > p2_Card[2]):
        print("Player 1 Wins!"); # Player 1 has better Suit
        return 1;
      else:
        print("Player 2 Wins!"); # Player 1 has better Suit
        return -1;
    elif(p1_Card[0] > p2_Card[0]): # Player 1 has better starting card
      print("Player 1 Wins");
      return 1;
    else:
      print("Player 2 Wins"); # Player 2 has better starting card
      return -1;
  
def helpMe(): # Details the Rules of the Game
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
  print("Cards are valued from 2 to Ace to Joker in increasing order,");
  print("and suits are ordered from Diamond,  Hearts, Clubs(clover) and Spades.");
  print("With the Jokers being the Trump Cards.");
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");

def current_Score(): # Lets Players know the current Score
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
  print("Current Score");
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
  print("Player 1: " + str(p1_Score));
  print("Player 2: " + str(p2_Score));
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  
# Main
while True:
  a=input("Press Enter to Draw Cards.\nPress ? for Current Score\nPress ! for Help.\nPress Anything else to Quit.");
  if a == "!":
    helpMe();
    continue;
  elif a == "?":
    current_Score();
    continue;
  elif a != "":
    break;
  
  # Hands out Cards
  p1_Card = deck.pop();
  p2_Card = deck.pop();
  print();
  print("Player 1's Card is: " + p1_Card);
  print("Player 2's Card is: " + p2_Card);
  print();
  
  # Splits up String so it is easier to compare
  p1_Card = p1_Card.split();
  p2_Card = p2_Card.split();
  
  # Check who has the better card
  winner = compare_Card();
  if(winner == 1):
    p1_Score += 1;
  elif(winner == -1):
    p2_Score += 1;
  
  if(len(deck) == 0): # Checks if there are any more cards in the Deck
    print("No More Cards in Deck.");
    current_Score();
    if(p1_Score == p2_Score):
      print("The Game is a Draw");
    elif(p1_Score > p2_Score):
      print("Player 1 is the Winner.");
    else:
      print("Player 2 is the Winner.");
    break;
