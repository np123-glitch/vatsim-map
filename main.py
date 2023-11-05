from flask import Flask, render_template, jsonify, send_file
import requests

app = Flask(__name__)

# Store pilot data globally for simplicity (in a real app, you might want to use a database)
pilots_info = []

@app.route('/')
def index():
    return render_template('index.html', pilots_info=pilots_info)

@app.route('/update_pilots')
def update_pilots():
    # Fetch pilot data from the API
    url = 'https://data.vatsim.net/v3/vatsim-data.json'
    response = requests.get(url)
    data = response.json()

    # Extract relevant pilot information (name, latitude, longitude)
    global pilots_info
    pilots_info = [
        {
            'name': pilot['name'],
            'lat': pilot['latitude'],
            'lon': pilot['longitude'],
            'alt': pilot['altitude'],
             'heading': pilot['heading']
        }
        for pilot in data['pilots']
    ]

    return jsonify(pilots_info)

@app.route('/img')
def img():
    image_path = 'C:/Users/sachi/Downloads/_Untitled design_inPixio.png'
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
