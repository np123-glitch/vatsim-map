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

    # Extract relevant pilot information (name, latitude, longitude, departure, arrival, route)
    global pilots_info
    pilots_info = []

    for pilot in data['pilots']:
        pilot_info = {
            'name': pilot['name'][:-4],  # Truncate the last 4 characters from the 'name' field
            'lat': pilot['latitude'],
            'lon': pilot['longitude'],
            'alt': pilot['altitude'],
            'heading': pilot['heading'],
            'transponder': pilot['transponder'],
            'departure': '',
            'arrival': '',
            'route': ''
        }

        flight_plan = pilot.get('flight_plan')

        if flight_plan:
            pilot_info['departure'] = flight_plan.get('departure', '')
            pilot_info['arrival'] = flight_plan.get('arrival', '')
            pilot_info['route'] = flight_plan.get('route', '')

        pilots_info.append(pilot_info)

    return jsonify(pilots_info)

@app.route('/img')
def img():
    image_path = 'C:/Users/sachi/Downloads/_Untitled design_inPixioedited.png'
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
