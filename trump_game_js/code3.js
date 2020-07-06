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

// デッキを表すクラスDeckの続きです。次は、デッキをシャッフルする関数を作成しましょう。また、デッキにあるカードを全て表示する関数を作成し、シャッフルする前と後を比べてみましょう。

class Deck {
      constructor(deck) {
            this.deck = deck;
      }

      // シャッフルする関数はtwo pointerを活用します。for文で一つ一つのカードをランダムに入れ替える処理を書きましょう。
      shuffleDeck() {
            let newDeck = [];
            for (let i = 0; i < this.deck.length; i++) {
                  newDeck.push(this.deck[i]);
                  // console.log(this.deck[i]);
                  let j = Math.floor(Math.random() * (i + 1));
                  let temp = newDeck[i];
                  newDeck[i] = newDeck[j];
                  newDeck[j] = temp;
            }

            this.deck = newDeck;
      }

      // デッキにあるカードを全て表示する関数は、デッキの一つ一つ内のカードを、クラスCard内にあるカードを表示する関数を使って表示します。
      pringDeck() {
            for (let i = 0; i < this.deck.length; i++) {
                  console.log(this.deck[i].infoOfCard());
            }
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
console.log("\n");
// デッキをシャッフルします
deck1.shuffleDeck();
console.log(deck1);
console.log("\n");
// シャッフルする前のデッキと後のデッキを表示しましょう
let deck2 = new Deck(Deck.createDeck());
deck2.pringDeck();
console.log("\n");
deck2.shuffleDeck();
deck2.pringDeck();