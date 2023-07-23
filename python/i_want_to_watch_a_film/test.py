import requests
from bs4 import BeautifulSoup

def get_movie_duration(key, movie_title):
    search_url = "http://www.omdbapi.com/?apikey=" + key + "&t=" + movie_title
    
    response = requests.get(search_url)
    infosMovie = response.json()
    if infosMovie["Response"] == 'True' :
        duration = infosMovie["Runtime"].split()
        if int(duration[0]) > 60 :
            hours, min = divmod(int(duration[0]), 60)
            duration = str(hours) + " h " + str(min) + " min"
        else:
            duration = infosMovie["Runtime"]
        rating = infosMovie["imdbRating"]
        year = infosMovie["Year"]
        print(f"The movie '{movie_title}': Time = {duration} / Rating = {rating} / Year = {year}")
    else:
        print(f"Unable to retrieve the movie '{movie_title}'.")

# Example usage
# API key
key = "9c446ee0"
# Movie Name
movie_title = input("Tape le nom du film que tu veux chercher : \n")
# Use function
get_movie_duration(key, movie_title)