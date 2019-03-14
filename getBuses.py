'''CATFORD ROAD/LEWISHAM TOWN HALL BUS TIMES APP BACKEND'''

#stop naptan ids: 490009117T, 490009117V

import requests #http module to get json data

def getBuses():
    #get bus stop arrival predictions
    requestT, requestV = requests.get('https://api.tfl.gov.uk/StopPoint/490009117T/Arrivals'), requests.get('https://api.tfl.gov.uk/StopPoint/490009117V/Arrivals')
    requestT, requestV = requestT.json(), requestV.json()

    #organise bus destinations
    destinations = {}

    #organise bus arrival info
    stopT, stopV = {}, {}

    #get number of buses coming to both stops
    busesComing = 0
    if len(requestT) > busesComing:
        busesComing = len(requestT)
    if len(requestV) > busesComing:
        busesComing = len(requestV)

    #gets all arriving buses and appends them to a dictionary with expectedArrival as key
    for bus in range(busesComing):
        try:
            if requestT[bus]["lineName"] not in destinations:
                destinations[requestT[bus]["lineName"]] = requestT[bus]["destinationName"]
        except:
            pass
        try:
            if requestV[bus]["lineName"] not in destinations:
                destinations[requestV[bus]["lineName"]] = requestV[bus]["destinationName"]
        except:
            pass

        try:
            if requestT[bus]["lineName"] not in stopT:
                stopT[requestT[bus]["lineName"]] = [requestT[bus]["expectedArrival"][11:16]]
            else:
                stopT[requestT[bus]["lineName"]].append(requestT[bus]["expectedArrival"][11:16])
        except:
            pass
        try:
            if requestV[bus]["lineName"] not in stopV:
                stopV[requestV[bus]["lineName"]] = [requestV[bus]["expectedArrival"][11:16]]
            else:
                stopV[requestV[bus]["lineName"]].append(requestV[bus]["expectedArrival"][11:16])
        except:
            pass

    return destinations, stopT, stopV