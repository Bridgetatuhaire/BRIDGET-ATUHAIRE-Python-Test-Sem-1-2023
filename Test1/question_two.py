#2. (i) average of two numbers

def find_average(x, y):
    return (x + y) / 2

# Testing the function with two different numbers
number1 = 20
number2 = 24
average = find_average(number1, number2)
print(f"The average of {number1} and {number2} is {average}")

#(ii)
number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))
number_three = float(input("Enter the third number: "))


minimum = min(number_one, number_two, number_three) #finding the minimum number using the min() function


print(f"The minimum number among {number_one}, {number_two}, and {number_three} is {minimum}")
