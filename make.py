#!/usr/bin/python
import requests # We'll use this for API calls to Flickr.

flickr_api_key = '' # You'll want to fill this in yourself.
try:
    keyfile = open('flickrapi.key', 'r')
    flickr_api_key = keyfile.readline()
except:
    pass
assert flickr_api_key != '', "You need to add your Flickr API key to the code. Do not commit it."

def getOutline(place_id = None, woe_id = None):
    # https://www.flickr.com/services/api/flickr.places.getInfo.html
    # Required args: api_key and place_id or woe_id
    errors = {
        1: "Required parameter missing:
            One or more required parameter is missing from the API call.",
        2: "Not a valid Places ID:
        An invalid Places (or WOE) ID was passed with the API call.",
        3: "Place not found:
        No place could be found for the Places (or WOE) ID passed to the API call."
        100: "Invalid API Key:
        The API key passed was not valid or has expired."
        105: "Service currently unavailable:
        The requested service is temporarily unavailable."
        106: "Write operation failed:
        The requested operation failed due to a temporary issue."
        111: "Format 'xxx' not found:
        The requested response format was not found."
        112: "Method 'xxx' not found:
        The requested method was not found."
        114: "Invalid SOAP envelope:
        The SOAP envelope send in the request could not be parsed."
        115: "Invalid XML-RPC Method Call:
        The XML-RPC request document could not be parsed."
        116: "Bad URL found:
        One or more arguments contained a URL that has been used for abuse on Flickr."}
    payload = { "api_key": flickr_api_key, "place_id" = place_id, "woe_id": woe_id}
    r = requests.post(URL, params=payload)
    r.text # The response
