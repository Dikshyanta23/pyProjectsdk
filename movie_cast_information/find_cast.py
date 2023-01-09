import constants
import requests 
import json
# the function uses movie_id of a movie in the moviedb.org and outputs a list of the names of cast
def get_cast(movie_id = 624860):
    #using url parts from constants to get a request from the movie_db.org of a list of casts
    url = f'{constants.base_url}/movie/{movie_id}/credits?{constants.api_part}'
    response = requests.get(url)
    # if value is returned
    if response.status_code == requests.codes.ok:
        json_object = json.loads(response.text)
        cast_list = json_object.get('cast')
        # sort the list in relation to the popularity (descending) of the cast
        newlist = sorted(cast_list, key=lambda d: d['popularity'], reverse=True)
        # create a new list titled cast names and put the names of all the cast 
        cast_names = []
        for i in range(len(newlist)):
            cast_names.append(newlist[i].get('name'))
        # return the list of cast names
        return cast_names