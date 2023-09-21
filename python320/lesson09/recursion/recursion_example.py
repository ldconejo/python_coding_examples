import json

def load_airport_data(source_file):
    with open(source_file, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)
    return data

def get_airport_id(iata_code, data):
    for airport in data:
        if airport['IATA/FAA'] == iata_code:
            return airport['Airport ID']
'''
origin_id: Starting airport ID
destination_id: Final airport ID
max_hops: Maximum number of flights to go from origin to destination
'''
def search_routes(origin_id, destination_id, max_hops, current_hops, data, route_string):
    # Are we there yet?
    if origin_id == destination_id:
        route_string = route_string + "," + destination_id # 32432, 4324, 3243
        print(decode_route(route_string, data))
    # If we're not there yet, have we exceeded the maximum number of stops (hops)?
    elif max_hops > current_hops:
        current_hops += 1
        for airport in data:
            if airport['Airport ID'] == origin_id:
                # If we are just starting to look for routes
                if route_string == '':
                    route_string = origin_id
                else:
                    route_string = route_string + "," + origin_id
                destinations = airport['destinations']
                # Each destination from the current airport will be the new origin
                # for the recursion call to search_routes()
                for destination in destinations:
                    search_routes(destination, destination_id, max_hops, current_hops, data, route_string)
    # If we are already over max_hops and we're not at the destination, just drop the route.


def decode_route(route_string, data):
    route_list = route_string.split(',')
    airport_list = []
    for airport_id in route_list:
        for airport in data:
            if airport['Airport ID'] == airport_id:
                airport_list.append(airport['City'])
    return airport_list

if __name__ == '__main__':
    data = load_airport_data('airports.txt')
    origin_code = input('Enter the starting airport IATA code: ')
    origin_id = get_airport_id(origin_code, data)

    destination_code = input('Enter the destination airport IATA code: ')
    destination_id = get_airport_id(destination_code, data)

    max_hops = int(input('How many stops? '))

    search_routes(origin_id, destination_id, max_hops, 0, data, '')

