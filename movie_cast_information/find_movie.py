# import constants, requests and json, to be used later in the script
import constants
import requests
import json
# the function below uses the keyword to search the database for matching movies and returns the most popular movie's id and name
def get_movie_by_name(movieName = 'the matrix'):
    # generate an url for requests
    api_url = f'{constants.base_url}/search/movie?{constants.api_part}&page=1&query={movieName}'
    response = requests.get(api_url)
    
    # if a result is returned
    if response.status_code == requests.codes.ok:
        json_object = json.loads(response.text)
        results = json_object.get('results')
        # set up counters to find the movie result with most popularity
        max_popularity = 0
        max_index = 0
        
        # finding the most popular movie
        for i in range(len(results)):
            if results[i].get('popularity') > max_popularity:
                max_popularity = results[i].get('popularity')
                max_index = i
        final_val = results[max_index]
        
        # getting the title of the movie and the movie_id 
        original_title = final_val.get('original_title')
        required_id = final_val.get('id')
    #return the results
    return original_title, required_id