#Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        word_with_guesses = "".join([char if char in guesses else "_" for char in secret_word])
        print(word_with_guesses)

        # Check if the entire word is guessed
        return all(char in guesses for char in secret_word)

    return hangman_closure

# Main execution block
if __name__ == "__main__":
    secret = input("Enter the secret word: ").strip().lower()
    print("\n")

    play = make_hangman(secret)

    print("Let's start the game!")

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if play(guess):
            print("Congratulations! You've guessed the word correctly.")
            break