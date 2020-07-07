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

// ディーラークラスの続きです。各プレイヤーの手札を足して、得点を返す関数を作成しましょう。21を越えると点数は0になることに注意してください。
// また、別のクラスHelperFunctionsを作成し、その中に複数の得点から最も高いものを返す関数を作成してください。

// ここから記入してください
// 最も高い得点を選ぶ関数を書きましょう。インデックスと得点を配列にまとめて返してください。各プレイヤーの得点が与えられます。
class HelperFunctions {
      static maxInArrayIndex(points) {
            // 0番目がインデックスの値（最大値を持つプレイヤーが誰かわかるようにします）1番目が最大値です
            let maxInt = [0,0];
            for (let i = 0; i < points.length; i++) {
                  if (maxInt[1] < points[i]) { 
                        // 得点が大きかった場合、インデックスの値と最大値を更新します。
                        maxInt[1] = points[i];
                        maxInt[0] = i;
                  }
            }
            return maxInt;
      }
}

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

      // 各プレイヤーの手札の数値を足す関数を作成しましょう。1人のプレイヤーの手札を与えるので、合計を返します。21を越えると点数は0になることに注意してください。
      static score21Individual(cards) {
            let value = 0;
            for (let i = 0; i < cards.length; i++) {
                  // intValueは0番目から始まるので、1を足します。
                  value += cards[i].intValue + 1;
            }
            if (value > 21) { value = 0; }
            return value;
      }
}

// 2つのカードを足した時の数値を返します
console.log(Dealer.score21Individual([new Card("♦︎","A", 1),new Card("♦︎","J", 11)]));
// 最大値のインデックスと数値を返します
console.log(HelperFunctions.maxInArrayIndex([12,3,21]));