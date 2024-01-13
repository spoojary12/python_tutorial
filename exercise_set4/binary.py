import random

def binary_search_guess_number():
    # Generate a random number between 0 and 100 for the user to guess
    target_number = random.randint(0, 100000)
    
    # Set the initial search space
    low = 0
    high = 100000
    guess = -1  # Initialize the guess variable
    counter = 0
    
    # Start the binary search loop
    while guess != target_number:
        counter = counter + 1
        # Use binary search to guess the number
        guess = (low + high) // 2
        
        # Print the current guess to the user
        print(f"Is the number {guess}?")
        
        # Get user input on whether the guess is correct or needs adjustment
        user_input = input("Enter 'h' if the guess is too high, 'l' if too low, or 'c' if correct: ")
        
        # Adjust the search space based on user input
        if user_input == 'h':
            high = guess - 1
        elif user_input == 'l':
            low = guess + 1
        elif user_input == 'c':
            print(f"Congratulations! The correct number is {target_number}, and it took me {counter} tries.")
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
    
    # End of the game




def b_search(max_value):
    # set max_value
    high = max_value
    # set min value
    low = 0
    # set mid value
    mid = 0
    # initialize counter
    counter = 0
    guess = random.randint(0, max_value)
    # check variable which check if answer if true
    isCorrectGuess = False
    # while loop till check is false
    for i in range(max_value):
        mid = (high - low) // 2 # floor division
        counter = counter + 1
        if mid == guess:
            return {"val":max_value, "tries": counter}
        elif guess > mid:
            low = mid
        elif guess < mid:
            high = mid
    #print(f'guess: {guess}, number of tries:{counter}')
    

results = []   
for i in range(0,1000,10):
   pass



print(b_search(100))
