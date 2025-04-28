
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/routes')
def routes():
    return jsonify([
        {
            "label": "least_loaded",
            "totalTime": 1200,
            "totalLoad": 30,
            "segments": [
                {"startLat": 43.234, "startLng": 42.512, "endLat": 43.235, "endLng": 42.513, "load": 10},
                {"startLat": 43.235, "startLng": 42.513, "endLat": 43.238, "endLng": 42.516, "load": 20}
            ]
        }
    ])

app.run(port=5000)
