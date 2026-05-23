import requests


BASE_URL = "https://api.adsb.lol/v2/point"

def get_nearby_aircraft(location):
    lat = location["lat"]
    lon = location["lon"]
    radius = location["radius_nm"]

    url = f"{BASE_URL}/{lat}/{lon}/{radius}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json()

    raw_aircraft_list = data.get("ac", [])
    simplified_aircraft_list = []

    for raw_aircraft in raw_aircraft_list:
        simplified_aircraft = normalize_aircraft(raw_aircraft)
        simplified_aircraft_list.append(simplified_aircraft)
    
    return simplified_aircraft_list

def normalize_aircraft(raw_aircraft):
    altitude_ft = raw_aircraft.get("alt_baro")
    speed_knots = raw_aircraft.get("gs")
    distance_nm = raw_aircraft.get("dst")
    flight = raw_aircraft.get("flight")

    if altitude_ft is None:
        altitude_m = None
    else:
        altitude_m = round(feet_to_meters(altitude_ft))

    if speed_knots is None:
        speed_kmh = None
    else:
        speed_kmh = round(knots_to_kmh(speed_knots))

    if distance_nm is None:
        distance_km = None
    else:
        distance_km = round(nautical_miles_to_km(distance_nm))
    
    if flight is not None:
        flight = flight.strip()

    return  {
        "hex": raw_aircraft.get("hex"),          # Fingerprint of the aircraft
        "flight": flight,                        # Flight (eg. AZUL2319) 
        "reg": raw_aircraft.get("r"),            # Aircraft Registration (eg PS-AEG) Brazillian registry
        "type": raw_aircraft.get("t"),           # Aircraft Type
        "altitude_ft": altitude_ft,
        "altitude_m": altitude_m,
        "speed_kmh": speed_kmh,
        "vertical_rate": raw_aircraft.get("baro_rate"),         
        "distance_km": distance_km,
        "seen": raw_aircraft.get("seen"),
    }


def knots_to_kmh(knots):
    return knots * 1.852



def feet_to_meters(feet):
    return feet * 0.3048



def nautical_miles_to_km(nm):
    return nm * 1.852