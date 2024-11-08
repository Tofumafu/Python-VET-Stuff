#Enter Numbers 
num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")
num3 = input("Enter Third Number: ")
num4 = input("Enter Forth Number: ")
num5 = input("Enter Fifth Number: ")
#List of Numbers Input
numbers = [int(num1), int(num2), int(num3), int(num4), int(num5)]
total = sum(numbers)
#Print
print("Sum = ", total)
#Average Calculation
average = sum(numbers) / len(numbers)
#Print
print("Average = ", average)