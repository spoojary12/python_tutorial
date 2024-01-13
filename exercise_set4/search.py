def guess_number():
    low, high = 1, 100
    
    print("Think of a number between 1 and 100")
    
    while low <= high:
        mid = (low + high) // 2
        print(f"Is your number {mid}?")
        response = input("Enter 'l' if the number is lower, 'h' if higher, or 'c' if correct: ")
        
        if response == 'c':
            print(f"Yay! I guessed your number {mid} correctly.")
            break
        elif response == 'l':
            high = mid - 1
        elif response == 'h':
            low = mid + 1
        else:
            print("Invalid input. Please enter 'l', 'h', or 'c'.")

if __name__ == "__main__":
    guess_number()