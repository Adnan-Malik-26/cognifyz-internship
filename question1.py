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

def main():
    num = random.randint(1, 100)
    print("Guess the number between 1 and 100")

    guess(num)

if __name__ == '__main__':
    main()
