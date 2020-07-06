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

// ディーラークラスの続きです。tabelのgameModeによって、勝利条件を変える関数を作成しましょう。

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

      static additionCards(cards) {
            let point = 0;
            for (let i = 0; i < cards.length; i++) {
                  point += cards[i].intValue + 1;
            }
            if (point > 21) { point = 0; }
            return point;
      }

      // テーブルの状態を与え、ゲームの種類に応じた勝利条件にを返します・
      static selectGame(table) {
            if (table["gameMode"] == "21") { return Dealer.winnerOf21(table); }
      }

      static winnerOf21(table) {
            let points = [];
            let cache = [];
            for (let i = 0; i < table["players"].length; i++) {
                  // なぜか末尾に0を入れないとエラーになるので、直します。
                  let player = table["players"][i][0];
                  let point = Dealer.additionCards(player);
                  if (cache[point] >= 1) {
                        cache[point] += 1;
                  } else {
                        cache[point] = 1;
                  }
                  points.push(point);
            }

            let maxInt = HelperFunction.helperMaxInt(points);

            if (cache[maxInt[1]] > 1) {
                  return "draw";
            } else if (maxInt[1] == 0) {
                  return "no winner";
            } else {
                  return "winner is " + (maxInt[0] + 1) + " player";
            }

      }
}

let table1 = Dealer.initialTable(3, "21");
console.log(table1["players"][0]);
console.log(table1["players"][1]);
console.log(table1["players"][2]);
console.log(Dealer.selectGame(table1));