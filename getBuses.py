import requests #http module to get json data

######'https://api.tfl.gov.uk/StopPoint/490009117T/Arrivals'

def getBuses(requestLink):
    #get bus stop arrival prediction
    request = requests.get(requestLink).json()

    #organise bus destinations
    destinations = {}

    #organise bus arrival info
    stop = {}

    #gets all arriving buses and appends them to a dictionary with expectedArrival as key
    for bus in range(len(request)):
        try:
            if request[bus]["lineName"] not in destinations:
                destinations[request[bus]["lineName"]] = request[bus]["destinationName"]
        except:
            pass

        try:
            if request[bus]["lineName"] not in stop:
                stop[request[bus]["lineName"]] = [round(request[bus]["timeToStation"]/60)]
            else:
                stop[request[bus]["lineName"]].append(round(request[bus]["timeToStation"]/60))
        except:
            pass

    #organise bus times by first arrival
    ordered = []
    for key in stop:
        for item in stop[key]:
            ordered.append({'bus': key, 'time': item})
    ordered = sorted(ordered, key=lambda x: x['time'])

    stop = {}
    for item in ordered:
        if item['bus'] not in stop:
            stop[item['bus']] = [item['time']]
        else:
            stop[item['bus']].append(item['time'])

    return stop, destinations
