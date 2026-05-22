AIRPORTS = {
    "confins": {
        "name": "Tancredo Neves International Airport [CNF]",
        "lat": -19.6244,
        "lon": -43.9719,
        "radius_nm": 50,
        "aliases": ["cnf", "cnfs", "confins"]
    },
    "pampulha": {
        "name": "Pampulha Carlos Drummond de Andrade Airport - [PLU]",
        "lat": -19.8512,
        "lon": -43.9506,
        "radius_nm": 30,
        "aliases": ["plu", "pampulha"]
    },
    "guarulhos": {
        "name": "Governor André Franco Montoro International Airport - [GRU]",
        "lat": -23.4356,
        "lon": -46.4731,
        "radius_nm": 50,
        "aliases": ["gru", "guarulhos"]
    },
}


CITIES = {
    "belo_horizonte": {
        "type": "city",
        "name": "Belo Horizonte | MG",
        "lat": -19.9167,
        "lon": -43.9345,
        "radius_nm": 70,
        "aliases": ["bh", "belo horizonte", "belohorizonte"],
    },
}



def get_airport(airport):
    for key, airport_data in AIRPORTS.items():
        if airport in airport_data["aliases"]:
            return airport_data
    return None


def get_city(city):
    for key, city_data in CITIES.items():
        if city in city_data["aliases"]:
            return city_data
    return None


def get_raw(input_lat, input_lon, radius_nm=50):

    try:
        lat = float(input_lat)
        lon = float(input_lon)
        radius = float(radius_nm)
    
    except ValueError:
        return None


    if not -90 <= lat <= 90:
        return None

    if not -180 <= lon <= 180:
        return None

    if radius <= 0:
        return None


    return {
        "name": "Custom Coordinates",
        "lat": float(input_lat),
        "lon": float(input_lon),
        "radius_nm": float(radius_nm),
    }
