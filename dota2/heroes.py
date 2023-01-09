# This python file contains method to output some information about dota 2 heroes

import conf
import requests

# a function to store the name and hero id of all heroes into a dictionary
def all_hero_nameid():
    r = conf.pass_val(conf.base_url+'heroes')
    if r != -1:
        data_json = r.json()
        # a dictionary to store all key(hero_name) and value (hero_id) pairs
        hero_nameid_dict = {}
        for i in range(len(data_json)):
            hero_nameid_dict[data_json[i]['localized_name']] =  data_json[i]['id']
        return(hero_nameid_dict)
    return -1
            
all_heroes_dict = all_hero_nameid()

# a function to check the win/loss performance of my favourite heroes against the counters
def check_matchup(a_list, the_list):
    # for each hero
    for z in range(len(a_list)):
        hero_id = all_heroes_dict[a_list[z]]
        hero_name = a_list[z]
        print(f'\n{hero_name} performance against some counters.\n')
        im_extn = f'heroes/{hero_id}/matchups'
        final_url = conf.base_url+im_extn
        
        r = conf.pass_val(final_url)
        if r != -1:
            json_data = r.json()
            # for each of the counter
            for j in range(len(the_list)):
                counter_name = the_list[j]
                counter_id = all_heroes_dict[the_list[j]]
                # matching the information
                found = False
                while not found:
                    for l in range(len(json_data)):
                        # once the id matches
                        if int(json_data[l]['hero_id']) == int(counter_id):
                            
                            # store all different values into variables
                            total_games = json_data[l]['games_played']
                            wins =json_data[l]['wins']
                            loss = total_games - wins
                            
                            # output the values for each hero to the console
                            print(f'Hero: {counter_name}\nGames played (against): {total_games}\nWins: {wins}\nLoss: {loss}\n')
                            found = True

# a function to output the desired number most banned and most picked heroes
def bans_and_pick(n):
    exntesnion = 'heroStats'
    final_url = conf.base_url+exntesnion
    r = conf.pass_val(final_url)
    if r != -1:
        data_json = r.json()
        # sort the list, one being in descending order of picks and the other in descending order of bans
        new_list = sorted(data_json, key=lambda i: i['pro_pick'], reverse=True)
        new_list1 = sorted(data_json, key=lambda i: i['pro_ban'], reverse=True)
        
        # two string values onto which each ouput will be concatenated
        picked_str = '\nThe most picked heroes:\n'
        banned_str = '\nThe most banned heroes:\n'
        
        for i in range(n):
            # append the values into the string
            picked_str += f'\nHero name: {new_list[i]["localized_name"]}\nTotal picks: {new_list[i]["pro_pick"]}\nTotal bans: {new_list[i]["pro_ban"]}\nTotal win: {new_list[i]["pro_win"]}\nTotal loss: {int(new_list[i]["pro_pick"])-int(new_list[i]["pro_win"])}\n'
            banned_str = banned_str+ f'\nHero name: {new_list1[i]["localized_name"]}\nTotal picks: {new_list1[i]["pro_pick"]}\nTotal bans: {new_list1[i]["pro_ban"]}\nTotal win: {new_list1[i]["pro_win"]}\nTotal loss: {int(new_list1[i]["pro_pick"])-int(new_list1[i]["pro_win"])}\n'
        # output the strings into the console
        print(picked_str, banned_str)

        





