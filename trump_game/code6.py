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


# ディーラークラスの続きです。21において誰が勝利したかを関数で表します。各プレイヤーの手札を比べて、誰が勝利したかを返す関数を作成してください。前回まで作った関数を活用し、作成してください。
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
      # 21で誰が勝つかを返す関数を作成します。テーブルの状態を引数とします。
      @staticmethod
      def checkWinner21(table):
            # 各プレイヤーの手札を足し、得点を求めます
            # キャッシュを活用して、同じ数値が出た人がいないかチェックします。
            playerPoints = []
            cachePoints = {}
            for cards in table["players"]:
                  # 各プレイヤーの得点を配列にまとめます
                  point = Dealer.score21Individual(cards)
                  playerPoints.append(point)
                  # キャッシュによって得点が重複するプレイヤーがいないか記録しておきます
                  if point in cachePoints:
                        cachePoints[point] += 1
                  else:
                        cachePoints[point] = 1

            # 各プレイヤーの中で最大の点数を探す
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
# 誰が勝ったか確認します
print(Dealer.checkWinner21(table1))