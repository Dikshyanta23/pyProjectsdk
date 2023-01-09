# import constants, requests and json to be used later in the program
import constants
import requests
import json

# This function will take the title of the movie and the list of cast and output the information of up to 10 most popular ones
def get_info(movie_name, name_list):
    # a general template for the API request
    api_template = 'https://api.api-ninjas.com/v1/celebrity?name='
    
    # outputting the information to the console
    print(f'Below are the names, gender, nationality and age(if they are alive) of up to 10 most popular cast members in {movie_name}')
    # setting a counter to output at most most 10 sets of information
    i = 0
    # for all names in the given list
    for name in name_list:    
            # complete the url query    
            api_url = api_template+name
            
            response = requests.get(api_url, headers={'X-Api-Key': constants.API_KEY})
            #  if we are provided with a result
            if response.status_code == requests.codes.ok:
                # convert it into a json_object
                json_object = json.loads(response.text)
                # check if the result is empty
                if len(json_object)>0:
                    json_object = json_object[0]
                    # store all the necessary values into variables
                    gender = json_object.get('gender')
                    nationality = json_object.get('nationality')
                    is_alive = json_object.get('is_alive')
                    age = json_object.get('age')
                    net_worth = json_object.get('net_worth')
                    
                    # only print the age if still alive
                    if is_alive == True:
                        print(f'\nname: {name}\ngender: {gender}\nnationality: {nationality}\nage: {age}\nnet worth: {net_worth}')
                    else:
                        print(f'\nname: {name}\ngender: {gender}\nnationality: {nationality}\nnet worth: {net_worth}')
                    # limiting the number of cast information to 10
                    i += 1
                    if i >= 10:
                        break