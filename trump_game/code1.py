# トランプアプリを開発していきます。ここでは21を開発しますが、どのトランプゲームでも組み込めるような設計にします。

import random

# まずは1枚分のカードを表すクラスCardを生成しましょう。
# 記号(♣, ♦, ♥, ♠の内1つ)・値（A,2,~,Kの内1つ）・数値（0~12の内1つ）をインスタンス化させるコンストラクタと、それらの情報を返す関数を作成してください

# // ここから記入してください
class Card:
      # インスタンス生成のためのコンストラクタ
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            # intValueは値の大きさになります（例：A=0,K=12）
            self.intValue = intValue

      # インスタンス化されたカード情報を返す関数
      def getCardString(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

# こちらが用意しておきます
# カードを生成し、カード情報を返す関数を使います
print(Card("A","♦︎",1).getCardString())