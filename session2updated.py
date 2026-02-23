#print()
variable_name = 5
variable_name2 = "Your name"
variable_name3 = 2+2

my_text = "Hello there"
my_integer = 5
my_float = 3
print(my_float)

box = "name"
box1 = input

#create an variable for age,name and favourite color.
age = 17
name = "Ilenia"
favourite_color = "White"

#Print all of them in seperate lines
print("name:", name)
print("age:", age)
print("favourite Color:", favourite_color)
#Store 3 numbers in different variables and print their sum.
number1 = 5
number2 = 7
number3 = 2
print(number1+number2+number3)

#Create variables for school name,grade and favourite subject,and write an short introduction.
school_name = "Luan Hajdaraga"
grade = 11
favourite_subject = "English"
introduction = "Hi,my name is Ilenia,I am 17 years old and I am from Albania."
print(school_name,grade,favourite_subject,introduction)

#Calculate the age of an person if he is born in 1900,store it in a variable and print it.
current_year = 2026
birth_year = 1900
print(current_year-birth_year)

#Convert the 10 kilometers to meters,5 hours into minutes,store them in variables and print them.
kilometers = 10
meters = kilometers*1000
print(meters)

hours = 5
minutes = hours*60
print(minutes)

#Take the name of the user as input and print a greeting with their name on it (Hello,[name])
name = input("Enter your name: ")
print("Hello,", name)

#Take the name,age and city of the user as input and print a short introduction for them
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print("Hi, my name is", name + ", I am", age, "years old and I live in", city + ".")

#Take 2 integer numbers as input,print them and their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_numbers = num1 + num2

print("First number:", num1)
print("Second number:", num2)
print("Sum:", sum_numbers)

#Take an amount of minutes as input as output that amount as seconds and as hours(2 outputs)
minutes = int(input("Enter amount of minutes: "))
seconds = minutes * 60
hours = minutes / 60
# optional: As hours and minutes(2 hours and 45 minutes)
full_hours = minutes // 60
remaining_minutes = minutes % 60

print("Seconds:", seconds)
print("Hours(decimal):", hours)
print("Hours and minutes:", full_hours, "hours and", remaining_minutes , "minutes")

#Take 2 values as input and calculate the area and perimeter of a rectangle with those sides.
side1 = float(input("Enter first side of rectangle: "))
side2 = float(input("Enter second side of rectangle: "))

area = side1 * side2
perimeter = 2 * (side1 + side2)

print("Area:", area)
print("Perimeter:", perimeter)

