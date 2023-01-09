# a program to generate a random password
import string
import random

# a list of possible characters in the password
characters = list(string.ascii_letters+string.digits+"~`! @#$%^&*()_-+={[}]|\:;'<,>.?/\"")

# a function for generating random password
def gen_password():
    # get the length of the password
    password_length = int(input('How long would you like your password to be?'))
    #shuffle the character set
    random.shuffle(characters)
    #create list to store the array
    password = []
    # add the required number of characters
    for i in range(password_length):
        password.append(random.choice(characters))
    # make the array into a single string using join
    password = "".join(password)
    print(f'Your password is {password}')
    
option = input("Do you want to generate a password?(yes/no):")

if option == 'yes':
    gen_password()
elif option == 'no':
    quit()
else:
    print('Invalid input, please input either yes or no.')
    quit()