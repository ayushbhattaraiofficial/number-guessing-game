import { Utils } from "./utils.js";
export class NumberGuessingGame {
    constructor(number_range, lives) {
        this.number_range = number_range;
        this.lives = lives;
        this.ut = new Utils();
        this.target = this.ut.getTarget(number_range);
    }

    play() {
        while (this.lives > 0) {
            alert(`You have ${this.lives} lives left`);
            var guess = this.ut.getUserInput();
            if (this.ut.checkGuess(this.target, guess)) {
                alert("YOU WIN!!!");
                break;
            } else {
                this.lives -= 1;
                let hint;
                if (guess > this.target) {
                    hint = "Guess lower";
                } else {
                    hint = "Guess higher";
                }
                alert(`${hint}`);
            }
        }
        if (self.lives <= 0) {
            alert("You have run out of lives");
            alert(`The correct answer was ${this.target}`);
        }
    }
}
