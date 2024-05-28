def get_secret_number(i):
    while True:
        secret = input(f"Player {i}, enter your secret multi-digit number: ")
        if secret.isdigit():
            return secret
        else:
            print("Invalid input. Please enter a valid multi-digit number.")

def get_guess(attempt_number):
    while True:
        guess = input(f"Attempt {attempt_number}: Enter your guess: ")
        if guess.isdigit():
            return guess
        else:
            print("Invalid input. Please enter a valid multi-digit number.")

def provide_feedback(secret, guess):
    correct_positions = sum(s == g for s, g in zip(secret, guess))
    correct_digits = sum(min(secret.count(d), guess.count(d)) for d in set(secret))
    return correct_positions, correct_digits

def play_round(secret_number):
    attempts = 0
    while True:
        attempts += 1
        guess = get_guess(attempts)
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return attempts
        else:
            correct_positions, correct_digits = provide_feedback(secret_number, guess)
            print(f"Digits in the correct position: {correct_positions}")
            print(f"Correct digits (including misplaced): {correct_digits}")

def mastermind_game():
    print("Player 1's turn to set the number.")
    secret_number_1 = get_secret_number(1)
    print("\n" * 50)  # Clear the screen to hide the secret number
    print("Player 2, it's your turn to guess the number.")
    attempts_player_2 = play_round(secret_number_1)

    print("Player 2's turn to set the number.")
    secret_number_2 = get_secret_number(2)
    print("\n" * 50)  # Clear the screen to hide the secret number
    print("Player 1, it's your turn to guess the number.")
    attempts_player_1 = play_round(secret_number_2)

    if attempts_player_1 < attempts_player_2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_player_2 < attempts_player_1:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie! Both players are Masterminds!")

if __name__ == "__main__":
    mastermind_game()
