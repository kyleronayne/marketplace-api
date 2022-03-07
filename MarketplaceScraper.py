from requests_html import HTMLSession
import json

GRAPHQL_URL = "https://www.facebook.com/api/graphql/"


def getLocationIDs(location):
    response = {"statusCode": "",
                "statusMessage": "",
                "data": []}

    requestHeaders = {"sec-fetch-site": "same-origin"}
    requestPayload = {
        "variables": """{"params": {"caller": "MARKETPLACE", "country_filter": "null", "page_category": ["CITY", "SUBCITY", "NEIGHBORHOOD","POSTAL_CODE"], "query": "%s", "search_type": "PLACE_TYPEAHEAD"}}""" % (location),
        "doc_id": "5585904654783609"
    }
    requestSession = HTMLSession()

    facebookResponse = requestSession.post(
        GRAPHQL_URL, headers=requestHeaders, data=requestPayload)
    response["statusCode"] = facebookResponse.status_code

    if (facebookResponse.status_code == 200):
        response["statusMessage"] = "success"
        facebookResponseJSON = json.loads(facebookResponse.text)

        # Get location names and location ids from the facebook response
        for location in facebookResponseJSON["data"]["city_street_search"]["street_results"]["edges"]:
            locationName = location["node"]["single_line_address"]
            locationID = location["node"]["page"]["id"]
            response["data"].append({locationName: locationID})

    return response
