# NearbyFlightsCLI

![NearbyFlightsCLI demo](assets/demo.gif)

NearbyFlightsCLI is a Python terminal application that lets users choose a pre-registered city, airport, or custom coordinates and display nearby live aircraft in the terminal.

The application queries aircraft within a default radius of 100 nautical miles from the selected location and displays the results in a formatted table. The table includes information such as flight/callsign, aircraft type, registration, altitude, speed, vertical rate, distance, and last-seen time.

## Data Source

NearbyFlightsCLI uses live ADS-B data from the public ADSB.lol API.

[ADS-B](https://en.wikipedia.org/wiki/Automatic_Dependent_Surveillance%E2%80%93Broadcast), or Automatic Dependent Surveillance–Broadcast, is a system where aircraft broadcast telemetry such as position, altitude, speed, and identification data. ADSB.lol collects this data through a global network of volunteer feeders.

To learn more about ADSB.lol project or contribute as a feeder, see the [ADSB.lol website](https://www.adsb.lol/).

## Installation

```bash
$ git clone https://github.com/vmiwa/NearbyFlightsCLI.git
$ cd NearbyFlightsCLI
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

Make sure the python virtual environment is active for the project:

```bash
$ source .venv/bin/activate
```

Run the application:

```bash
$ python3 main.py
```

Then choose one of the available search modes:

```text
[1] Airport
[2] City
[3] Coordinates
[4] Exit
```

Airport search accepts airport codes or common airport names, such as `GRU`, `JFK`, `DXB`, `guarulhos`, or `o'hare`.

City search accepts city names and common aliases, such as `São Paulo`, `New York`, `NYC`, `Tokyo`, or `Bogotá`.

Coordinate search uses decimal degrees with a dot:

```text
Latitude:  -23.4356
Longitude: -46.4731
```

South and West coordinates should be negative.

## Project Structure

```text
main.py         - Program flow and menu handling
locations.py    - Airport, city, and coordinate lookup
adsb_client.py  - API request, response handling, and aircraft data normalization
display.py      - Terminal output and table formatting
requirements.txt - Python dependencies
```
