import random

class Card:
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            self.intValue = intValue

      def getCardString(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

# デッキを表すクラスDeckの続きです。次は、デッキをシャッフルする関数を作成しましょう。また、デッキにあるカードを全て表示する関数を作成し、シャッフルする前と後を比べてみましょう。
class Deck:
      def __init__(self):
            self.deck = self.generateDeck()

      # ここから記入してください
      # シャッフルする関数はtwo pointerを活用します。for文で一つ一つのカードをランダムに入れ替える処理を書きましょう。
      def shuffleDeck(self):
            # デッキにあるカードの数を取得します。
            deckSize = len(self.deck)
            # デッキにあるカードの数分for文で処理します
            for i in range(0, deckSize):
                  # ランダムに得た数値をインデックスとし、two pointerで入れ替えます。
                  j = random.randint(0,i)
                  temp = self.deck[i]
                  self.deck[i] = self.deck[j]
                  self.deck[j] = temp

      # デッキにあるカードを全て表示する関数は、デッキの一つ一つ内のカードを、クラスCard内にあるカードを表示する関数を使って表示します。
      def printDeck(self):
            print("Displaying cards...")
            for i in self.deck:
                  print(i.getCardString())

      @staticmethod
      def generateDeck():
            newDeck = []
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            suits = ["♣", "♦", "♥", "♠"]

            for suit in suits:
                  for i, value in enumerate(values):
                        newDeck.append(Card(value, suit, i))

            return newDeck

# デッキを生成し、入っているカードを表示します
deck1 = Deck()
deck1.printDeck()
# デッキをシャッフルし、入っているカードを表示します
deck1.shuffleDeck()
deck1.printDeck()