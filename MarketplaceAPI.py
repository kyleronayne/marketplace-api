from flask import Flask, request
import MarketplaceScraper

API = Flask(__name__)


@API.route("/locations", methods=["GET"])
def locations():
    response = {}

    # Required parameters provided by the user
    locationSearchQuery = request.args.get("searchQuery")

    if (locationSearchQuery):
        status, error, data = MarketplaceScraper.getLocations(
            locationSearchQuery=locationSearchQuery)
    else:
        status = "Failure"
        error["source"] = "User"
        error["message"] = "Missing required parameter"
        data = {}

    response["status"] = status
    response["error"] = error
    response["data"] = data

    return response


@API.route("/listings", methods=["GET"])
def listings():
    response = {}

    # Required parameters provided by user
    locationLatitude = request.args.get("locationLatitude")
    locationLongitude = request.args.get("locationLongitude")
    itemSearchQuery = request.args.get("searchQuery")

    if (locationLatitude and locationLongitude and itemSearchQuery):
        status, error, data = MarketplaceScraper.getListings(
            locationLatitude=locationLatitude, locationLongitude=locationLongitude, itemSearchQuery=itemSearchQuery)
    else:
        status = "Failure"
        error["source"] = "User"
        error["message"] = "Missing required paramter(s)"
        data = {}

    response["status"] = status
    response["error"] = error
    response["data"] = data

    return response
