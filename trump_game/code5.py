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

# ディーラークラスの続きです。各プレイヤーの手札を足して、得点を返す関数を作成しましょう。21を越えると点数は0になることに注意してください。
# また、別のクラスHelperFunctionを作成し、その中に最高得点をとったプレイヤーのインデックスを返す関数を作成してください。

# ここから記入してください
# 最高点をとったプレイヤーのインデックスを返す関数を書きましょう。各プレイヤーの得点が与えられます。
class HelperFunction:
      @staticmethod
      def maxInArrayIndex(points):
            # 0番目がインデックスの値（最大値を持つプレイヤーが誰かわかるようにします）1番目が最大値です
            maxInt = [0,points[0]]
            for index, point in enumerate(points[1:]):
                  if int(maxInt[1]) < point:
                        # 得点が大きかった場合、インデックスの値と最大値を更新します。
                        maxInt = [index + 1, point]
            # インデックスを返します
            return maxInt[0]

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

      # 各プレイヤーの手札の数値を足す関数を作成しましょう。1人のプレイヤーの手札を与えるので、合計を返します。21を越えると点数は0になることに注意してください。
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
# 各プレイヤーの手札を足した数をprintで出力します
print(Dealer.score21Individual(table1["players"][0]))
print(Dealer.score21Individual(table1["players"][1]))
print(Dealer.score21Individual(table1["players"][2]))
# 最も高い得点がどれか確かめます
points = [Dealer.score21Individual(table1["players"][0]), Dealer.score21Individual(table1["players"][1]), Dealer.score21Individual(table1["players"][2])]
print(HelperFunction.helperMaxInt(points))