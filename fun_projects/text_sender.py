# a program to send text periodically to a number

#download schedule using the terminal command: pip3 install schedule
#download requests using the terminal command: pip3 install requests  
import requests
import schedule
import time
def send_message():
    resp = requests.post('https://textbelt.com/text', {
    # enter the phone number
    'phone': '',
    # enter the message to be send
    'message': '',
    'key': 'textbelt',
    })
    #print(resp.json())

# schedule the text message every day at 6
schedule.every().day.at('06:00').do(send_message)