from numpy.random import randint


class Utils:
    def getTarget(self, min: int, max: int) -> int:
        return randint(min, max)

    def getUserInput(self, prompt: str) -> int:
        while True:
            try:
                user_input = int(input(f"{prompt}\n"))
                return user_input
            except ValueError:
                print("Invalid input. Please Enter Valid Input.")

    def checkGuess(self, target: int, guess: int) -> bool:
        return target == guess

    def printMessage(self, message):
        print(message)
