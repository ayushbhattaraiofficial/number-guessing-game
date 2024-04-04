from utils.utils import checkGuess, getTarget, getUserInput, printMessage


class NumberGuessingGame:
    def __init__(self, number_range: int, mode: str):
        target = getTarget(10 ** (number_range - 1), (10**number_range) - 1)
        self.target = target
        health = {"E": 6, "M": 4, "H": 3}
        self.lives = health.get(mode.upper(), 6)

    def play(self):
        while self.lives > 0:
            printMessage(f"You have {self.lives} lives left")
            guess = getUserInput("Your Guess")
            if checkGuess(self.target, guess):
                printMessage("You Win!!!")
                break
            else:
                self.lives -= 1
                hint = "Guess lower" if guess > self.target else "Guess higher"
                printMessage(hint)
        if self.lives <= 0:
            printMessage("You have run out of lives")
            printMessage(f"The correct answer was {self.target}")
