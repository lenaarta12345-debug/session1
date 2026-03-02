#Output numbers from 1 to 10 using while loops
i = 1
while i <= 10:
    print(i)
    i += 1
#Output numbers from 1-10 using for loop
for i in range(1-11):
    print(i)
#Output your name 5 times
for i in range(5):
    print("Ilenia")

#Output only even numbers 1-20
for i in range(1,21,2):
    print(i)

#Level 2
#Create an countdown from 10
count = 10
while count > 0:
    print(count)
    count = count-1
#Take an integer input from the user and calculate the sum of all numbers from 1 to n
n = int(input("Enter a number: "))

total = n * (n + 1) // 2
print("Sum from 1 to", n, "is:", total)

#Take an integer intput from the user and output the multiplication table of that number
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

 #Level 3
#1
    password = "Mypass123"
    attempts = 3
    for i in range(attempts):
       user_input = input("Enter password :")
    if user_input == password:
        print("Success")
    else:
        print("Acces Denied")
        break

#Declare a number variable from 1-100.Implement a loop that repeatedly takes user input until they
#find the number.
#Optional Implement a hint system outputting "higher" or "lower"
import random
secret_number = random.randint(1, 100)

print("I have selected a number between 1 and 100.")

while True:
    user_input = input("Enter your guess: ")
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue
    s
    guess = int(user_input)

    if gues == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
#Level 4
n = 4
for i in range (n):
    print('*'*(i+1))
    
    #Implement a menu system loop that will take user input and output "hello" for input = 1,output
    #"bye" for input = 2 and exit the program for input 3.
    while True:
        print("\nMenu:")
        print("1. Say Hello")
        print("2. Say Bye")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("hello")
        elif choice == "2":
            print("bye")
        elif choice == "3":
            print("Exiting program...")
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
            break
