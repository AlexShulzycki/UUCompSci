import numpy as np

G = 6.674083131313131313 * 10**(-11)

mEarth = 5.972 * 10 ** 24 #kg
mSun = 1.989 * 10 ** 30 #kg
distance = 151.87 * 10 ** 9 #m

#center of mass when both masses are on the x-axis
barycenter = ( mSun * distance ) / (mEarth + mSun)
print(barycenter)

x0_sun = barycenter - distance
x0_earth = barycenter

s = 1 + mEarth / mSun

def velocity_e(x,t):
    return (x / t)

def velocity_s(y,t):
    return (y / t)

def acceleration_e(x,y):
    return (-1 * G * mSun) * (x * s) / (np.sqrt(x ** 2 * s ** 2 + y ** 2 * s ** 2)) ** 3

def acceleration_s(x,y):
    return (-1 * G * mSun) * (y * s) / (np.sqrt(x ** 2 * s ** 2 + y ** 2 * s ** 2)) ** 3

print("The mass of the Earth is %fkg, while the mass of the sun is %fkg" % (mEarth, mSun))