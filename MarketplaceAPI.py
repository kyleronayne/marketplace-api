from flask import Flask, jsonify, request
import MarketplaceScraper

API = Flask(__name__)


@API.route("/location-ids", methods=["GET"])
def getLocationIDs():
    location = request.args.get("location")
    return MarketplaceScraper.getLocationIDs(location=location)
