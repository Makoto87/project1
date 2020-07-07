class Card {
      constructor(suit, value, intValue) {
            this.suit = suit;
            this.value = value;
            this.intValue = intValue
      }

      getCardString() {
            return this.suit + this.value + "(" + this.intValue + ")";
      }
}

// デッキを表すクラスDeckの続きです。次は、デッキをシャッフルする関数を作成しましょう。また、デッキにあるカードを全て表示する関数を作成し、シャッフルする前と後を比べてみましょう。

class Deck {
      constructor() {
            this.deck = Deck.generateDeck();
      }

      // ここから記入してください
      // シャッフルする関数はtwo pointerを活用します。for文で一つ一つのカードをランダムに入れ替える処理を書きましょう。
      shuffleDeck() {
            for (let i = 0; i < this.deck.length; i++) {
                  // ランダムに得た数値をインデックスとし、two pointerで入れ替えます。
                  let j = Math.floor(Math.random() * (i + 1));
                  let temp = this.deck[i];
                  this.deck[i] = this.deck[j];
                  this.deck[j] = temp;
            }
      }

      // デッキにあるカードを全て表示する関数は、デッキの一つ一つ内のカードを、クラスCard内にあるカードを表示する関数を使って表示します。
      printDeck() {
            console.log("Displaying cards...")
            for (let i = 0; i < this.deck.length; i++) {
                  console.log(this.deck[i].getCardString());
            }
      }

      static generateDeck() {
            let newDeck = [];
            const suits = ["♣", "♦", "♥", "♠"];
            const values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

            for (let i = 0; i < suits.length; i++) {
                  for (let j = 0; j < values.length; j++) {
                        newDeck.push(new Card(suits[i], values[j], j));
                  }
            }

            return newDeck;
      }
}

// 新しくデッキを生成します
let deck1 = new Deck();
console.log(deck1)
console.log("\n");
// デッキをシャッフルします
deck1.shuffleDeck();
console.log(deck1);
console.log("\n");
// シャッフルする前のデッキと後のデッキを表示しましょう
let deck2 = new Deck();
deck2.printDeck();
console.log("\n");
deck2.shuffleDeck();
deck2.printDeck();