from requests_html import HTMLSession
import json

GRAPHQL_URL = "https://www.facebook.com/api/graphql/"


def getLocationIDs(location):
    locationIDs = {}
    requestHeaders = {"sec-fetch-site": "same-origin"}
    requestPayload = {
        "variables": """{"params": {"caller": "MARKETPLACE", "country_filter": "null", "page_category": ["CITY", "SUBCITY", "NEIGHBORHOOD","POSTAL_CODE"], "query": "%s", "search_type": "PLACE_TYPEAHEAD"}}""" % (location),
        "doc_id": "5585904654783609"
    }
    requestSession = HTMLSession()

    response = requestSession.post(
        GRAPHQL_URL, headers=requestHeaders, data=requestPayload)
    responseJSON = json.loads(response.text)

    for location in responseJSON["data"]["city_street_search"]["street_results"]["edges"]:
        locationName = location["node"]["single_line_address"]
        locationID = location["node"]["page"]["id"]
        locationIDs[locationName] = locationID

    return locationIDs
