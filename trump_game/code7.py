import random

class Card:
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            self.intValue = intValue

      def infoOfCard(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

class Deck:
      def __init__(self):
            self.deck = self.generateDeck()

      def printCard(self):
            print("Displaying cards...")
            for i in self.deck:
                  print(i.infoOfCard())

      def shuffleDeck(self):
            shuffledDeck = []
            for i, card in enumerate(self.deck):
                  shuffledDeck.append(card)
                  j = random.randint(0,i)
                  temp = shuffledDeck[j]
                  shuffledDeck[j] = card
                  shuffledDeck[i] = temp

            self.deck = shuffledDeck

      def draw(self):
            return self.deck.pop()

      @staticmethod
      def generateDeck():
            newDeck = []
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            suits = ["♦︎", "♡", "♠︎", "♣︎"]

            for suit in suits:
                  for i, value in enumerate(values):
                        newDeck.append(Card(value, suit, i))

            return newDeck

class HelperFunction:
      @staticmethod
      def helperMaxInt(points):
            maxInt = [0,points[0]]
            for index, point in enumerate(points[1:]):
                  if int(maxInt[1]) < point:
                        maxInt = [index + 1, point]
            return maxInt


# ディーラークラスの続きです。tabelのgameModeによって、勝利条件を変える関数を作成しましょう。
class Dealer:

      @staticmethod
      def initialTable(amoutOfPeople ,gameMode):
            table = {
                  "players": [],
                  "gameMode": gameMode,
                  "deck": Deck()
            }

            table["deck"].shuffleDeck()

            for person in range(0, amoutOfPeople):
                  personCards = []
                  for cards in range(0, Dealer.initialCards(gameMode)):
                        personCards.append(table["deck"].draw())
                  table["players"].append(personCards)

            return table


      @staticmethod
      def initialCards(gameMode):
            if gameMode == "21":
                  return 2
            if gameMode == "porker":
                  return 5

      # ゲームの種類によって返すものを変えます。
      @staticmethod
      def selectWinnerConditions(table):
            if table["gameMode"] == "21":
                  return Dealer.checkWinner21(table)
            if table["gameMode"] == "porker":
                  return "no game"

      @staticmethod
      def checkWinner21(table):
            playerPoints = []
            cachePoints = {}
            for cards in table["players"]:
                  point = Dealer.additionCards(cards)
                  playerPoints.append(point)
                  if point in cachePoints:
                        cachePoints[point] += 1
                  else:
                        cachePoints[point] = 1

            maxInt = HelperFunction.helperMaxInt(playerPoints)
            print(int(maxInt[1]))
            print(int(maxInt[0]))

            if cachePoints[int(maxInt[1])] == 0:
                  return "no winner"
            elif cachePoints[int(maxInt[1])] > 1:
                  return "draw"
            else:
                  return "winner is " + str(maxInt[0] + 1) + "player"

      @staticmethod
      def additionCards(cards):
            point = 0
            for card in cards:
                  point += card.intValue + 1

            if 21 >= point >= 0:
                  return point
            else:
                  return 0
      
      @staticmethod
      def printTable(table):
            print("This table: ")
            print("gameMode: " + table["gameMode"])
            print("deck: ")
            table["deck"].printCard()
            for i, player in enumerate(table["players"]):
                  print(str(i + 1) + "player's cards: ")
                  for cards in player:
                        print(cards.infoOfCard())


table1 = Dealer.initialTable(3, "21")
Dealer.printTable(table1)
print(Dealer.selectWinnerConditions(table1))