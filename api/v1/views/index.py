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