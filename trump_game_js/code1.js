// トランプアプリを開発していきます。ここでは21を開発しますが、どのトランプゲームでも組み込めるような設計にします。

// まずは1枚分のカードを表すクラスCardを生成しましょう。
// 記号・値（A~K）・数値（1~13）をインスタンス化させる関数と、それらの情報を返す関数を作成してください
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

let card1 = new Card("♦︎","A",1)
console.log(card1.infoOfCard())