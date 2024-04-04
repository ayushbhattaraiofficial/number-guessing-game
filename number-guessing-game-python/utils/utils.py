from numpy.random import randint


def getTarget(min: int, max: int) -> int:
    return randint(min, max)


def getUserInput(prompt: str) -> int:
    while True:
        try:
            user_input = int(input(f"{prompt}\n"))
            return user_input
        except ValueError:
            print("Invalid input. Please Enter Valid Input")


def checkGuess(target: int, guess: int) -> bool:
    return target == guess


def printMessage(message):
    print(message)
