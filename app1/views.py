from django.shortcuts import render
import json
from newimdb03.settings import IMDB_DATA


def dict_data():
    dict_da=json.loads(open(IMDB_DATA).read())
    titles=[x['title'][0:len(x['title'])-1] for x in dict_da if
        x['title']!='' and x['poster']!='' and x['trailer']['link']!='' and x['rating'] != '' and x[
                  'plot'] != '']
    posters = [x['poster'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    trailer_links = [x['trailer']['link'] for x in dict_data if
                     x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                         'plot'] != '']
    ratings = [x['rating'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    plots = [x['plot'] for x in dict_data if
             x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                 'plot'] != '']

    #print(titles)
    # print(len(ratings))
    # print(len(posters))

    context = [{'title': title, 'poster': poster, 'rating': rating, 'plot': plot, 'trailer': trailer} for
               title, poster, rating, plot, trailer in zip(titles, posters, ratings, plots, trailer_links)]
    return context


def index(request):
    context = dict_data()
    return render(request,"index.html",{"data":context})