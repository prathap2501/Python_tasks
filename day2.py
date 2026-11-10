a = 50

guess = int(input("Guess the number: "))

if guess == a:
    print("Correct guess!")
elif guess > a:
    print("Too high!")
else:
    print("Too low!")
