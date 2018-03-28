import webbrowser

#this is the movie object, contains the constructor, with the different attributes needed to describe the movie
#These attributes will then be used by fresh_tomatoes
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #displays the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)