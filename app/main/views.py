from flask import render_template
from app import app
from .request import get_movies

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
     # Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template('index.html', message = message)