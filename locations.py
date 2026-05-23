DEFAULT_RADIUS_NM = 100


AIRPORTS = {
    # Brazil
    "gru": {
        "name": "Sao Paulo/Guarulhos International Airport [GRU]",
        "lat": -23.4356,
        "lon": -46.4731,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["gru", "guarulhos", "sao paulo guarulhos", "sao paulo"],
    },
    "cgh": {
        "name": "Sao Paulo/Congonhas Airport [CGH]",
        "lat": -23.6267,
        "lon": -46.6554,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["cgh", "congonhas"],
    },
    "bsb": {
        "name": "Brasilia International Airport [BSB]",
        "lat": -15.8697,
        "lon": -47.9208,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["bsb", "brasilia", "df"],
    },
    "vcp": {
        "name": "Viracopos International Airport [VCP]",
        "lat": -23.0074,
        "lon": -47.1345,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["vcp", "viracopos", "campinas"],
    },
    "gig": {
        "name": "Rio de Janeiro/Galeao International Airport [GIG]",
        "lat": -22.8099,
        "lon": -43.2506,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["gig", "galeao", "rio galeao", "rio de janeiro"],
    },
    "cnf": {
        "name": "Tancredo Neves International Airport [CNF]",
        "lat": -19.6244,
        "lon": -43.9719,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["cnf", "cnfs", "confins", "belo horizonte"],
    },
    "sdu": {
        "name": "Santos Dumont Airport [SDU]",
        "lat": -22.9105,
        "lon": -43.1631,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["sdu", "santos dumont"],
    },
    "rec": {
        "name": "Recife/Guararapes International Airport [REC]",
        "lat": -8.1265,
        "lon": -34.9236,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["rec", "recife", "guararapes"],
    },
    "ssa": {
        "name": "Salvador Bahia Airport [SSA]",
        "lat": -12.9086,
        "lon": -38.3225,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["ssa", "salvador"],
    },
    "cwb": {
        "name": "Afonso Pena International Airport [CWB]",
        "lat": -25.5285,
        "lon": -49.1758,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["cwb", "curitiba", "afonso pena"],
    },
    "poa": {
        "name": "Salgado Filho International Airport [POA]",
        "lat": -29.9944,
        "lon": -51.1714,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["poa", "porto alegre", "salgado filho"],
    },
    "for": {
        "name": "Fortaleza/Pinto Martins International Airport [FOR]",
        "lat": -3.7763,
        "lon": -38.5326,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["for", "fortaleza", "pinto martins"],
    },
    "bel": {
        "name": "Belem/Val de Cans International Airport [BEL]",
        "lat": -1.3793,
        "lon": -48.4763,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["bel", "belem", "val de cans"],
    },
    "fln": {
        "name": "Florianopolis/Hercilio Luz International Airport [FLN]",
        "lat": -27.6705,
        "lon": -48.5477,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["fln", "florianopolis", "hercilio luz"],
    },
    "mao": {
        "name": "Manaus/Eduardo Gomes International Airport [MAO]",
        "lat": -3.0386,
        "lon": -60.0497,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["mao", "manaus", "eduardo gomes"],
    },
    "plu": {
        "name": "Pampulha Carlos Drummond de Andrade Airport [PLU]",
        "lat": -19.8512,
        "lon": -43.9506,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["plu", "pampulha"],
    },
    # South America outside Brazil
    "bog": {
        "name": "El Dorado International Airport [BOG]",
        "lat": 4.7016,
        "lon": -74.1469,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["bog", "bogota", "el dorado"],
    },
    "lim": {
        "name": "Jorge Chavez International Airport [LIM]",
        "lat": -12.0219,
        "lon": -77.1143,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["lim", "lima", "jorge chavez"],
    },
    "scl": {
        "name": "Santiago Arturo Merino Benitez Airport [SCL]",
        "lat": -33.3928,
        "lon": -70.7858,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["scl", "santiago", "arturo merino benitez"],
    },
    "aep": {
        "name": "Buenos Aires Aeroparque Jorge Newbery [AEP]",
        "lat": -34.5592,
        "lon": -58.4156,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["aep", "buenos aires", "aeroparque", "jorge newbery"],
    },
    "mde": {
        "name": "Jose Maria Cordova International Airport [MDE]",
        "lat": 6.1645,
        "lon": -75.4231,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["mde", "medellin", "jose maria cordova"],
    },
    # United States
    "atl": {
        "name": "Hartsfield-Jackson Atlanta International Airport [ATL]",
        "lat": 33.6407,
        "lon": -84.4277,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["atl", "atlanta", "hartsfield", "hartsfield jackson"],
    },
    "dfw": {
        "name": "Dallas Fort Worth International Airport [DFW]",
        "lat": 32.8998,
        "lon": -97.0403,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["dfw", "dallas", "fort worth", "dallas fort worth"],
    },
    "den": {
        "name": "Denver International Airport [DEN]",
        "lat": 39.8561,
        "lon": -104.6737,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["den", "denver"],
    },
    "ord": {
        "name": "Chicago O'Hare International Airport [ORD]",
        "lat": 41.9742,
        "lon": -87.9073,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["ord", "chicago", "ohare", "o'hare"],
    },
    "lax": {
        "name": "Los Angeles International Airport [LAX]",
        "lat": 33.9416,
        "lon": -118.4085,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["lax", "los angeles", "la"],
    },
    # Europe
    "lhr": {
        "name": "London Heathrow Airport [LHR]",
        "lat": 51.4700,
        "lon": -0.4543,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["lhr", "london", "heathrow", "london heathrow"],
    },
    "ist": {
        "name": "Istanbul Airport [IST]",
        "lat": 41.2753,
        "lon": 28.7519,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["ist", "istanbul"],
    },
    "cdg": {
        "name": "Paris Charles de Gaulle Airport [CDG]",
        "lat": 49.0097,
        "lon": 2.5479,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["cdg", "paris", "charles de gaulle"],
    },
    "ams": {
        "name": "Amsterdam Schiphol Airport [AMS]",
        "lat": 52.3105,
        "lon": 4.7683,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["ams", "amsterdam", "schiphol"],
    },
    "mad": {
        "name": "Adolfo Suarez Madrid-Barajas Airport [MAD]",
        "lat": 40.4983,
        "lon": -3.5676,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["mad", "madrid", "barajas"],
    },
    # Asia
    "dxb": {
        "name": "Dubai International Airport [DXB]",
        "lat": 25.2532,
        "lon": 55.3657,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["dxb", "dubai"],
    },
    "hnd": {
        "name": "Tokyo Haneda Airport [HND]",
        "lat": 35.5494,
        "lon": 139.7798,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["hnd", "tokyo", "haneda"],
    },
    "del": {
        "name": "Delhi Indira Gandhi International Airport [DEL]",
        "lat": 28.5562,
        "lon": 77.1000,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["del", "delhi", "indira gandhi"],
    },
    "can": {
        "name": "Guangzhou Baiyun International Airport [CAN]",
        "lat": 23.3924,
        "lon": 113.2988,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["can", "guangzhou", "baiyun"],
    },
    "pvg": {
        "name": "Shanghai Pudong International Airport [PVG]",
        "lat": 31.1443,
        "lon": 121.8083,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["pvg", "shanghai", "pudong"],
    },
}


CITIES = {
    # Brazil
    "sao_paulo": {
        "type": "city",
        "name": "Sao Paulo | SP",
        "lat": -23.5505,
        "lon": -46.6333,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["sp", "sao paulo", "saopaulo"],
    },
    "rio_de_janeiro": {
        "type": "city",
        "name": "Rio de Janeiro | RJ",
        "lat": -22.9068,
        "lon": -43.1729,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["rio", "rio de janeiro", "riodejaneiro"],
    },
    "brasilia": {
        "type": "city",
        "name": "Brasilia | DF",
        "lat": -15.7939,
        "lon": -47.8828,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["brasilia", "bsb"],
    },
    "belo_horizonte": {
        "type": "city",
        "name": "Belo Horizonte | MG",
        "lat": -19.9167,
        "lon": -43.9345,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["bh", "belo horizonte", "belohorizonte"],
    },
    "vespasiano": {
        "type": "city",
        "name": "Vespasiano | MG",
        "lat": -19.6919,
        "lon": -43.9233,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["vespasiano"],
    },
    "campinas": {
        "type": "city",
        "name": "Campinas | SP",
        "lat": -22.9099,
        "lon": -47.0626,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["campinas"],
    },
    "recife": {
        "type": "city",
        "name": "Recife | PE",
        "lat": -8.0476,
        "lon": -34.8770,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["recife"],
    },
    "salvador": {
        "type": "city",
        "name": "Salvador | BA",
        "lat": -12.9777,
        "lon": -38.5016,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["salvador"],
    },
    "curitiba": {
        "type": "city",
        "name": "Curitiba | PR",
        "lat": -25.4284,
        "lon": -49.2733,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["curitiba"],
    },
    "porto_alegre": {
        "type": "city",
        "name": "Porto Alegre | RS",
        "lat": -30.0346,
        "lon": -51.2177,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["porto alegre", "poa"],
    },
    "fortaleza": {
        "type": "city",
        "name": "Fortaleza | CE",
        "lat": -3.7319,
        "lon": -38.5267,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["fortaleza"],
    },
    # South America
    "bogota": {
        "type": "city",
        "name": "Bogota | Colombia",
        "lat": 4.7110,
        "lon": -74.0721,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["bogota", "bog"],
    },
    "lima": {
        "type": "city",
        "name": "Lima | Peru",
        "lat": -12.0464,
        "lon": -77.0428,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["lima", "lim"],
    },
    "santiago": {
        "type": "city",
        "name": "Santiago | Chile",
        "lat": -33.4489,
        "lon": -70.6693,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["santiago", "scl"],
    },
    "buenos_aires": {
        "type": "city",
        "name": "Buenos Aires | Argentina",
        "lat": -34.6037,
        "lon": -58.3816,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["buenos aires", "buenosaires", "aep"],
    },
    "medellin": {
        "type": "city",
        "name": "Medellin | Colombia",
        "lat": 6.2442,
        "lon": -75.5812,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["medellin", "mde"],
    },
    # United States
    "atlanta": {
        "type": "city",
        "name": "Atlanta | GA",
        "lat": 33.7490,
        "lon": -84.3880,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["atlanta", "atl"],
    },
    "dallas": {
        "type": "city",
        "name": "Dallas-Fort Worth | TX",
        "lat": 32.7767,
        "lon": -96.7970,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["dallas", "fort worth", "dfw"],
    },
    "denver": {
        "type": "city",
        "name": "Denver | CO",
        "lat": 39.7392,
        "lon": -104.9903,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["denver", "den"],
    },
    "chicago": {
        "type": "city",
        "name": "Chicago | IL",
        "lat": 41.8781,
        "lon": -87.6298,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["chicago", "ord"],
    },
    "los_angeles": {
        "type": "city",
        "name": "Los Angeles | CA",
        "lat": 34.0522,
        "lon": -118.2437,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["los angeles", "la", "lax"],
    },
    # Europe
    "london": {
        "type": "city",
        "name": "London | United Kingdom",
        "lat": 51.5072,
        "lon": -0.1276,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["london", "lhr"],
    },
    "istanbul": {
        "type": "city",
        "name": "Istanbul | Turkiye",
        "lat": 41.0082,
        "lon": 28.9784,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["istanbul", "ist"],
    },
    "paris": {
        "type": "city",
        "name": "Paris | France",
        "lat": 48.8566,
        "lon": 2.3522,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["paris", "cdg"],
    },
    "amsterdam": {
        "type": "city",
        "name": "Amsterdam | Netherlands",
        "lat": 52.3676,
        "lon": 4.9041,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["amsterdam", "ams"],
    },
    "madrid": {
        "type": "city",
        "name": "Madrid | Spain",
        "lat": 40.4168,
        "lon": -3.7038,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["madrid", "mad"],
    },
    # Asia
    "dubai": {
        "type": "city",
        "name": "Dubai | United Arab Emirates",
        "lat": 25.2048,
        "lon": 55.2708,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["dubai", "dxb"],
    },
    "tokyo": {
        "type": "city",
        "name": "Tokyo | Japan",
        "lat": 35.6762,
        "lon": 139.6503,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["tokyo", "hnd"],
    },
    "delhi": {
        "type": "city",
        "name": "Delhi | India",
        "lat": 28.6139,
        "lon": 77.2090,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["delhi", "del"],
    },
    "guangzhou": {
        "type": "city",
        "name": "Guangzhou | China",
        "lat": 23.1291,
        "lon": 113.2644,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["guangzhou", "can"],
    },
    "shanghai": {
        "type": "city",
        "name": "Shanghai | China",
        "lat": 31.2304,
        "lon": 121.4737,
        "radius_nm": DEFAULT_RADIUS_NM,
        "aliases": ["shanghai", "pvg"],
    },
}


def get_airport(airport):
    airport = airport.lower().strip()

    for airport_data in AIRPORTS.values():
        if airport in airport_data["aliases"]:
            return airport_data
    return None


def get_city(city):
    city = city.lower().strip()

    for city_data in CITIES.values():
        if city in city_data["aliases"]:
            return city_data
    return None


def get_raw(input_lat, input_lon, radius_nm=DEFAULT_RADIUS_NM):
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
        "lat": lat,
        "lon": lon,
        "radius_nm": radius,
    }
