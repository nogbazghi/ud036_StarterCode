#imported the media file to access the Movie class
#imported the fresh_tomatoes file to pass the Movie objects to the file, in order to display on the html file
import media
import fresh_tomatoes

# I created a Movie instance for each movie and assigned them to a variable
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=vwyZH85NQC4")
black_panther = media.Movie("Black Panther",
                            "A story about the black panther",
                            "https://ia.media-imdb.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=dxWvtMOGAhw")
star_wars = media.Movie("Star Wars",
                        "most recent star wars movie",
                        "https://ia.media-imdb.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")
moonlight = media.Movie("Moonlight",
                        "A boy struggling with his sexuality",
                        "https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png",
                        "https://www.youtube.com/watch?v=9NJj12tJzqc")

# I placed the movies in a list, which I then passed to the fresh_tomatoes file
movies = [toy_story, black_panther, star_wars, moonlight]
fresh_tomatoes.open_movies_page(movies)
