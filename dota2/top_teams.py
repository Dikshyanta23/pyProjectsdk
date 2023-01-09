# This python file contains the script to get chosen number of top rated teams in a table format in an html file

# import the necessary modules and functions
import requests
import pandas as pd
import conf

# a function to get the teams with the highest ratings, takes the number of teams as input
def get_top_teams(n=10):
    extension = 'teams?page=0'
    url = conf.base_url+extension
    data = conf.pass_val(url)
    
    if not(data == -1):
        data_json = data.json()
        new_list = []
        
        for i in range(n):
            data_json[i].pop('last_match_time')
            data_json[i].pop('team_id')
            data_json[i]['logo_url'] = conf.make_image(data_json[i]['logo_url'])
            
            new_list.append(data_json[i])
            
    return new_list



