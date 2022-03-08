from flask import Flask, request
import MarketplaceScraper

API = Flask(__name__)


@API.route("/location-coordinates", methods=["GET"])
def locationCoordinates():
    response = {}

    # Required location parameter provided by the user
    location = request.args.get("location")

    if (location):
        statusMessage, data = MarketplaceScraper.getLocationCoordinates(
            location=location)
    else:
        statusMessage = "Failure: No location parameter provided"
        data = []

    response = {
        "statusMessage": statusMessage,
        "data": data
    }

    response["statusMessage"] = statusMessage
    response["data"] = data

    return response