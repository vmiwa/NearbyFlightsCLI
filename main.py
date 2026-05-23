from locations import get_airport, get_city, get_raw
from display import show_banner, show_location, show_menu, show_aircraft_table
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
            coord_input_lat = input("\nEnter the Latitude: ")
            coord_input_lon = input("\nEnter the Longitude: ")
            location = get_raw(coord_input_lat, coord_input_lon)

        elif menu_select == "4":
            print("\nExiting.")
            break

        else:
            print("\n[ERROR] Invalid option. Please choose 1, 2, 3, or 4.")
            continue

        if location is None:
            print("\n[ERROR] Location not found.")
        else:
            show_location(location)
            aircraft_list = get_nearby_aircraft(location)

            if aircraft_list is None:
                print("\n[ERROR] Could not reach ADS-B API.")
            elif len(aircraft_list) == 0:
                print("\nNo aircraft found nearby.")
            else:
                show_aircraft_table(aircraft_list)



if __name__ == "__main__":
    main()
