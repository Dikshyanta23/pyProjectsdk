# email_sender
The project scrapes the web to get information about the top 10 most watched youtube videos(wikipedia, link: 'https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos') and sends the information on an email to selected email adresses.

A brief description of all the files are given.

scrape.py: contains functions to take an input url (speicific to wikipedia for the given example) and scrapes the resultant webpage to take values from the first table.

values.py: stores all the values necessary for the project. These include email sender, email reciever, password (stored as a local environment variable for privacy reasons), the body of the email, subject, etc.

send_mail.py: contains function to use values such as email_sender, email_reciever, password, subject, body, etc. to generate the emails and send them to the desired recievers.

main.py: The main function that contains script to use the values and functions in the other python documents to scrape the values from the webpage, use the values to generate appropriate email and send them to the desired email addresses.

For running the program, please run the python file main.py (you need to have installed all the modules used. They are os, requests, requests_html, email.message, ssl, smtplib). The password for the email is stored in a local enviroment variable for privacy reasons, therefore an appropriate password must also be stored in the localhost as environment variable with a key 'password'.

