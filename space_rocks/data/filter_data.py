import json

SUPER_DICT = {}


with open('data.json', 'r') as f:
    data = json.load(f)
    data = data['near_earth_objects']


def filter_all_data(data):
    name = data['name']
    new_approach = data['close_approach_data'][0]
    new_orbital = data['orbital_data']
    new_diameter = data['estimated_diameter']
    new_general = {}
    general = ['neo_reference_id',
               'absolute_magnitude_h',
               'is_potentially_hazardous_asteroid']
    for key in data:
        if key in general:
            new_general[key] = data[key]
    data = [new_approach, new_orbital, new_diameter, new_general]
    for item in data:
        item['name'] = name
    return data


def filter_approach_data(data):
    data_in = data[0]
    data_out = {}
    required = ['miss_distance', 'relative_velocity', 'name']
    if data_in['orbiting_body'] != 'earth':
        print('nope')
    for item in data_in:
        if data_in[item] == ' ':
            del data[item]
        if item in required:
            data_out[item] = data_in[item]
    return data_out


def filter_orbital_data(data):
    data_in = data[1]
    data_out = {}
    required = ['aphelion_distance', 'jupiter_tisserand_invariant', 'orbit_id', 'name']
    for item in data_in:
        if data_in[item] == '':
            del data[item]
        if item in required:
            data_out[item] = data_in[item]
    return data_out


def filter_diameter_data(data):
    data_in = data[2]
    for item in data_in:
        if data_in[item] == '':
            del data[item]
    return data_in


def create_super_dict(data):
    returned = filter_all_data(data)
    general = returned[3]
    orbital = filter_orbital_data(returned)
    diameter = filter_diameter_data(returned)
    approach = filter_approach_data(returned)
    name = orbital['name']
    SUPER_DICT[name] = []
    SUPER_DICT[name].append(general)
    SUPER_DICT[name].append(orbital)
    SUPER_DICT[name].append(diameter)
    SUPER_DICT[name].append(approach)
    return SUPER_DICT[name]


# returned = filter_all_data(data[0])
# filter_orbital_data(returned)
# filter_diameter_data(returned)
