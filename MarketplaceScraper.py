from requests_html import HTMLSession
import json

GRAPHQL_URL = "https://www.facebook.com/api/graphql/"


def getLocationCoordinates(location):
    # Return values
    statusMessage = ""
    data = []

    requestHeaders = {"sec-fetch-site": "same-origin"}
    requestPayload = {
        "variables": """{"params": {"caller": "MARKETPLACE", "page_category": ["CITY", "SUBCITY", "NEIGHBORHOOD","POSTAL_CODE"], "query": "%s"}}""" % (location),
        "doc_id": "5585904654783609"
    }
    requestSession = HTMLSession()

    facebookResponse = requestSession.post(
        GRAPHQL_URL, headers=requestHeaders, data=requestPayload)

    if (facebookResponse.status_code == 200):
        statusMessage = "Success"
        facebookResponseJSON = json.loads(facebookResponse.text)

        # Get location names and their latitude and longitude from the facebook response
        for location in facebookResponseJSON["data"]["city_street_search"]["street_results"]["edges"]:
            locationName = location["node"]["single_line_address"]
            latitude = location["node"]["location"]["latitude"]
            longitude = location["node"]["location"]["longitude"]
            data.append({
                locationName: {
                    "latitude": latitude,
                    "longitude": longitude
                }
            })
    else:
        statusMessage = "Failure: Facebook response status code %d" % facebookResponse.status_code

    return (statusMessage, data)


def getListings(latitude, longitude):
    statusMessage = ""
    data = []
