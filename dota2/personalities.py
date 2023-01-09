# This python file contains the functions to output different infomration about the dota2 personalities in conf file

# necessary imports
import conf
import requests
from math import ceil

intermediate_url = 'players/'

# create a class to keep the players and their account ids
class Player:
    def __init__(self, name, account_id):
        self.name = name
        self.account_id = account_id

# a function to format time in minutes
def in_mins(secs):
    minutes = secs//60
    secs = secs%60
    return f'{minutes}:{secs}'

# make the dictionary in conf into Player class so that the values can be easily accessed
players = []
players_dict = conf.personalities
dict_keys = list(players_dict.keys())
dict_vals = list(players_dict.values())

for i in range(len(players_dict)):
    temp = Player(dict_keys[i], dict_vals[i])
    players.append(temp)


# a function to get hero name given hero id
def get_name_from_id(id):
    hero_extn = 'heroes'
    hero_url = conf.base_url+hero_extn
    q = requests.get(hero_url)
    data_json = q.json()
    for i in range(len(data_json)):
        if int(data_json[i]['id']) == int(id):
            return data_json[i]['localized_name']
    return '-'



# a function to ouput name, personaname, mmr and leaderboard rank of players in a provided list
def get_base_stats(list_of_players):
    for player in list_of_players:
        final_url = conf.base_url+intermediate_url+f'{player}'
        wlurl = final_url+'/wl'
        r = conf.pass_val(final_url)
        if not (r == -1):
            data_json = r.json()
            q = conf.pass_val(wlurl)
            wl_json = q.json()
            # store useful values into variables
            leaderboard_rank = data_json['leaderboard_rank']
            mmr = data_json['mmr_estimate']['estimate']
            personaname = data_json['profile']['personaname']
            name = data_json['profile']['name']
            wins = wl_json['win']
            loss = wl_json['lose']
            
            #output the information to the console
            print(f'Name: {name}\nPersona name: {personaname}\nMMR: {mmr}\nRank: {leaderboard_rank}\nWins: {wins}\nLosses: {loss}\n')
        
# a function to get the recent matches of the players
def get_recent_matches(player_list):
    extension = 'recentMatches'
    # for each player
    for i in range(len(player_list)):
        name = player_list[i].name
        final_url = conf.base_url+intermediate_url+f'{player_list[i].account_id}/{extension}'
        r = conf.pass_val(final_url)
        
        # if we get valid response
        if r!= -1:
            data_json = r.json()
            
            # set counters for all variables in order to return the averages
            matches = len(data_json)
            duration = 0
            kills = 0
            deaths = 0
            assists = 0
            party_size = 0
            
            # loop through to add the values for each match to the counters
            for i in range(len(data_json)):
                duration+= data_json[i]['duration']
                kills+=data_json[i]['kills']
                deaths+=data_json[i]['deaths']
                assists+= data_json[i]['assists']
                party_size+=data_json[i]['party_size']
            
            # calc the averages for each varaible by dividing by total matches    
            avg_duration = in_mins(ceil(duration/matches))
            avg_kills = ceil(kills/matches)
            avg_deaths = ceil(deaths/matches)
            avg_assists = ceil(assists/matches)
            party_size = ceil(party_size/matches)
            
            # output the results to the console
            print(f'Player: {name}\nAverage duration: {avg_duration}\nKills: {avg_kills}\nAssists: {avg_assists}\nDeaths: {avg_deaths}\nParty size: {party_size}\n')
                
# a function to get the player's n most played heroes           
def get_most_played_heroes(player_list, n):
    extension = '/heroes'
    # for each player
    for i in range(len(player_list)):
        name = player_list[i].name    
        final_url = conf.base_url+intermediate_url+f'{player_list[i].account_id}{extension}' 
        r = conf.pass_val(final_url)
        
        # if we get a proper response
        if r != -1:
            data_json = r.json()
            print(f'\nPlayer: {name}\n')
            
        # loop through the already sorted list to get the top heroes
            for i in range(n):
                # get only the necessary dictionary values
                temp = data_json[i]
                hero_id = temp['hero_id']
                games = temp['games']
                wins = temp['win']
                loss = games-wins
                hero_name = get_name_from_id(hero_id)
                
                # ouput the results to the console
                print(f'{i+1}\nName: {hero_name}\nTotal games: {games}\nWins: {wins}\nLosses: {loss}')
            
    
    
