from connectSQL import *
from read_films import *


def film_insert():
    films = []

    film_title = input("Enter a movie title.\n")
    film_year = int(input("Enter the year the movie was released.\n"))
    film_rating = input("Enter the movie rating: G for General Audience, PG for Parental Guidance, R for Restricted.\n")
    film_duration = int(input("Enter the duration of the movie, in minutes.\n"))
    film_genre = input("Enter the genre of movie. Select from: Action, Animation, Comedy, Crime, Fantasy, Fighting, Sci-fi, Test\n")

    film_title = film_title.title()
    film_rating = film_rating.upper()
    film_genre = film_genre.title()
    
    films.append(film_title)
    films.append(film_year)
    films.append(film_rating)
    films.append(film_duration)
    films.append(film_genre)

    cursor.execute("Insert into tblFilms (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)", films)

    conn.commit()
    print(f"{film_title} has been added to the table.\n\n")
    

    read()
    
if __name__ == '__main__':
    film_insert()
    