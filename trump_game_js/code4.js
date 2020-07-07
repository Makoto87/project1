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

class Deck {
      constructor() {
            this.deck = Deck.generateDeck();
      }

      shuffleDeck() {
            for (let i = 0; i < this.deck.length; i++) {
                  let j = Math.floor(Math.random() * (i + 1));
                  let temp = this.deck[i];
                  this.deck[i] = this.deck[j];
                  this.deck[j] = temp;
            }
      }

      printDeck() {
            console.log("Displaying cards...")
            for (let i = 0; i < this.deck.length; i++) {
                  console.log(this.deck[i].getCardString());
            }
      }

      // デッキからカードを1枚引く関数を作成しましょう。配列の末尾を取得するとともに、削除する処理を入れます。
      draw() {
            return this.deck.pop()
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

// ディーラーの動きをまとめたクラスDealerを作成します。まずはゲームスタート時にテーブルの状態（各プレイヤーの手札、ゲームの種類、シャッフルされたデッキ）を返す関数を作成しましょう。
// その際、クラスDeck内にカードを1枚引く関数と、クラスDealer内にゲームの種類によって引く手札の数を返す関数が必要になります。先に作成してから、テーブルの状態を返す関数を作成してください。

// ここから記入してください
// インスタンスを作成する必要がないので、全てstaticメソッドにしましょう
class Dealer {

      // テーブルの状態を表す関数です。人数とゲームの種類が与えられ、デッキのシャッフルと各プレイヤーの手札を作成する処理を行い、テーブルの状態を返します
      static startGame(amountOfPlayers, gameMode) {
            // 連想配列でテーブルの状態を作成します。
            let table = {
                  "players":[],
                  "gameMode": gameMode,
                  "deck": new Deck()
            }

            // デッキをシャッフルします
            table["deck"].shuffleDeck();

            // デッキからカードを引いていき、各プレイヤーの手札をtableにセットします。
            for (let i = 0; i < amountOfPlayers; i++) {
                  let playerCard = [];
                  for (let j = 0; j < Dealer.initialCards(gameMode); j++) {
                        playerCard.push(table["deck"].draw());
                  }
                  table["players"].push(playerCard);
            }

            return table;
      }

      // ゲームの種類が与えられるので、種類によって何枚カードを引くか、数字を返す関数を作成しましょう。
      static initialCards(gameMode) {
            if (gameMode == "21") { return 2;}
            if (gameMode == "porker") { return 5;}
      }

      // テーブルの状態を表す関数を用意しました。これを使って、テーブルの状態を確認しましょう
      static printTableInformation(table) {
            console.log("Amount of players: " + table["players"].length + "... Game mode: " + table["gameMode"] + ". At this table: ");

            for (let i = 0; i < table["players"].length; i++) {
                  console.log("Player " + (i + 1) + " hand is: ");
                  for(let j = 0; j < table["players"][i].length; j++) {
                        console.log(table["players"][i][j].getCardString());
                  }
            }
      }

      
}

// 新しくデッキを生成します
let table1 = Dealer.startGame(3, "21");
// 用意した関数を使って、テーブルの状態を見ましょう
Dealer.printTableInformation(table1);