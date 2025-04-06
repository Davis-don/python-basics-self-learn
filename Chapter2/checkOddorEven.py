# Function to check whether number is even or odd

def check_odd_or_even(number):
    if(number % 2 == 0):
        print(f" number {number} is even")
    else:
        print(f"number {number} is odd")


number_input_is = input("Enter a number:\n")

check_odd_or_even(int(number_input_is))