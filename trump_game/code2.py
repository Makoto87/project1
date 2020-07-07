import random

class Card:
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            self.intValue = intValue

      def getCardString(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

# 次にデッキを表すクラスDeckを生成しましょう
# クラスCardを活用し、クラスDeckにトランプのカード全種類を生成させる関数を作成しましょう。その後、その関数を使って、デッキをインスタンス化させるコンストラクタを作成しましょう

# ここから記入してください
class Deck:
      # コンストラクタ
      def __init__(self):
            self.deck = self.generateDeck()

      # デッキを生み出す関数を作成します。staticメソッドを使います。ここではインスタンス無しでも使える関数と考えていただければ問題ありません。
      # 全記号・全ての値を用意し、for文で一つずつカードを生成します。
      @staticmethod
      def generateDeck():
            newDeck = []
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            suits = ["♣", "♦", "♥", "♠"]

            for suit in suits:
                  for i, value in enumerate(values):
                        # 入るカードが何かを確認します
                        print(Card(value, suit, i).getCardString())
                        newDeck.append(Card(value, suit, i))

            return newDeck

# デッキを生成します
deck1 = Deck()
print(deck1)