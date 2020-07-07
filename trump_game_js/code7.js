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

// ディーラークラスの続きです。tabelのgameModeによって、勝利条件を変える関数を作成しましょう。

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
      // テーブルの状態を与え、ゲームの種類に応じた勝利条件にを返します・
      static checkWinner(table) {
            if (table["gameMode"] == "21") {
                  return Dealer.checkWinner21(table);
            } else {
                  return "no game"
            }
      }

      static checkWinner21(table) {
            let playerStats = [];
            let cachedScores = [];
            for (let i = 0; i < table["players"].length; i++) {
                  let player = table["players"][i];
                  let point = Dealer.score21Individual(player);
                  if (cachedScores[point] >= 1) {
                        cachedScores[point] += 1;
                  } else {
                        cachedScores[point] = 1;
                  }
                  playerStats.push(point);
            }

            let maxInt = HelperFunction.helperMaxInt(playerStats);

            if (maxInt[1] == 0) {
                  return "No winners..";
            } else if (cache[maxInt[1]] > 1) {
                  return "It is a draw ";
            } else {
                  return "player " + (maxInt[0] + 1) + " is the winner";
            }

      }
}

// 勝利条件の記述があるゲームの場合
let table1 = Dealer.startGame(3, "21");
console.log(Dealer.checkWinner(table1));
// 勝利条件の記述がないゲームの場合
let table2 = Dealer.startGame(3, "porker");
console.log(Dealer.checkWinner(table2));