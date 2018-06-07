# coding: utf-8

import sys
import csv
import pymap3d as pm

obs_geo = {
    'lat': 35.616695643435804,
    'lon': 139.8975994159839,
    'alt': 3.4972135106328324
    }

offset_alt = 1.5

read_name = 'state.txt'
write_name = 'dst_state.csv'

rf = open(read_name, 'r')
reader = csv.reader(rf)

header = next(reader)
header.append('az')
header.append('el')
header.append('dst')

data = [header]
for row in reader:
    lat = float(row[7])
    lon = float(row[8])
    alt = float(row[9]) + offset_alt

    az, el, dst = pm.geodetic2aer(lat, lon, alt, obs_geo['lat'], obs_geo['lon'], obs_geo['alt'])
    row.append(az)
    row.append(el)
    row.append(dst)

    data.append(row)

rf.close()

wf = open(write_name, 'w')
writer = csv.writer(wf)
writer.writerows(data)
wf.close()