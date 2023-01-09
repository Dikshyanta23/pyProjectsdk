# get all parts of email adress entered by the user
import re

# function to get the email and slice it
def main():
    # ask the user for a valid email address
    email_input = input("Please enter a valid email address: ")
    #check for validity
    # a regular expression for accepted email addresses
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    #valid
    if (re.search(email_regex, email_input)):
        # store the values
        (username, domain) = email_input.split("@")
        (domain, extension) = domain.split(".")
        
        print(f'Username: {username}')
        print(f'Domain: {domain}')
        print(f'Extension: {extension}')
    #invalid
    else:
        print('Enter a valid email adress.')

# run main
main()
    
        
        