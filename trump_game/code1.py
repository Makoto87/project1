# トランプアプリを開発していきます。ここでは21を開発しますが、どのトランプゲームでも組み込めるような設計にします。

import random

# まずは1枚分のカードを表すクラスCardを生成しましょう。
# 記号・値（A~K）・数値（1~13）をインスタンス化させる関数と、それらの情報を返す関数を作成してください
class Card:
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            self.intValue = intValue

      def infoOfCard(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

print(Card("A","♦︎",1).infoOfCard())