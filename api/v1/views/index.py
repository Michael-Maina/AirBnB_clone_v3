#!/usr/bin/python3
"""
Initializes status and statistics of objects
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route("/stats")
def stats():
    response = {"amenities": storage.count(Amenity),
                "cities": storage.count(City),
                "places": storage.count(Place),
                "reviews": storage.count(Review),
                "states": storage.count(State),
                "users": storage.count(User)}
    return jsonify(response)
