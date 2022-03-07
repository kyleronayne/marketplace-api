from flask import Flask, request
import MarketplaceScraper

API = Flask(__name__)


@API.route("/location-ids", methods=["GET"])
def locationIDs():
    response = {}

    # Required location parameter to be provided by the user
    location = request.args.get("location")

    if (location):
        statusMessage, data = MarketplaceScraper.getLocationIDs(
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