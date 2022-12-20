import pymap3d as pm
from math import *
import csv
import pandas as pd
from decimal import *

df = pd.read_csv('ref_pos.csv')

len=len(df)
count=0

header=['x','y','z']

with open('ecef_data.csv','w',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for ind in df.index:
        lat,lon,alt = df['ref_pos_lat (deg)'][ind],df['ref_pos_lon (deg)'][ind],df['ref_pos_alt (m)'][ind]
        x,y,z = pm.geodetic2ecef(lat,lon,alt)

        writer.writerow([x,y,z])

        lat1,lon1,alt1 = pm.ecef2geodetic(x,y,z)

        if((round(lat1,5)==round(lat,5)) and (round(lon1,5)==round(lon,5)) and (round(alt1,5)==round(alt,5))):
            count+=1


if (count==len):
    print('Data verified')