# dota2

### Used the Open Dota API (https://docs.opendota.com) to run different queries about the game stats, professional teams and professional players.

### A brief summary of all the files is given below:

1. **conf.py**: Contains all the uniform functions and global constants used throughout the other .py files.

2. **heroes.py**: Contains functions related to dota 2 heroes that ouput infomration like most picked heroes, most banned heroes, etc.

3. **personalities.py**: Contains functions realated to dota 2 personalities that ouput information like the personality's most played heroes, games played, wins, loss and account information.

4. **pro_players**: Contains functions realated to the dota 2 current pro_players like getting a chosen number of random professional players or getting players by team names.

5. **top_teams**: Contains the functions related to the dota 2 professional teams like getting a chosen number of the most highly rated current dota 2 team.

6. **main.py**: The main file for the program, contains script that runs a sample of all the functions defined in the other py file.

**Note that, in order to run a sample of the program, please use main.py as it contains the script that calls all the functions which are only defined in the other .py files. More detailed explanation of each python file is given within the file itself in the form of comments.**


### Dependencies

The following modules are required for running the program, the terminal command to download these modules are given alongside in parenthesis:
1. Pandas *(pip -m install pandas)*
2. Requests *(pip -m install requests)*

