from locations import get_airport, get_city, get_raw
from display import (
    fetch_status,
    show_aircraft_table,
    show_banner,
    show_coordinate_help,
    show_error,
    show_goodbye,
    show_location,
    show_menu,
    show_warning,
)
from adsb_client import get_nearby_aircraft

def main():
    show_banner()

    while True:
        show_menu()

        menu_select = input("\nSelect Option: ").strip()

        if menu_select == "1":
            airport_input = input("\nWhat Airport do you want to query?: ").lower().strip()
            location = get_airport(airport_input)

        elif menu_select == "2":
            city_input = input("\nWhat City do you want to query?: ").lower().strip()
            location = get_city(city_input)

        elif menu_select == "3":
            show_coordinate_help()
            coord_input_lat = input("\nLatitude  (decimal degrees, e.g. -23.4356): ").strip()
            coord_input_lon = input("Longitude (decimal degrees, e.g. -46.4731): ").strip()
            location = get_raw(coord_input_lat, coord_input_lon)

        elif menu_select == "4":
            show_goodbye()
            break

        else:
            show_error("Invalid option. Please choose 1, 2, 3, or 4.")
            continue

        if location is None:
            if menu_select == "3":
                show_error(
                    "Invalid coordinates. Use decimal degrees like -23.4356 and -46.4731."
                )
            else:
                show_error("Location not found.")
        else:
            show_location(location)
            with fetch_status(location):
                aircraft_list = get_nearby_aircraft(location)

            if aircraft_list is None:
                show_error("Could not reach ADS-B API.")
            elif len(aircraft_list) == 0:
                show_warning("No aircraft found nearby.")
            else:
                show_aircraft_table(aircraft_list)



if __name__ == "__main__":
    main()
