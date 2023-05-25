from PIL import Image
from PIL import ExifTags
import csv
import os

metadata = []

images = [file for file in os.listdir() if file[-4:] == '.JPG']

for image_name in images:
    row = [image_name]    
    with Image.open(image_name) as image:
        exif = image.getexif()
        row.append(exif[306]) # date created
        raw_coordinates = exif.get_ifd(ExifTags.IFD.GPSInfo)
        if len(raw_coordinates) > 0:
            row.append(f"{raw_coordinates[2][0]}º {int(raw_coordinates[2][1])}' {(raw_coordinates[2][1] - int(raw_coordinates[2][1])) * 60} '' N") # latitude
            row.append(f"{raw_coordinates[4][0]}º {int(raw_coordinates[4][1])}' {(raw_coordinates[4][1] - int(raw_coordinates[4][1])) * 60} '' W") # longitude
        else:
            row.append("N/A")
            row.append("N/A")
    metadata.append(row)

with open('coordinates.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['Filename', 'Date', 'Latitude', 'Longitude'])
    write.writerows(metadata)