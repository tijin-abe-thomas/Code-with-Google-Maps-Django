import datetime

import requests
from django.shortcuts import render

import googlemaps
import populartimes

# Create your views here.
def index(request):
    API_KEY = open("API_KEY","r").read()
    #Documentation of the client: https://googlemaps.github.io/google-maps-services-python/docs/index.html#module-googlemaps
    gmaps = googlemaps.Client(key=API_KEY)

    #We have to take input (type of establishment), add this to the type attribute of the req.
    #Accepted Types are there in this documentation: https://developers.google.com/maps/documentation/places/web-service/supported_types#table1
    #API Call Doc: https://googlemaps.github.io/google-maps-services-python/docs/index.html#googlemaps.Client.places
    query_response = gmaps.places(type="<Enter query like resto, etc.>")
    #This is ideally supposed to be giving place id as the response
    #(Haven't tested it out :lol)

    #Approach 1: We don't have much work in terms of getting popular times here
    #Syntax of popular times lib: https://github.com/m-wrzr/populartimes#populartimesget
    response = populartimes.get(api_key=API_KEY, types=["<Enter type like resto, airport etc.>"], p1=(48.132986, 11.566126), p2=(48.142199, 11.580047))
    #It is ideally supposed to be giving me a combined popular times data of all such establishments in the region

    #Approach 2 
    #Syntax of popular times lib: https://github.com/m-wrzr/populartimes#populartimesget_id
    response = populartimes.get_id(api_key=API_KEY, place_id=query_response)
    #This takes 2x the API calls but essentially does the same thing as the first approach.
    #All the client work is under the hood prolly. We can look at source code and figure something out maybe?
    
    #Hotel Rates (How to figure out the Hotel prices?)
    #Hotel APIs are REST APIs.. to use with python (little complex ig? Maybe we can try it with requests)
    #Worst case, if this doesnt work, we can use this popular times API to extract time_spent and then figure out whats the churn 
    #(Assumption: more time a customer spends in a shop, more likely he is to purchase a product)

    
    #HeatMaps
    #Now to do the actual visulatisation, heatmaps are only visible in Javascript :FacePalm
    #https://developers.google.com/maps/documentation/javascript/heatmaplayer



