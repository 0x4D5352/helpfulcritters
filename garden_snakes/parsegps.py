"""
Converting some JSON files with misc info + Time/Lat/Long into CSVs!
Lotta hard coded stuff atm, but that's a problem for future me.
TODO: let it take cli args, u need to learn how to do that eventually
Example CLI Args:
    -- pass in header
    -- pass in directory (or single file!)
TODO: remove hardcoded field extraction and number of header fields!!!
<3
"""

import json
import csv
import os

def extract_json_fields_to_csv(json_file, csv_name):
    with open(json_file) as file_being_processed:
        imported_json = json.load(file_being_processed)
        header = ['Timestamp', "Latitude", "Longitude"]
        with open(csv_name, 'w') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=header)
            writer.writeheader()
            seen_time = []
            for entry in imported_json:
                time = entry[header[0]]
                if time not in seen_time:
                    writer.writerow({header[0]: time, header[1]: entry[header[1]], header[2]: entry[header[2]]})
                    seen_time.append(time)

json_names = [file for file in os.listdir() if file[-4:] == 'json']
csv_names = ['{0}csv'.format(file[0:-4]) for file in json_names]


if __name__ == '__main__':
    for index, name in enumerate(json_names):
        extract_json_fields_to_csv(name, csv_names[index])