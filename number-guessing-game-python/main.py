from game.game import NumberGuessingGame


def main():
    name = str(input("Enter player name\n"))
    print(f"Hello! {name}")
    number_range = int(
        input("Enter the number of digits you would like to play\n")
    )
    level = str(input("Enter E, M or H for Easy, Medium or Hard mode\n"))
    play_game = NumberGuessingGame(number_range, level).play()


if __name__ == "__main__":
    main()
