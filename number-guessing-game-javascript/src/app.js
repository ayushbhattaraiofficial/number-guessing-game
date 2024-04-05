import { NumberGuessingGame } from "./game.js";
function app() {
    var user_name = prompt("Enter username");
    alert(`Welcome to the number guessing game ${user_name}`);
    var number_range = parseInt(
        prompt("Enter the number of digits you would like to play")
    );
    let lives;
    while (true) {
        var difficulty = prompt(`
        Select Difficulty:
        E for 6 lives,
        M for 4 lives,
        H for 3 lives.
        `);
        if (difficulty.toUpperCase() === "E") {
            lives = 6;
            break;
        } else if (difficulty.toUpperCase() === "M") {
            lives = 4;
            break;
        } else if (difficulty.toUpperCase() === "H") {
            lives = 3;
            break;
        }
    }
    alert(`lives ${lives}`);
    const PLAY_GAME = new NumberGuessingGame(number_range, lives);
    PLAY_GAME.play();
}
app();
