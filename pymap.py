import pymap3d as pm
from math import *
import csv
import pandas as pd
from decimal import *

def geodetic_ecef(lat,lon,alt):
    x,y,z = pm.geodetic2ecef(lat,lon,alt)
    return x,y,z

def ecef_geodetic(x,y,z):
    lat,lon,alt = pm.ecef2geodetic(x,y,z)
    return lat,lon,alt

def enu_ecef(e,n,u,lat,lon,alt):
    x,y,z = pm.enu2ecef(e,n,u,lat,lon,alt)
    return x,y,z

def ecef_enu(x,y,z,lat,lon,alt):
    e,n,u = pm.ecef2enu(x,y,z,lat,lon,alt)
    return e,n,u

def ecef_aer(x,y,z,lat,lon,alt):
    az,el,sr = pm.ecef2aer(x,y,z,lat,lon,alt)
    return az,el,sr
#pd.options.display.max_rows = 10

df = pd.read_csv('ref_pos.csv')
len=print(len(df))
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
        if(round(alt1,5)==round(alt,5)):
            count+=1

print(count)