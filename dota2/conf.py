# This python file cotnains all the constant values and functions used by other Py files in the project
import os
import requests
import pandas as pd

# define a variable to store the base_directory and a directory to store the outputs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, 'outputs')
os.makedirs(OUT_DIR, exist_ok=True)

# the base url for the open dota API
base_url = 'https://api.opendota.com/api/'

# the function to convert a json file into an HTML table
def write_file(filename, val):
    file_dir = OUT_DIR+ f'/{filename}'
    df = pd.DataFrame.from_records(val)
    df.replace({"": "-"}, inplace=True)
    html_str = df.to_html()
    with open(file_dir,'w') as f:
        f.write(html_str)
        
# a dictionary of dota personalities and their account_id
personalities = {'pieliedie': 6922000,
'Sneyking': 10366616,
'Handsken': 18180970,
'N0tail': 19672354,
'Bamboe': 20321748,
'Cr1t-': 25907144,
'JerAx': 26771994,
'MinD_ContRoL': 34505203}
        
# a function to make an image url into an HTML image tag
def make_image(url):
    return f'<img src ="{url}" alt="team_logo" width="200" height="200">'  

# a function that makes a request to API and checks if feedback is recieved
def pass_val(url):
    r = requests.get(url)
    if r.status_code in range(200, 299):
        return r
    return -1