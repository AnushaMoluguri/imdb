import requests
import json
from newimdb03.settings import IMDB_DATA
class imdb():
    def __init__(self,get_respounse):
        self.get_response=get_respounse
        print("I am constructor")
        t_list=fetchdata()
        #import requests
        list_of_data=[]
        for title in t_list:

            url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+title

            headers = {
                'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
                'x-rapidapi-key': "0ac662495cmsha3ddbe01a85b038p1b0e32jsn0541b2f89aff"
            }

            response = requests.request("GET", url, headers=headers)
            dict_data=json.loads(response.text)
            #print(type(dict_data))
            list_of_data.append(dict_data)
            #print(list_of_data)
            json.dump(list_of_data,open(IMDB_DATA,"w"))

    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        print("I am call")
        return response
def fetchdata():
    #import requests


    url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

    querystring = {"genre": "%2Fchart%2Fpopular%2Fgenre%2Fadventure"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "11f73d77e2msh6fa7bccf408b169p14a164jsn27c043803560"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(type(response.text))#strg
    #print(response.text)
    list_data=response.text.split('/')
    #print(type(list_data))#list
    #print(list_data)
    l=[]
    for x in list_data:
        if x.split('/'):
            if x.startswith('tt'):
                l.append(x)
    return l
