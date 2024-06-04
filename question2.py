import random

def guess(n):
    while True:
        u = int(input("Please Give Your Guess: "))
        if n < u:
            print("Too High, Try Again!")
        elif n > u:
            print("Too Low, Try Again!")
        else:
            print("You have guessed the number correctly! It was ",n)
            break
def inputs():
    lower_range = int(input("Please Give Your Lower Range: ")) 
    upper_range = int(input("Please Give Your Upper Range: "))
    if lower_range>upper_range:
        print("Please Enter the ranges Correctly")
        return inputs()
    else:
        return lower_range,upper_range

 
def main():
    lower_range , upper_range = inputs()
    
    num = random.randint(lower_range, upper_range)
    print(f"Guess the number between {lower_range} and {upper_range}")

    guess(num)

if __name__ == '__main__':
    main()
