# Function for nth Fibonacci number
reps = int(input("Enter number:"))


def fibonacci(n):
    if n < 0:
        print("Incorrect Input")
    elif n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


for i in range(reps):
    print(fibonacci(i))
