"""
Created on Fri Oct 27 13:42:12 2017

@author: Ying
"""
import fresh_tomatoes
import media

# create a list of movies
movies = []

# read all movies from a text file, one line for each movie, separated by comma
with open("movies.txt") as fp:
    for line in fp:
        movie_info = line.split(",")
        # create a new instance of the Movie class
        if(len(movie_info) == 4):
            new_movie = media.Movie(movie_info[0],
                                    movie_info[1],
                                    movie_info[2],
                                    movie_info[3])
            # add the new movie to the list
            movies.append(new_movie)

fresh_tomatoes.open_movies_page(movies)


