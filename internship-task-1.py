import random

words = ["python", "computer", "programming", "keyboard", "internet"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
incorrect_guesses = 0
guessed_letters = []

print("Welcome to Hangman Game!")

while incorrect_guesses < 6 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", 6 - incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")

            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)