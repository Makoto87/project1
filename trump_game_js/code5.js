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

// ディーラークラスの続きです。各プレイヤーの手札を足して、得点を返す関数を作成しましょう。21を越えると点数は0になることに注意してください。
// また、別のクラスHelperFunctionを作成し、その中に複数の得点から最も高いものを返す関数を作成してください。

// 最も高い得点を選ぶ関数を書きましょう。インデックスと得点を配列にまとめて返してください。各プレイヤーの得点が与えられます。
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

class Dealer {

      static initialTable(amountOfPlayers, gameMode) {
            let table = {
                  "players":[],
                  "gameMode": gameMode,
                  "deck": []
            }

            table["deck"] = new Deck(Deck.createDeck());
            table["deck"].shuffleDeck();

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

      static initialCards(gameMode) {
            if (gameMode == "21") { return 2;}
            if (gameMode == "porker") { return 5;}
      }

      // 各プレイヤーの手札の数値を足す関数を作成しましょう。1人のプレイヤーの手札を与えるので、合計を返します。21を越えると点数は0になることに注意してください。
      static additionCards(cards) {
            let point = 0;
            for (let i = 0; i < cards.length; i++) {
                  point += cards[i].intValue;
            }
            if (point > 21) { point = 0; }
            return point;
      }
}

console.log(Dealer.additionCards([new Card("♦︎","A", 1),new Card("♦︎","J", 11)]));
console.log(HelperFunction.helperMaxInt([12,3,21]));