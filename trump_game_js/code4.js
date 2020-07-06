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

      printDeck() {
            for (let i = 0; i < this.deck.length; i++) {
                  console.log(this.deck[i].infoOfCard());
            }
      }

      // デッキからカードを1枚引く関数を作成しましょう。配列の末尾を取得するとともに、削除する処理を入れます。
      draw() {
            return this.deck.pop()
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

// ディーラーの動きをまとめたクラスDealerを作成します。まずはゲームスタート時にテーブルの状態（各プレイヤーの手札、ゲームの種類、シャッフルされたデッキ）を返す関数を作成しましょう。
// その際、クラスDeck内にカードを1枚引く関数と、クラスDealer内にゲームの種類によって引く手札の数を返す関数が必要になります。先に作成してから、テーブルの状態を返す関数を作成してください。

class Dealer {

      // テーブルの中身（各プレイヤーの手札、ゲームの種類、シャッフルされたデッキ）を表示する関数です。
      // 人数とゲームの種類を入力し、テーブルの状態を返します
      static initialTable(amountOfPlayers, gameMode) {
            // 連想配列でテーブルの状態を作成します。
            let table = {
                  "players":[],
                  "gameMode": gameMode,
                  "deck": []
            }

            // クラスDeckを使って、生み出したデッキをtableにセットし、シャッフルします。
            table["deck"] = new Deck(Deck.createDeck());
            table["deck"].shuffleDeck();

            // デッキからカードを引いていき、各プレイヤーの手札をtableにセットします。
            for (let i = 0; i < amountOfPlayers; i++) {
                  let playerCard = [];
                  for (let j = 0; j < Dealer.initialCards(gameMode); j++) {
                        let cards = [];
                        cards.push(table["deck"].draw());
                        playerCard.push(cards);
                  }
                  table["players"].push(playerCard);
            }

            return table;
      }

      // ゲームの種類によって何枚カードを引くか、数字を返す関数を作成しましょう。
      static initialCards(gameMode) {
            if (gameMode == "21") { return 2;}
            if (gameMode == "porker") { return 5;}
      }
}

let table1 = Dealer.initialTable(3, "21");
console.log(table1);
console.log(table1["players"][0][0]);
console.log(table1["players"][2][0]);
console.log(table1["deck"].printDeck());