// トランプアプリを開発していきます。ここでは21を開発しますが、どのトランプゲームでも組み込めるような設計にします。

// まずは1枚分のカードを表すクラスCardを生成しましょう。
// 記号(♣, ♦, ♥, ♠の内1つ)・値（A,2,~,Kの内1つ）・数値（0~12の内1つ）をインスタンス化させるコンストラクタと、それらの情報を返す関数を作成してください

// ここから記入してください
class Card {
      // インスタンス生成のためのコンストラクタ
      constructor(suit, value, intValue) {
            this.suit = suit;
            this.value = value;
            // intValueは値の大きさになります（例：A=0,K=12）
            this.intValue = intValue
      }
      // インスタンス化されたカード情報を返す関数
      getCardString() {
            return this.suit + this.value + "(" + this.intValue + ")";
      }
}

// こちらが用意しておきます
// 新しくカードを作成し、カード情報を返す関数を使用します
let card1 = new Card("♦︎","A",1)
console.log(card1.getCardString())