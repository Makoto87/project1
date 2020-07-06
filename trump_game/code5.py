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

# ディーラークラスの続きです。各プレイヤーの手札を足して、得点を返す関数を作成しましょう。21を越えると点数は0になることに注意してください。
# また、別のクラスHelperFunctionを作成し、その中に複数の得点から最も高いものを返す関数を作成してください。

# 最も高い得点を選ぶ関数を書きましょう。インデックスと得点を配列にまとめて返してください。
class HelperFunction:
      @staticmethod
      def helperMaxInt(points):
            maxInt = [0,points[0]]
            for index, point in enumerate(points[1:]):
                  if int(maxInt[1]) < point:
                        maxInt = [index + 1, point]
            return maxInt

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

      # プレイヤーの手札を足す関数です
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
# 各プレイヤーの得点をprintで出力しましょう
print(Dealer.additionCards(table1["players"][0]))
print(Dealer.additionCards(table1["players"][1]))
print(Dealer.additionCards(table1["players"][2]))
# 最も高い得点がどれか確かめましょう
points = [Dealer.additionCards(table1["players"][0]), Dealer.additionCards(table1["players"][1]), Dealer.additionCards(table1["players"][2])]
print(HelperFunction.helperMaxInt(points))