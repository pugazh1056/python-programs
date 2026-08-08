def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    
    return (coordinate[0],coordinate[1])


def compare_records(azara_record, rui_record):
    azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    rui_coordinate = convert_coordinate(rui_record[1])  # Convert Rui coord too!
    return azara_coordinate == rui_coordinate


def create_record(treasure, location):
    treasure_name, treasure_coordinate = treasure
    location_name, location_coordinate, color = location

    # convert location coordinate tuple back to string
    loc_coord_string = location_coordinate[0] + location_coordinate[1]

    if treasure_coordinate == loc_coord_string:
        return (treasure_name,
                treasure_coordinate,
                location_name,
                location_coordinate,
                color)
    else:
        return "not a match"


def clean_up(records):
    result = ""

    for record in records:
        treasure_name = record[0]
        location_name = record[2]
        location_coordinate = record[3]
        color = record[4]

        new_tuple = (treasure_name, location_name, location_coordinate, color)

        result += str(new_tuple) + "\n"

    return result
