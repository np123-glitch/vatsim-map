# VATSIM Map Project

## Overview

The VATSIM Map Project is a web application that provides a real-time map displaying the locations of pilots connected to the Virtual Air Traffic Simulation Network (VATSIM). The map uses Leaflet, an open-source JavaScript library for interactive maps, to visualize the positions of aircraft, including their names, altitudes, and headings.

## Features

- **Real-time Updates:** The map dynamically updates every 15 seconds to reflect the latest positions of VATSIM pilots.
- **Aircraft Information:** Clicking on an aircraft marker reveals detailed information such as the pilot's name, altitude, and heading.
- **Custom Aircraft Icons:** Each aircraft is represented by a custom icon that includes a rotation feature to indicate the aircraft's heading.

## Project Structure

- **Flask App (app.py):** The Flask application serves as the backend, providing routes for updating pilot data and serving the aircraft icon image.
- **Leaflet Map (index.html):** The frontend contains an HTML file with Leaflet integration, displaying the map and handling real-time updates.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/vatsim-map.git
    cd vatsim-map
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:

    ```bash
    python app.py
    ```

    Visit `http://127.0.0.1:80` in your browser to view the VATSIM map.

## Configuration

- **Update Interval:** The map updates every 15 seconds (adjustable in the JavaScript code).

## Credits

- **Leaflet:** [Leaflet](https://leafletjs.com/) is an open-source JavaScript library for interactive maps.
- **VATSIM Data API:** The project fetches real-time pilot data from the VATSIM Data API.

## License

This project is licensed under the [MIT License](LICENSE).
