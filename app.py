from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)


client = MongoClient()
db = client.Playlister
# playlists = db.playlists


# @app.route('/')
# def index():
#     """Return homepage."""
#     return render_template('home.html', msg='Flask is Cool!!')


# OUR MOCK ARRAY OF PROJECTS
playlists = [
    {'title': 'Great Playlist'},
    {'title': 'Next Playlist'}
]


@app.route('/')
def playlists_index():
    """Show all playlists."""
    for item in playlists:
        print(item)
    return render_template('playlists_index.html', playlists=playlists.find())


if __name__ == '__main__':
    app.run(debug=True)
