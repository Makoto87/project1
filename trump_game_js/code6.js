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
      constructor(deck) {
            this.deck = deck;
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

class HelperFunction {
      static helperMaxInt(points) {
            let maxInt = [0,0];
            for (let i = 0; i < points.length; i++) {
                  if (maxInt[1] < points[i]) { 
                        maxInt[1] = points[i];
                        maxInt[0] = i;
                  }
            }
            return maxInt;
      }
}

// ディーラークラスの続きです。21において誰が勝利したかを関数で表します。各プレイヤーの手札を比べて、誰が勝利したかを返す関数を作成してください。前回まで作った関数を活用し、作成してください。

class Dealer {

      static startGame(amountOfPlayers, gameMode) {
            let table = {
                  "players":[],
                  "gameMode": gameMode,
                  "deck": new Deck(Deck.generateDeck())
            }

            table["deck"].shuffleDeck();

            for (let i = 0; i < amountOfPlayers; i++) {
                  let playerCard = [];
                  for (let j = 0; j < Dealer.initialCards(gameMode); j++) {
                        playerCard.push(table["deck"].draw());
                  }
                  table["players"].push(playerCard);
            }

            return table;
      }

      static initialCards(gameMode) {
            if (gameMode == "21") { return 2;}
            if (gameMode == "porker") { return 5;}
      }

      static score21Individual(cards) {
            let value = 0;
            for (let i = 0; i < cards.length; i++) {
                  value += cards[i].intValue + 1;
            }
            if (value > 21) { value = 0; }
            return value;
      }

      // ここから記入してください
      // 21で誰が勝つかを返す関数を作成します。テーブルの状態を引数とします。
      static winnerOf21(table) {
            // 各プレイヤーの手札を足し、得点を求めます
            // キャッシュを活用して、同じ数値が出た人がいないかチェックします。
            let points = [];
            let cache = [];
            for (let i = 0; i < table["players"].length; i++) {
                  let player = table["players"][i];
                  // 各プレイヤーの得点を配列にまとめます
                  let point = Dealer.score21Individual(player);
                  points.push(point);
                  // キャッシュによって得点が重複するプレイヤーがいないか記録しておきます
                  if (cache[point] >= 1) {
                        cache[point] += 1;
                  } else {
                        cache[point] = 1;
                  }
            }
            // 最大の数値を得ます
            let maxInt = HelperFunction.helperMaxInt(points);

            // 最大値によって返す結果を変更します。条件式の書き方次第で、no winnerも全てdrawになる可能性があります。書く順番に気をつけましょう。
            if (maxInt[1] == 0) {
                  return "No winners..";
            } else if (cache[maxInt[1]] > 1) {
                  return "It is a draw ";
            } else {
                  return "player " + (maxInt[0] + 1) + " is the winner";
            }

      }
}

// テーブルを生成します
let table1 = Dealer.startGame(3, "21");
// 各プレイヤーの手札を見ます
console.log(table1["players"][0]);
console.log(table1["players"][1]);
console.log(table1["players"][2]);
// 誰が勝利するか確認します
console.log(Dealer.winnerOf21(table1));

// 各勝利条件が果たされているか見ます
// drawのtable
let table2 = {
      "players":[[new Card("♦︎", "9", 9), new Card("♦︎", "9", 9)], [new Card("♦︎", "9", 9), new Card("♦︎", "9", 9)]],
      "gameMode": "21",
      "deck": new Deck
}
// no winnerのtable
let table3 = {
      "players":[[new Card("♦︎", "10", 10), new Card("♦︎", "10", 10)], [new Card("♦︎", "10", 10), new Card("♦︎", "10", 10)]],
      "gameMode": "21",
      "deck": new Deck
}
console.log(Dealer.winnerOf21(table2));
console.log(Dealer.winnerOf21(table3));