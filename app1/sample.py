import requests


url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

querystring = {"genre":"%2Fchart%2Fpopular%2Fgenre%2Fadventure"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "11f73d77e2msh6fa7bccf408b169p14a164jsn27c043803560"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)