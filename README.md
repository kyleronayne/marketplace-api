# Marketplace API

An easy-to-use Facebook Marketplace API. Leverages the Facebook GraphQL API to allow for quick and easy retrieval of Facebook Marketplace listings and other relevant Marketplace data.
<br><br>
## Responses
---
**All** endpoints will return a JSON response in the following format:
```js
{
    "statusMessage": String,
    "data": Array
}
```
```statusMessage```: A description of the request status. Successful requests will receive a status message equal to "Success". Failed requests will receive a message containing "Failure", followed by an explanation.
<br><br>
```data```: A list of JSON objects representing the information an endpoint retrieves. An empty data value and a successful status message indicates that there was no available information to retrieve.
<br><br>
## Endpoints
---
- ```/location-coordinates```<br>
  *Response:*<br>
  Locations and their latitude and longitude points for exact, or close matches, to the location provided. Location coordinates are needed to find Marketplace listings in specific areas.<br><br>
  Example:
  ```json
  {
    "statusMessage": "Success", 
    "data": [
        {"Chicago, Illinois": 
            {"latitude": 41.883222, "longitude": -87.632496}},
        {"Chicago Lawn": 
            {"latitude": 41.771827, "longitude": -87.695848}},
        {"South Chicago": 
            {"latitude": 41.740721, "longitude": -87.552392}},
        {"West Chicago, Illinois":
            {"latitude": 41.8884, "longitude": -88.2097}}
    ]
  }
  ```
  <br><br>
  *Required Parameters:*<br>
  A location to find latitude and longitude points for.
  ```js
  "location": String
  ```