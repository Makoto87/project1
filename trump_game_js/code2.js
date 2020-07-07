// 次にデッキを表すクラスDeckを生成しましょう
// クラスCardを活用し、クラスDeckにトランプのカード全種類を生成させる関数を作成しましょう。その後、その関数を使って、デッキをインスタンス化させるコンストラクタを作成しましょう

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

// ここから記入してください
class Deck {
      // コンストラクタ
      constructor() {
            this.deck = Deck.generateDeck();
      }

      // デッキを生み出す関数を作成します。staticメソッドを使います。ここではインスタンス無しでも使える関数と考えていただければ問題ありません。
      // 全記号・全ての値を用意し、for文で一つずつカードを生成します。
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

// こちらが用意しておきます
// 新しくデッキを作成し、コンソール上に出力します
let deck1 = new Deck();
console.log(deck1)