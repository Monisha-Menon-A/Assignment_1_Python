
# 1) Print name, student number, and email address
print("Bob")
print("ST1001")
print("bob@example.com")

# 2) Print name, student number, and email address using escape sequences
print("Bob\nST1001\nbob@example.com")

# 3) Add, subtract, multiply and divide two numbers
a=14
b=7
c=a+b
d=a-b
e=a*b
f=int(a/b)
print("14+7=",c)
print("14-7=",d)
print("14*7=",e)
print("14/7=",f)

# 4) Displays the numbers from 1 to 5 as steps
steps = "1\n2\n3\n4\n5"
print(steps)

# 5) Output sentence with quotation marks and line break
print("\"SDK\" stands for \"Software Development Kit\", whereas")
print("\"IDE\" stands for \"Integrated Development Environment\".")

# 6) Check the outputs
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

#  7) Data type conversion
num = 23
textnum = "57"
decimal = 98.3
# Print types
print(type(num))
print(type(textnum))
print(type(decimal))
# Calculate sum
sum = num + int(textnum) + decimal
print("Sum:", sum)
# Print datatype of sum
print("Type of sum:", type(sum))

#  8) Calculates total minutes in a year
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour
print("This program calculates the total number of minutes in a year.")
print(f"A year has {total_minutes_in_year} minutes.")

# 9) Print name with greeting
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

# 10) PoundsToDollars.py
conversion_rate = 1.3
pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * conversion_rate
print(f"£{pounds} are ${dollars}")
