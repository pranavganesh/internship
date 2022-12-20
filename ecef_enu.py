import pymap3d as pm
from math import *
import csv
import pandas as pd
from decimal import *

df = pd.read_csv('ecef_data.csv')

lat0,lon0,alt0 = 11.0,73.0,0.0
count=0
header = ['e','n','u']

with open('enu_data.csv','w',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for ind in df.index:
        x,y,z = df['x'][ind],df['y'][ind],df['z'][ind]

        e,n,u = pm.ecef2enu(x,y,z,lat0,lon0,alt0)
        writer.writerow([e,n,u])

        x1,y1,z1 = pm.enu2ecef(e,n,u,lat0,lon0,alt0)

        if ((round(x1,5)==round(x,5)) and (round(y1,5)==round(y,5)) and (round(z1,5)==round(z,5))):
            count+=1

if (count==len(df)):
    print('Data verified')