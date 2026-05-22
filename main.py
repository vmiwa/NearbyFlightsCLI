from locations import get_airport, get_city
from display import show_banner, show_location, show_menu


show_banner()
show_menu()

menu_select = input("Select Option: ").strip()

if menu_select == "1":
    airport_input = input("What Airport do you want to query?: ").lower().strip()
    airport = get_airport(airport_input)

    if airport is None:
        print("Airport not found.")
    else:
        show_location(airport)

elif menu_select == "2":
    city_input = input("What City do you want to query?: ").lower().strip()
    city = get_city(city_input)

    if city is None:
        print("City not found.")
    else:
        show_location(city)

elif menu_select == "3":
    coord_input_lat = input("Enter the Latitude (e.g. 40.7128 or -19.6244):")
    coord_input_lon = input("Enter the Longitude (e.g. 2.3522 or -43.9719):")

    location = get_raw(coord_input_lat, coord_input_lon)
    show_location(location)

else: 
    print("Invalid Option")
