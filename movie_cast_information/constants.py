# this file contains all the constants used by the other py files in the directory

# import os for using environment variable (for privacy purposes)
import os

# api key for themovidb.org and Ninja API
MOVIE_DB_API = os.environ.get('MOVIE_DB_API')
API_KEY = os.environ.get('NINJA_API')

#fixed parts of the url for themoviedb.org
base_url = 'https://api.themoviedb.org/3'
api_part = f'api_key={MOVIE_DB_API}&language=en-US'
