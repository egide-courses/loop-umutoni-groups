









"""for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
        
    print()""""1"
# Program to reverse the digits of an integer using a while loop

"""num = int(input("Enter an integer: "))
n = abs(num)
reversed_num = 0
while n > 0:
    digit = n % 10          
    reversed_num = reversed_num * 10 + digit  
    n //= 10                    
if num < 0:
    reversed_num = -reversed_num
print("The reversed number is:", reversed_num)""""2"


"""num = int(input("Enter an integer: "))
reversed_num = 0
is_negative = False
if num < 0:
    is_negative = True
    num = -num  
while num > 0:
    digit = num % 10          
    reversed_num = reversed_num * 10 + digit  
    num = num // 10           
if is_negative:
    reversed_num = -reversed_num
print("Reversed number:", reversed_num)""""3"

"""for num in range(2, 101):  
    is_prime = True        
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break 
    if is_prime:
        print(num, end=" ")""""4"


# Factorial using for loop
"""n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")""""5"

# Program to calculate the sum of digits of an integer
"""num = int(input("Enter an integer: "))
n = abs(num)
sum_digits = 0
while n > 0:
    digit = n % 10      
    sum_digits += digit  
    n //= 10             
print("The sum of digits of", num, "is:", sum_digits)""""6"


"""for a in range(1, 6):
    for b in range(1, a + 1):
        print(b, end=" ")
    print()""""7"

"""numbers = []
# Ask user to enter 10 numbers
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Initialize max and min with the first number
maximum = numbers[0]
minimum = numbers[0]

# Loop through the list to find max and min
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

# Display results
print("Maximum value:", maximum)
print("Minimum value:", minimum)""""8"

"""for n in range(1, 101):
    if n%3==0:
        continue
    elif n == 73:
        break
    print(n)""""9"

"""# Check if a string is a palindrome using a loop
text = input("Enter a string: ")
is_palindrome = True
length = len(text)
for i in range(length // 2):
    if text[i] != text[length - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')""""10"





