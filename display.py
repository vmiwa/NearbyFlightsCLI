BANNER = r"""
                                       |
                                       |
                                       |
                                     .-'-.
                                    ' ___ '
                          ---------'  .-.  '---------
          _________________________'  '-'  '_________________________
           ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                         \    /  ||/   H   \||  \    /
                          '--'   OO   O|O   OO   '--'

     _   _                 _             _____ _ _       _     _       
    | \ | | ___  __ _ _ __| |__  _   _  |  ___| (_) __ _| |__ | |_ ___ 
    |  \| |/ _ \/ _` | '__| '_ \| | | | | |_  | | |/ _` | '_ \| __/ __|
    | |\  |  __/ (_| | |  | |_) | |_| | |  _| | | | (_| | | | | |_\__ \
    |_| \_|\___|\__,_|_|  |_.__/ \__, | |_|   |_|_|\__, |_| |_|\__|___/
                                 |___/             |___/               
                
             Aircraft near Airports, Cities or Coordinates 
                                     
"""


def show_menu():
    print("""
          
-------------- Menu -----------------
          
1. Airport
2. City
3. Coordinates
4. Exit
          
-------------------------------------

          
""")
    

def show_banner():
    print(BANNER)


def show_location(location):
    print("\n=======================================================================\n")
    print(f"                   {location['name']}\n")
    print(f"Latitude: {location['lat']}")
    print(f"Longitude: {location['lon']}")
    print(f"Radius: {location['radius_nm']} nautical miles")
    print("\n=======================================================================\n")



def show_aircraft_table(aircraft_list):
    print("\nNearby Aircraft\n")
    print(f"{'Callsign':<10} {'Type':<6} {'Reg':<10} {'Alt(ft)':>8} {'Alt(m)':>8} {'Speed(km/h)':>12} {'Vert':>10} {'Dist(km)':>10} {'Seen':>10}")
    print("-" * 92)

    for aircraft in aircraft_list:
        flight = format_value(aircraft["flight"])
        aircraft_type = format_value(aircraft["type"])
        reg = format_value(aircraft["reg"])
        altitude_ft = format_value(aircraft["altitude_ft"])
        altitude_m = format_value(aircraft["altitude_m"])
        speed_kmh = format_value(aircraft["speed_kmh"])
        vertical_rate = format_vertical_rate(aircraft["vertical_rate"])
        distance_km = format_value(aircraft["distance_km"])

        if aircraft["seen"] is None:
            seen = "N/A"
        else:
            seen = f"{round(aircraft['seen'], 1)}s ago"

        print(f"{flight:<10} {aircraft_type:<6} {reg:<10} {altitude_ft:>8} {altitude_m:>8} {speed_kmh:>12} {vertical_rate:>10} {distance_km:>10} {seen:>10}")
    print()



def format_value(value):
    if value is None:
        return "N/A"

    return str(value)

def format_vertical_rate(rate):
    if rate is None:
        return "N/A"

    if rate > 0:
        return f"↑{rate}"

    if rate < 0:
        return f"↓{abs(rate)}"

    return "level"