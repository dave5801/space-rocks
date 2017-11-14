"""
Bunch of nonsense that makes a GET request through each NASA NEO API page.

It will then break down their painful nested dict/list/dict mess and pull
out only the information we need and place it into a single dict with
only one level.
"""
import requests
SPACE_DATA = []

for x in range(201):
    r = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?page=' + str(x) + '&size=20&api_key=LOTf1b1LrXn7WMAMYM4UtgEbaiZwNjxFStMKr5L4')
    data = r.json()
    data = data['near_earth_objects']
    try:
        for i in range(len(data)):
            data_id = data[i]['neo_reference_id']
            data_name = data[i]['name']
            data_abs_mag = data[i]["absolute_magnitude_h"]
            data_diameter_miles = data[i]["estimated_diameter"]["miles"]
            diameter_miles_average = (data_diameter_miles['estimated_diameter_max'] + data_diameter_miles['estimated_diameter_min']) / 2
            data_diameter_feet = data[i]["estimated_diameter"]["feet"]
            diameter_feet_average = (data_diameter_feet['estimated_diameter_max'] + data_diameter_feet['estimated_diameter_min']) / 2
            data_diameter_kilometers = data[i]["estimated_diameter"]["kilometers"]
            diameter_kilometers_average = (data_diameter_kilometers['estimated_diameter_max'] + data_diameter_kilometers['estimated_diameter_min']) / 2
            data_diameter_meters = data[i]["estimated_diameter"]["meters"]
            diameter_meters_average = (data_diameter_meters['estimated_diameter_max'] + data_diameter_meters['estimated_diameter_min']) / 2
            data_hazard = data[i]["is_potentially_hazardous_asteroid"]
            go_through = data[i]['close_approach_data']
            for key in go_through:
                data_miss_astronomical = key['miss_distance']['astronomical']
                data_miss_lunar = key['miss_distance']['lunar']
                data_miss_kilometers = key['miss_distance']['kilometers']
                data_miss_miles = key['miss_distance']['miles']
                data_velocity_kps = key['relative_velocity']['kilometers_per_second']
                data_velocity_kph = key['relative_velocity']['kilometers_per_hour']
                data_velocity_mph = key['relative_velocity']['miles_per_hour']
                data_orbiting_body = key['orbiting_body']
            data_orbit_period = data[i]['orbital_data']['orbital_period']
            data_perihelion_dist = data[i]['orbital_data']['perihelion_distance']
            data_aphelion_dist = data[i]['orbital_data']['aphelion_distance']
            data_orbit_eccentricity = data[i]['orbital_data']['eccentricity']
            data_perihelion_time = data[i]['orbital_data']['perihelion_time']

            one_asteroid = {
                'id': data_id,
                'name': data_name,
                'absmag': data_abs_mag,
                'diamiles': diameter_miles_average,
                'diafeet': diameter_feet_average,
                'diakm': diameter_kilometers_average,
                'diam': diameter_meters_average,
                'hazard': data_hazard,
                'miss_astronomical': data_miss_astronomical,
                'miss_lunar': data_miss_lunar,
                'miss_km': data_miss_kilometers,
                'miss_miles': data_miss_miles,
                'velocity_kps': data_velocity_kps,
                'velocity_kph': data_velocity_kph,
                'velocity_mph': data_velocity_mph,
                'orbit_period': data_orbit_period,
                'perihelion_dist': data_perihelion_dist,
                'aphelion_dist': data_aphelion_dist,
                'orbit_eccentricity': data_orbit_eccentricity,
                'perihelion_time': data_perihelion_time
            }
            SPACE_DATA.append(one_asteroid)
    except KeyError:
        continue
    print("Page: " + str(x))
