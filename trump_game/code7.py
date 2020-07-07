import random

class Card:
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            self.intValue = intValue

      def getCardString(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

class Deck:
      def __init__(self):
            self.deck = self.generateDeck()

      def printDeck(self):
            print("Displaying cards...")
            for i in self.deck:
                  print(i.getCardString())

      def shuffleDeck(self):
            deckSize = len(self.deck)
            for i in range(0, deckSize):
                  j = random.randint(0,i)
                  temp = self.deck[i]
                  self.deck[i] = self.deck[j]
                  self.deck[j] = temp

      def draw(self):
            return self.deck.pop()

      @staticmethod
      def generateDeck():
            newDeck = []
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            suits = ["♣", "♦", "♥", "♠"]

            for suit in suits:
                  for i, value in enumerate(values):
                        newDeck.append(Card(value, suit, i))

            return newDeck

class HelperFunction:
      @staticmethod
      def maxInArrayIndex(points):
            maxInt = [0,points[0]]
            for index, point in enumerate(points[1:]):
                  if int(maxInt[1]) < point:
                        maxInt = [index + 1, point]
            return maxInt[0]


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

      # ここから記入してください
      # テーブルの状態を与え、ゲームの種類に応じた勝利条件にを返します・
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
                  point = Dealer.score21Individual(cards)
                  playerPoints.append(point)
                  if point in cachePoints:
                        cachePoints[point] += 1
                  else:
                        cachePoints[point] = 1

            maxIndex = HelperFunction.maxInArrayIndex(playerPoints)

            if cachePoints[playerPoints[maxIndex]] == 0:
                  return "no winner"
            elif cachePoints[playerPoints[maxIndex]] > 1:
                  return "draw"
            else:
                  return "winner is " + str(maxIndex + 1) + "player"

      @staticmethod
      def score21Individual(cards):
            value = 0
            for card in cards:
                  value += card.intValue + 1

            return value if 21 >= value >= 1 else 0
      
      @staticmethod
      def printTable(table):
            print("This table: ")
            print("gameMode: " + table["gameMode"])
            print("deck: ")
            table["deck"].printDeck()
            for i, player in enumerate(table["players"]):
                  print(str(i + 1) + "player's cards: ")
                  for cards in player:
                        print(cards.getCardString())

# テーブルを生成します
table1 = Dealer.initialTable(3, "21")
Dealer.printTable(table1)
# ゲームの種類によって勝利条件を選び、勝者を返します
print(Dealer.selectWinnerConditions(table1))