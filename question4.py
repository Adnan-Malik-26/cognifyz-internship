def fibonacci(n):
    sequence = []
    a,b=0,1
    while a<=n:
        sequence.append(a)
        a, b = b,a+b
        
    return sequence

def main():
    user_input = input("Enter a number to generate Fibonacci sequence up to: ")
    
    number = int(user_input)
    if number<0:
        print("Please enter a non-negative integer.")

    else:
        fibo = fibonacci(number)
        print(f"Fibonacci sequence upto {number}: {fibo}")

if __name__ =="__main__":
    main()