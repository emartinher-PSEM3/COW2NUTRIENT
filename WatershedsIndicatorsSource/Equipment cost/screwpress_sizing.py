from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import numpy as np
import scipy.interpolate
from scipy.optimize import curve_fit
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import csv
import pandas as pd
import seaborn as sns


#SIZES FOR SCREW PRESS FOR SLUDGE DEWATERING (PWTech)
inch_to_m = 0.0254
GPM_to_cuft_hr = 0.1336801*60
cuft_to_m3 = 0.02831685
HP_to_kW = 0.7456999

#PWTech http://pwtech.us/HTML/addResources.html
diameter_inch = np.array([9.1, 13.8, 16.5, 23])
diameter_m = diameter_inch*inch_to_m

flow_GPM = np.array([8, 15, 35, 65])
flow_cuft_hr = flow_GPM*GPM_to_cuft_hr
flow_m3_day = flow_cuft_hr*cuft_to_m3*24

power_HP = np.array([0.4, 0.6, 1.2, 2.6])
power_kW = power_HP*HP_to_kW

#Fit
#def screwpress_size(xdata, a):
#    return (a**xdata) #Negative exp function

def screwpress_size(xdata, a, b, c, d):
    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly

#def screwpress_size(xdata, a, b, c):
#    return a*xdata*xdata+b*xdata+c #Second order poly
    
#def screwpress_size(xdata, a, b):
#    return a*xdata+b #Fist order poly

#def screwpress_size(xdata, a, b, c, d, e):
#    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly

#def screwpress_size(xdata, a, b, c):
#    return a/(1+((xdata)*b)**(c)) #Sigmoidal function

#def screwpress_cost(xdata, a, b):
#    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)

# Meters
plt.figure()
parameters_screwpress_size_m, cov_screwpress_size_m = curve_fit(screwpress_size, flow_m3_day, diameter_m)
#
#with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
#    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
plt.plot(flow_m3_day, diameter_m)
plt.plot(flow_m3_day, screwpress_size(flow_m3_day, *parameters_screwpress_size_m), 'k--', label='Fit: a=%5.3e, b=%5.3e, \n      c=%5.3e,  d=%5.3e' % tuple(parameters_screwpress_size_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
plt.legend(loc='upper left')
plt.title('Screw press size (SI)')
plt.xlabel("Flow $ (m^{3} / day) $")
plt.ylabel("Screw press diameter $ (m) $")
plt.savefig("screwpress_size_m.pdf")


#Inches
plt.figure()
parameters_screwpress_size_inch, cov_screwpress_size_inch = curve_fit(screwpress_size, flow_m3_day, diameter_inch)
#
#with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
#    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
plt.plot(flow_m3_day, diameter_inch)
plt.plot(flow_m3_day, screwpress_size(flow_m3_day, *parameters_screwpress_size_inch), 'k--', label='Fit: a=%5.3e, b=%5.3e, \n      c=%5.3e,  d=%5.3e' % tuple(parameters_screwpress_size_inch)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
plt.legend(loc='upper left')
plt.title('Screw press size (British Empire)')
plt.xlabel("Flow $ (m^{3} / day) $")
plt.ylabel("Screw press diameter $ (inch) $")
plt.savefig("screwpress_size_inch.pdf")


#Power

#Fit
#def screwpress_power(xdata, a):
#    return (a**xdata) #Negative exp function

#def screwpress_power(xdata, a, b, c, d):
#    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly

def screwpress_power(xdata, a, b, c):
    return a*xdata*xdata+b*xdata+c #Second order poly
    
#def screwpress_power(xdata, a, b):
#    return a*xdata+b #Fist order poly

#def screwpress_power(xdata, a, b, c, d, e):
#    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly

#def screwpress_power(xdata, a, b, c):
#    return a/(1+((xdata)*b)**(c)) #Sigmoidal function

#def screwpress_power(xdata, a, b):
#    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
    
plt.figure()
parameters_screwpress_power, cov_screwpress_power = curve_fit(screwpress_power, flow_m3_day, power_kW)
#
#with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
#    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
plt.plot(flow_m3_day, power_kW)
plt.plot(flow_m3_day, screwpress_power(flow_m3_day, *parameters_screwpress_power), 'k--', label='Fit: a=%5.3e, b=%5.3e, c=%5.3e' % tuple(parameters_screwpress_power)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
plt.legend(loc='upper left')
plt.title('Screw press power (SI)')
plt.xlabel("Flow $ (m^{3} / day) $")
plt.ylabel("Screw press power $ (kW) $")
plt.savefig("screwpress_power_kW.pdf")
