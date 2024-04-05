export class Utils {
    getTarget(number_range) {
        var min = 10 ** (number_range - 1);
        var max = 10 ** number_range - 1;
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    checkGuess(target, guess) {
        return target === guess;
    }

    getUserInput(){
        while (true) {
            try {
                var user_input = parseInt(prompt("Enter the guess"));
                return user_input;
            } catch (TypeError) {
                alert("Please enter a valid number");
            }
        }
    }
}
