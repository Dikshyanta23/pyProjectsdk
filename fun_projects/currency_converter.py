# program converts any of the five currencies to each other (pounds, dollars, nepalese, australian dollar, euro)

import requests


url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()
rates = data['rates']

def main():
    #create a valid input list
    val_input = ['eur', 'usd', 'aud', 'npr', 'gbp']
    #take the inputs
    currency1 = input('Please enter the currecny you want to exchange.\naustralian dollars: "aud", British pounds: "gbp", Dollars: "usd", Nepalese: "nrp", Euroes: "eur".\n')
    currency2 = input('Please enter the currecny you want to exchange into.\naustralian dollars: "aud", British pounds: "gbp", Dollars: "usd", Nepalese: "npr", Euroes: "eur".\n')
    amount_to_exchange = int(input('Please enter the amount you want to exchange: '))
    # main-logic
    if (currency1 in val_input) and (currency2 in val_input):
        currency1up = currency1.upper()
        currency2up = currency2.upper()
        # convert currency1 into usd
        amount_in_usd = amount_to_exchange/rates[currency1up]
        #convert usd into the final currency
        amount_final = amount_in_usd*rates[currency2up]
        print(f'In exchanging {amount_to_exchange} {currency1up}, you recieve {amount_final:.2f} {currency2up}')
        
        
    else:
        print("The program accepts only one of (aud, usd, eur, npr, gbp) as inputs.")
        
#execute main
main()