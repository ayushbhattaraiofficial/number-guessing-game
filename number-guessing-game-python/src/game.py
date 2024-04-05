from utils import Utils


class NumberGuessingGame:
    def __init__(self, number_range: int, mode: str):
        self.ut = Utils()
        target = self.ut.getTarget(
            10 ** (number_range - 1), (10**number_range) - 1
        )
        self.target = target
        health = {"E": 6, "M": 4, "H": 3}
        self.lives = health.get(mode.upper(), 6)

    def play(self):
        while self.lives > 0:
            self.ut.printMessage(f"You have {self.lives} lives left")
            guess = self.ut.getUserInput("Your  Guess")
            if self.ut.checkGuess(self.target, guess):
                self.ut.printMessage("You Win!!!")
                break
            else:
                self.lives -= 1
                hint = "Guess lower" if guess > self.target else "Guess higher"
                self.ut.printMessage(hint)
        if self.lives <= 0:
            self.ut.printMessage("You have run out of lives.")
            self.ut.printMessage(f"The correct answer was {self.target}")
