import pyorb
import kepler
from astropy.constants import G, M_earth, R_earth
import numpy as np
import math

r_test = [R_earth.value + 600.0e+3, 0, 50]
v_test = [0, 6.5e+3, 0]

M0 = 5.972167867791379e+24

orb = pyorb.Orbit(M0 = M0)

orb.update(a=5536635.97804355,e=0.26035015266525435,i=7.165289637941395e-06,omega=-1.5707963267948966,Omega=-1.5707963267948966,anom=3.141592653589793)
print(orb)
anom=3.141592653589793
print()
orb.update(x=orb.x,y=orb.y,z=orb.z,vx=orb.vx,vy=orb.vy,vz=orb.vz)
print(orb)
eccentric_anomaly, cos, sin = kepler.kepler(orb.anom, orb.e)
print(eccentric_anomaly,cos,sin) 

def Eccanom(e,anom):
    anom=anom
    i=0
    delta=1e-6

    if (e<0.8):
        E=anom
    else:
        E=anom+math.sin(anom)
    F=E-e*math.sin(E) - anom
    while((math.fabs(F)>delta) and (i<1000)):
        E=E-F/(1.0-(e*math.cos(E)))
        F=E-e*math.sin(E)-anom
        i=i+1
    return E

print(Eccanom(0.5,27))  
