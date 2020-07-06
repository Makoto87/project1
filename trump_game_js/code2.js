// 次にデッキを表すクラスDeckを生成しましょう
// 前回作成したカードを生み出す関数を活用し、クラス内にトランプのカード全種類を生成させる関数を作成しましょう。その後、その関数を使って、トランプカードが全種類入ったデッキをインスタンス化させる関数を作成しましょう

class Card {
      constructor(suit, value, intValue) {
            this.suit = suit;
            this.value = value;
            this.intValue = intValue
      }

      infoOfCard() {
            return this.suit + this.value + "(" + this.intValue + ")";
      }
}

class Deck {
      constructor(deck) {
            this.deck = deck;
      }

      static createDeck() {
            let newDeck = [];
            const suits = ["♦︎", "♡", "♠︎", "♣︎"];
            const values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

            for (let i = 0; i < suits.length; i++) {
                  for (let j = 0; j < values.length; j++) {
                        newDeck.push(new Card(suits[i], values[j], j));
                  }
            }

            return newDeck;
      }
}

let deck1 = new Deck(Deck.createDeck());
console.log(deck1)