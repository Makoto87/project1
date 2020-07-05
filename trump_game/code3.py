import random

class Card:
      def __init__(self, value, suit, intValue) :
            self.value = value
            self.suit = suit
            self.intValue = intValue

      def infoOfCard(self):
            return self.suit + self.value + "(" + str(self.intValue) + ")"

# デッキを表すクラスDeckの続きです。次は、デッキをシャッフルする関数を作成しましょう。また、デッキにあるカードを全て表示する関数を作成し、シャッフルする前と後を比べてみましょう。
class Deck:
      def __init__(self):
            self.deck = self.generateDeck()

      # ここから記入してください
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

      @staticmethod
      def generateDeck():
            newDeck = []
            values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            suits = ["♦︎", "♡", "♠︎", "♣︎"]

            for suit in suits:
                  for i, value in enumerate(values):
                        newDeck.append(Card(value, suit, i))

            return newDeck

deck1 = Deck()
deck1.printCard()
deck1.shuffleDeck()
deck1.printCard()