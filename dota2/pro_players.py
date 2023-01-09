# Below are the functions to list the name of selected numbers of pro dota 2 players or list the name of 3 players from any team
import requests
import conf

def get_pro_players(n):
    extended_url = 'proPlayers'
    r = requests.get(conf.base_url+extended_url)
    if r.status_code in range(200, 299):
        data_json = r.json()
        player_list = []
        # add the dictionaries into a list
        for i in range(n):
            player_list.append(data_json[i])
        # we do not want all the keys, a list of all the keys desired
        wanted_keys = ['avatar', 'personaname','country_code', 'name','fantasy_role', 'team_name']
        for i in range(len(player_list)):
            # making the links to the images into an image html element using make_image (defined in conf)
            player_list[i]['avatar'] = conf.make_image(player_list[i]['avatar'])
            # filtering the keys
            res = dict((k, player_list[i][k]) for k in wanted_keys
                        if k in player_list[i])
            player_list[i] = res
        return player_list

# a pro player list by their teams
def get_pro_players_by_team_name(team_name):
    extended_url = 'proPlayers'
    r = requests.get(conf.base_url+extended_url)
    if r.status_code in range(200, 299):
        data_json = r.json()
        player_list = []
        # adding 3 players from the desired team into an array
        i = 0
        while i < 3:
            if data_json[i]['team_name'] == team_name:
                player_list.append(data_json[i])
                i +=1
        # only the wanted keys
        wanted_keys = ['avatar', 'personaname','country_code', 'name','fantasy_role', 'team_name']
        for i in range(len(player_list)):
            player_list[i]['avatar'] = conf.make_image(player_list[i]['avatar'])
            # filtering the dictionary for only wanted
            res = dict((k, player_list[i][k]) for k in wanted_keys
                        if k in player_list[i])
            player_list[i] = res
        return player_list
    
