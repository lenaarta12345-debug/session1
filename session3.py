bool = True
bool2 = False

#Boolean True or False
print(bool,bool2)
print(5==3)
print(5=="5")
print(5!=1)
print(5>3,5<3,5>=1,5<=3)

#Conditional statements 1
if 10 > 5:
    print("This statement is true")
print("Outside")
#2
number = 5
if number > 0:
    print("We still have tickets remaining")

age = 19
if age > 18:
    print("You are an adult")
else:
    print("You are not an adult")

#3
age = 150
if age > 18:
    print("The price is 500 lek")
elif age > 10:
    print("The price is 200 lek")
else:
    print("You can enter for free")

grade = 11
if grade > 100:
    print("Invalid input")
elif grade < 0:
    print("Invalid Input")
else:
    print("Valid")

#Exersizes
#Level 1
#Print boolean expressions by comparing different numbers.Use all 6 comparison operators.
bool = "True"
bool2 = "False"
print(5==9)
print(3!=5)
print(7>4)
print(4<2)
print(19>=12)
print(23<=21)
#Store an number in a variable and print whether the variable is greater than 10.
number = 9
if number > 10:
    print("The variable is greater than 10")
else:
    print("The variable is not greater than 10")
#Store 2 numbers in variables and print whether they are equal.
number1 = 3
number2 = 5
print(number1==number2)
#Level 2
#Use conditional statements to check if a number is positive
number = 2
if number > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")
#Use conditional statements to check if the score input (0-100) is passing of failing (50+)
number = 61
if number < 0:
    print("You have failed the test.")
elif number > 50:
    print("You have passed the test.")
else:
    print("You have failed the test")

#Use conditional statements to check if a number input is even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Level 3
#Use if-else conditional statements to check if an age input is categorized an adult or minor.
age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult")
else:
    print("You are an minor")

#Use conditional statements to check which of 2 number inputs is greater than the other (Number 1,number 2 ,either.
num1 =int(input("Enter your first number: "))
num2 =int(input("Enter your second number: "))
if num1 > num2:
    print("The first number is greater than the second.")
else:
    print("The first number is not greater than the second")
#Ask the user for 2 password inputs and check if they match.
password1 =int(input("Enter password 1"))
password2 = int(input("Enter password 2"))
if password1 == password2:
    print("Your password matches.")
else:
    print("Your password does not match.")
#Level 4

#Use conditional statements to check if a temperature is warm or cold.<10 is cold 10-25 is warm,25+ is hot.
temperature = 32
if temperature < 10:
    print("The temperature is cold.")
elif temperature < 25:
    print ("The temperature is warm.")
else:
    print("The temperature is hot.")
#Use conditional statements to check if a number input is big or small, <100, 100-1000,1000+
num=int(input("Enter number"))
if num < 100:
    print("Number is small.")
elif num < 1000:
    print("Number is big.")
else:
    print("Number is bigger.")
#Create 2 variables for username and password.Take 2 inputs from the user and check if the credientals match.Output
#Acces granted" or "Acces Denied

stored_user= "admin"
stored_pass = "1234"
username = input("Enter username: ")
password = input("Enter password: ")
if username == stored_user and password == stored_pass:
    print("Access granted")
else:
    print("Access Denied")
