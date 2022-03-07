from flask import Flask, request
import MarketplaceScraper

API = Flask(__name__)


@API.route("/location-ids", methods=["GET"])
def locationIDs():
    location = request.args.get("location")
    return MarketplaceScraper.getLocationIDs(location=location)
