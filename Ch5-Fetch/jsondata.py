#
# parsing and processing JSON
# json data url: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson
# json encoder and decoder: https://docs.python.org/3/library/json.html
#

import urllib.request
import json
import ssl

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])   # USGS Magnitude 2.5+ Earthquakes, Past Hour
        
    # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(count, "events recorded")           # 1 events recorded
    
    # for each event, print the place where it occured ( features property is an array )
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("-----------------------------\n")
    
    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print(i["properties"]["mag"])
    print("-----------------------------\n")
    
    # print only the events where at least 1 person reported feeling something
    print("\nEvents that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(i["properties"]["place"], feltReports, "times")


def main():
    # define a variable to hold the source URL
    # In this case, we'll use the free data from UGSG
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    # urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"
    
    # Open the URL and read the data
    context = ssl._create_unverified_context()
    webUrl = urllib.request.urlopen(urlData, context=context)
    print("result code:", str(webUrl.getcode()))
    
    # Print out data if the http status code 200
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error from the server, cannot print results", webUrl.getcode())

if __name__ == "__main__":
  main()