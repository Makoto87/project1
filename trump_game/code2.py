import random

class Card:
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            self.intValue = intValue

      def infoOfCard(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

# 次にデッキを表すクラスDeckを生成しましょう
# クラス内にトランプのカード全種類を生成させる関数を作成しましょう。その後、その関数を使って、トランプカードが全種類入ったデッキをインスタンス化させる関数を作成しましょう
class Deck:
      def __init__(self):
            self.deck = self.generateDeck()

      @staticmethod
      def generateDeck():
            newDeck = []
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            suits = ["♦︎", "♡", "♠︎", "♣︎"]

            for suit in suits:
                  for i, value in enumerate(values):
                        # 入るカードが何かを確認します
                        print(Card(value, suit, i).infoOfCard())
                        newDeck.append(Card(value, suit, i))

            return newDeck

Deck()