# Movie cast information program (python)

### The project uses a movie name input to get the information about the most popular cast in the movie. A short description of all the files in the project are given below:

#### constants.py - (stores all the constants that are imported and used by the other python files in the project)

#### find_movie.py - (contains a function that will take a movie name as input and return the full title and movie_id of the most popular movie matching the name from themoviedb.org)

#### find_cast.py - (contains a function that will take a valid movie_id pertaining to themoviedb.org and returns a list of all the cast in the movie)

#### get_info.py - (contains a function that will take a list of names and request information about those names on Ninja\Celibrity API, in order to get the basic information like gender, nationality, age(if still alive) and net worth (in USD) and print them to the console)

#### main.py - (imports all the functions located in the other python files and runs the functions located in the different py files in proper order, in order to get the information of up to 10 most popular cast in the most popular movie result matching the input)

## Note to the reader

Please note that I have set up and used environemnt variables for unshareable information such as API_KEYS. Therefore the program
will not run if simply downloaded and run from the terminal. However, I will share the websites so that the user can get their own
API keys and also the link to a youtube video which shows how to create and use environment variable. The environment variables in
the code can be found in constants.py with the names MOVIE_DB_API (themoviedb.org) and API_KEYS (Ninja API)

- themoviedb.org: 'https://www.themoviedb.org/settings/api'
- ninja_api: 'https://api-ninjas.com/profile'
- create and use environment variable: 'https://youtu.be/R0hpSIPqZek'





