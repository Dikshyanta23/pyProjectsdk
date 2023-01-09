# define the functions for performing addition, subtraction, multiplication and division

# add function
def add(a, b):
    value = a+b
    value_string = (f'{a} + {b} = {value}')
    return value_string
    
# subtract function
def sub(a, b):
    value = a-b
    value_string = (f'{a} - {b} = {value}')
    return value_string

# multiplication function
def mult(a, b):
    value = a*b
    value_string = (f'{a} * {b} = {value}')
    return value_string

# divide function, the answer is limited to 2 decimal places
def div(a, b):
    value = a/b
    value_formatted = f'{value:.2f}'
    value_string = (f'{a} / {b} = {value_formatted}')
    return value_string

# a function to return respective values
def answer(a, b, sign):
    if sign == "+":
        print(add(a, b)+'\n')
    elif sign == '-':
        print(sub(a,b)+'\n')
    elif sign == '*':
        print(mult(a,b)+'\n')
    else:
        print(div(a,b)+'\n')

# Main
# take the choice of operation from the user
print("\nEnter +, -, *, / for addition, subtraction, multiplication and division respectively. Enter ':' to stop the program.")

# use a while loop to let the user perform multiple operations
choice  = 'a'
valid_inputs = ['+', '-', '/', '*']
while (choice != ':'):
    choice = input("Input your choice (+, -, *, /): ")
    # check for exiting the program
    if choice == ":":
        print("Thank you for using the basic calculator.")
    # check if the user input is valid
    # not valid
    elif choice not in valid_inputs:
        print('Only +, -, *, / are accepted as inputs at this stage.')
    #valid
    else:
        # take the integer inputs
        a = int(input('Enter the first integer value: '))
        b = int(input('Enter second integer value: '))
        
        # use the function 'answer' to print the values to the console
        answer(a, b, choice)
        