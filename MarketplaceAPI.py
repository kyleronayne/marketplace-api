from flask import Flask, request
import MarketplaceScraper

API = Flask(__name__)


@API.route("/locations", methods=["GET"])
def locations():
    response = {}

    # Required parameters provided by the user
    locationQuery = request.args.get("locationQuery")

    if (locationQuery):
        status, error, data = MarketplaceScraper.getLocations(
            locationQuery=locationQuery)
    else:
        status = "Failure"
        error["source"] = "User"
        error["message"] = "Missing required parameter"
        data = {}

    response["status"] = status
    response["error"] = error
    response["data"] = data

    return response


@API.route("/search", methods=["GET"])
def search():
    response = {}

    # Required parameters provided by user
    locationLatitude = request.args.get("locationLatitude")
    locationLongitude = request.args.get("locationLongitude")
    listingQuery = request.args.get("listingQuery")

    if (locationLatitude and locationLongitude and listingQuery):
        status, error, data = MarketplaceScraper.getListings(
            locationLatitude=locationLatitude, locationLongitude=locationLongitude, listingQuery=listingQuery)
    else:
        status = "Failure"
        error["source"] = "User"
        error["message"] = "Missing required parameter(s)"
        data = {}

    response["status"] = status
    response["error"] = error
    response["data"] = data

    return response
