import numpy as np

G = 6.674083131313131313 * 10**(-11)

mEarth = 5.972 * 10 ** 24 #kg
mSun = 1.989 * 10 ** 30 #kg
distance = 151.87 * 10 ** 9 #m

distance_earth_barycenter = distance * mSun / (mEarth + mSun)
distance_sun_barycenter = distance * mEarth / (mEarth + mSun)

x0_earth = -distance_earth_barycenter
x0_sun = distance_sun_barycenter

s = 1 + mEarth / mSun

def position_e(x,t):
    return (x / t)

def position_s(y,t):
    return (y / t)

def velocity_e(x,y):
    return (-1 * G * mSun) * (x * s) / (np.sqrt(x ** 2 * s ** 2 + y ** 2 * s ** 2)) ** 3

def velocity_s(x,y):
    return (-1 * G * mSun) * (y * s) / (np.sqrt(x ** 2 * s ** 2 + y ** 2 * s ** 2)) ** 3

print("The mass of the Earth is %fkg, while the mass of the sun is %fkg" % (mEarth, mSun))