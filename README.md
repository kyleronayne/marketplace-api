# Marketplace API

An easy-to-use Facebook Marketplace API. Wraps the Facebook GraphQL API, allowing for quick and easy retrieval of Facebook Marketplace listings and other relevant Marketplace data.
<br><br>
## Responses
**All** endpoints will return a JSON response in the following format:
```js
{
    "status": String,
    "error": {
        "source": String,
        "message": String
    },
    "data": Array
}
```
```status```: Indicates whether a request was a success or failure. Successful requests will have a status of "Success" and failed requests will have a status of "Failure".
<br>

```error```: A request error (will be empty if no error exists).
- ```error.source```: Indicates the party responsible for an error. Server-side Facebook errors will have a source of "Facebook" and errors caused by the user will have a source of "User".
- ```error.message```: A detailed description of the request error.
<br>

```data```: A list of JSON objects representing the information an endpoint retrieved (will be empty if an error exists).
<br><br>
## Endpoints
- ```/locations```<br>
  *Response:*<br>
  Locations which are exact, or close matches, to the search query location provided. Latitude and longitude coordinates for a location are required to find Marketplace listings in a targeted area.<br><br>
  Example:
  ```json
  {
      "status": "Success",
      "error": {},
      "data": {
          "locations": [
              {
                  "name": "Houston, Texas",
                  "latitude": 29.7602,
                  "longitude": -95.3694
              },
              {
                  "name": "Downtown Houston, TX",
                  "latitude": 29.758767,
                  "longitude": -95.361523
              },
              {
                  "name": "Houston, Mississippi",
                  "latitude": 33.8981,
                  "longitude": -89.0017
              },
              {
                  "name": "Houston, Alaska",
                  "latitude": 61.6083,
                  "longitude": -149.774
              }
          ]
      }
  }
  ```
  <br>

  *Required Parameters:*<br>
  A location in which to find the latitude and longitude coordinates.
  ```js
  "searchQuery": String
  ```
---