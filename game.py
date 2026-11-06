import random

def guessing_game():
    # 1. Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # 2. Start the game loop
    while True:
        try:
            # Get the user's guess and convert it to an integer
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # 3. Check the user's guess against the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break # Exit the loop and end the game
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guessing_game()