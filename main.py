from airports import AIRPORTS

airport_key = input("What Airport do you want to query?: ").lower().strip()

if airport_key not in AIRPORTS:
    raise KeyError(f"Airport not found: {airport_key}")

airport = AIRPORTS[airport_key]

print(f"Airport Name: {airport['name']}")
print(f"Latitude: {airport['lat']}")
print(f"Longitude: {airport['lon']}")
print(f"Radius: {airport['radius_nm']}")
