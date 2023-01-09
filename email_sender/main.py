# this is the main script for the application

# the necessary imports
import values
import send_mail
import scrape

# set the url from which data needs to be pulled
url = 'https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos'

# scrape the url and return a string
the_final_string = scrape.makeString(scrape.parse_and_extract(url))

#subject and body of the email 
subject = 'Knowledge is power!'
body = f'Knowledge is power. Therefore, I have provided you a list of top 10 most watched videos on youtube.\n\n{the_final_string}\n\nThank you.'

# use the values and function in send_mail to send the emails

send_mail.generate_email(values.email_sender, values.email_reciever, subject, body, values.email_password)



