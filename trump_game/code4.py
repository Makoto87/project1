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

      # ここにカードを1枚引く関数を作成してください。
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

# ディーラーの動きをまとめたクラスDealerを作成します。まずはゲームスタート時にテーブルの状態（各プレイヤーの手札、ゲームの種類、シャッフルされたデッキ）を返す関数を作成しましょう。
# その際、クラスDeck内にカードを1枚引く関数と、クラスDealer内にゲームの種類によって引く手札の数を返す関数が必要になります。先に作成してから、テーブルの状態を返す関数を作成してください。
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

            # print(table)
            return table


      @staticmethod
      def initialCards(gameMode):
            if gameMode == "21":
                  return 2
            if gameMode == "porker":
                  return 5

      # テーブルの中身（各プレイヤーの手札、ゲームの種類、シャッフルされたデッキ）を表示する関数です。ディーラークラス作成後、これを使って正常な処理ができているか確認してください
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