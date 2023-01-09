# import all the function to be used from the other .py files in the directory
from find_movie import get_movie_by_name
from find_cast import get_cast
from get_info import get_info

# the name of a movie to be used by the API as keyword
q_string = 'avengers'

# call the get_movie_by_name function to get valuable information about the movie and store the full name and movie id
full_name = get_movie_by_name(q_string)[0]
movie_id = get_movie_by_name(q_string)[1]

# call the get_cast function and pass the movie_id to get the name of the entire cast
cast_list = get_cast(movie_id)

# call the get info method to print the basic information of up to 10 most popular cast in the most popular result of the search
# movie named q_string
get_info(full_name, cast_list)