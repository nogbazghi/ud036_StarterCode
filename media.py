import webbrowser

#this is the movie object, contains the constructor, with the different attributes needed to describe the movie
#These attributes will then be used by fresh_tomatoes
class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.movie_title = title
        self.movie_storyline = storyline
        self.movie_poster_image_url = poster_image
        self.movie_trailer_youtube_url = trailer_youtube
    #displays the trailer
    def show_trailer(self):
        webbrowser.open(self.movie_trailer_youtube_url)