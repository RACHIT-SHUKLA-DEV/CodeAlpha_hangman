import random

def hangman():
    # Predefined list of 5 words
    words = ["python", "developer", "hangman", "program", "code"]
    word = random.choice(words)  # Randomly choose a word
    guessed_letters = []
    attempts = 6  # Maximum wrong guesses allowed

    print(" Welcome to the Hangman Game!")
    print("You have 6 attempts to guess the word.\n")

    # Game loop
    while attempts > 0:
        # Display current progress
        display_word = ""
        for letter in word:
            display_word += letter if letter in guessed_letters else "_"
        print("Word:", " ".join(display_word))

        # Check for win
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly:", word)
            break

        # Take user input
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        # Check if guess is in the word
        if guess in word:
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("-" * 40)

    else:
        print(f"\n💀 Game Over! The correct word was: {word}")

if __name__ == "__main__":
    hangman()
