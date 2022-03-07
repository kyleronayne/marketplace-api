from requests_html import HTMLSession
import json

GRAPHQL_URL = "https://www.facebook.com/api/graphql/"


def getLocationIDs(location):
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

        # Get location names and location ids from the facebook response
        for location in facebookResponseJSON["data"]["city_street_search"]["street_results"]["edges"]:
            locationName = location["node"]["single_line_address"]
            locationID = location["node"]["page"]["id"]
            data.append({locationName: locationID})
    else:
        statusMessage = "Failure: Facebook response status code %d" % facebookResponse.status_code

    return (statusMessage, data)
