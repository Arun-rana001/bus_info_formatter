import json

def bus_info_formatter(input_string):
    # Split multiple entries separated by semicolon
    entries = input_string.split(";")
    bus_list = []

    for entry in entries:
        parts = [p.strip() for p in entry.split(",")]
        if len(parts) == 5:
            bus_dict = {
                "BusNo": int(parts[0]),
                "Source": parts[1],
                "Destination": parts[2],
                "Time": parts[3],
                "Fare": int(parts[4])
            }
            bus_list.append(bus_dict)

    # If only one entry, return object instead of list
    if len(bus_list) == 1:
        return json.dumps(bus_list[0], indent=4)
    else:
        return json.dumps(bus_list, indent=4)


# Example usage
input_data = "202, Rohtak, Delhi, 8:45 AM, 50; 305, Chandigarh, Jaipur, 9:30 PM, 120"
print(bus_info_formatter(input_data))
