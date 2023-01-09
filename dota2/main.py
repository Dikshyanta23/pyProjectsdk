# This file will use the functions listed in the other python files in the directory to generate desired outputs

# import all the files
import heroes, personalities, top_teams, pro_players, conf

""" 
Script based on dota 2 heroes, imported from heroes.py
"""
# The following line of code outputs the chosen number(5) of most picked and most banned heroes in competitive dota into the console
heroes.bans_and_pick(5)

# The function below outputs stats (matches played, wins, and losses of each hero in a list) against a list of counters
# defining the list of heroes and the counter set
heroes_chosen = ['Io', 'Earth Spirit', 'Jakiro']
# Some potential counters to those heroes
counters = ['Axe', 'Rubick', 'Doom', 'Silencer', 'Lion']    
           
heroes.check_matchup(heroes_chosen, counters)



""" 
Script based on dota2 players, imported from personalities.py
"""

# For the three functions below, the informnation about a list of players will be outputted to the console
# The personalities pieliedie,'Sneyking','Handsken', 'N0tail', 'Bamboe', 'Cr1t-', 'JerAx', 'MinD_ContRoL'

# The following script will output the desired number(3) of each players most played heroes into the console
personalities.get_most_played_heroes(personalities.players)  

# The following script will get the average duration, kills, death and assists and the party size of the players in the recent 20 matches      
personalities.get_recent_matches(personalities.players) 

# The following script will output the name, persona, mmr, leaderboard rank, wins and losses of each players into the console    
personalities.get_base_stats(personalities.players)




""" 
Script based on pro players, imported from pro_players.py
Note that any output external from the terminal console can be found in a folder named outputs in the same directory as the script

"""

# The following code will create an HTML file, named eg_players.html and put the information of 3 random eg players into the file
conf.write_file('eg_players.html', pro_players.get_pro_players_by_team_name())

# The following code will get information about desired number of random pro players(10) and output it in a chosen HTML file (pro_players.html)
conf.write_file('pro_players.html',pro_players.get_pro_players(10))



""" 
Script based on  professional teams, imported from top_teams.py
Note that any output external from the terminal console can be found in a folder named outputs in the same directory as the script

"""

# The code below will create an HTML file of chosen name (top_teams.html) and store the information of chosen number(10) of most rated dota 2 teams
conf.write_file('top_teams.html', top_teams.get_top_teams(10))