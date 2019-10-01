from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for

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


@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))


@app.route('/playlists/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html')


if __name__ == '__main__':
    app.run(debug=True)
