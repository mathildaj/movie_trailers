"""
Created on Fri Oct 27 13:40:24 2017

@author: Ying
"""
import webbrowser


class Movie():
    """This is the Movie class

    Attributes:
        title(string): title of the movie
        storyline(string): brief description of the movie
        poster_image_url(string): the url of a poster image for the movie
        trailer_youtube_url(string): the url of the movie trailer

    Mehthods:
        show_trailer(self): opens a browser showing the movie trailer
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
