
# Python program to add two numbers
 
# Take input from the user
num1 = input("Enter first number: ")	#Integer is needed for math operations not string.
num2 = input("Enter second number: ")

# Convert the input strings to integers
num1 = int(num1)  # Corrected: Convert input to integer
num2 = int(num2)  # Corrected: Convert input to integer
 
# Add the two numbers
result = num1 + num2	#Result will give sum now that num1 and num2 are integers and not string anymore.
 
# Print the result
print("The sum of", num1, "and", num2, "is", result)  # Corrected: Now 'result' will be the sum, not a concatenation
