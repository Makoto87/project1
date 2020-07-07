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
            for i in reversed(range(0, deckSize)):
                  j = random.randint(0,i)
                  temp = self.deck[i]
                  self.deck[i] = self.deck[j]
                  self.deck[j] = temp

      # デッキからカードを1枚引く関数を作成しましょう。配列の末尾を取得するとともに、削除する処理を入れます。
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


# ディーラーの動きをまとめたクラスDealerを作成します。まずはゲームスタート時にテーブルの状態（各プレイヤーの手札、ゲームの種類、シャッフルされたデッキ）を返す関数を作成しましょう。
# その際、クラスDeck内にカードを1枚引く関数と、クラスDealer内にゲームの種類によって引く手札の数を返す関数が必要になります。先に作成してから、テーブルの状態を返す関数を作成してください。

# ここから記入してください
# インスタンスを作成する必要がないので、全てstaticメソッドにしましょう
class Dealer:

      # テーブルの状態を表す関数です。人数とゲームの種類が与えられ、デッキのシャッフルと各プレイヤーの手札を作成する処理を行い、テーブルの状態を返します
      @staticmethod
      def initialTable(amoutOfPeople ,gameMode):
            # 連想配列でテーブルの状態を作成します。
            table = {
                  "players": [],
                  "gameMode": gameMode,
                  "deck": Deck()
            }

            # デッキをシャッフルします
            table["deck"].shuffleDeck()

            # デッキからカードを引いていき、各プレイヤーの手札をtableにセットします。
            for person in range(0, amoutOfPeople):
                  personCards = []
                  for cards in range(0, Dealer.initialCards(gameMode)):
                        personCards.append(table["deck"].draw())
                  table["players"].append(personCards)

            return table


      # ゲームの種類が与えられるので、種類によって何枚カードを引くか、数字を返す関数を作成しましょう。
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
            table["deck"].printDeck()
            for i, player in enumerate(table["players"]):
                  print(str(i + 1) + "player's cards: ")
                  for cards in player:
                        print(cards.getCardString())

# テーブルを生成し、どのような状態か出力します
table1 = Dealer.initialTable(3, "21")
Dealer.printTable(table1)