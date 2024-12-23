from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests, os

app = Flask(__name__, static_folder='static')
CORS(app)

API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'

def fetch(endpoint, params=None):
    params = params or {}
    params['api_key'] = API_KEY
    r = requests.get(f"{BASE_URL}/{endpoint}", params=params)
    return r.json() if r.status_code == 200 else {"error": "Failed", "status": r.status_code}

@app.route('/search', methods=['GET'])
def search():
    q = request.args.get('query', '')
    if not q:
        return jsonify({"error": "Missing query"}), 400
    params = {'query': q}
    movies = fetch('search/movie', params).get('results', [])
    tv_shows = fetch('search/tv', params).get('results', [])
    for m in movies: m['media_type'] = 'movie'
    for t in tv_shows: t['media_type'] = 'tv'
    return jsonify({"results": movies + tv_shows})

@app.route('/<media>/popular', methods=['GET'])
def popular(media):
    if media not in ['movie', 'tv']:
        return jsonify({"error": "Invalid media type"}), 400
    page = request.args.get('page', 1, type=int)
    data = fetch(f'{media}/popular', {'page': page})
    for item in data.get('results', []): item['media_type'] = media
    return jsonify(data)

@app.route('/<media>/<int:id>', methods=['GET'])
def details(media, id):
    if media not in ['movie', 'tv']:
        return jsonify({"error": "Invalid media type"}), 400
    return jsonify(fetch(f'{media}/{id}'))

@app.route('/tv/<int:id>/season/<int:season>', methods=['GET'])
def season(id, season):
    return jsonify(fetch(f'tv/{id}/season/{season}'))

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/details')
def serve_details():
    return send_from_directory(app.static_folder, 'details.html')

@app.route('/watch')
def serve_watch():
    return send_from_directory(app.static_folder, 'watch.html')

@app.route('/logo.png')
def serve_icon():
    return send_from_directory(app.static_folder, 'logo.png')

if __name__ == '__main__':
    app.run(debug=True)