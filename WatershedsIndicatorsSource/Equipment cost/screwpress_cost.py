from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
#from matplotlib.mlab import griddata
import numpy as np
import scipy.interpolate
from scipy.optimize import curve_fit
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import csv
import pandas as pd
import seaborn as sns

inch_to_m = 0.0254


#Matche.com http://matche.com/equipcost/Separator.html (screw classifier, 1 screw)
diameter_inch = np.arange(2, 84, 4)
diameter_m = diameter_inch*inch_to_m

cost_2014_USD = np.array([400, 2200, 4900, 8500, 12800, 17700, 23200, 29200, 35800, 42900, 50400, 58400, 66800, 75600, 84900, 94600, 104600, 115100, 125900, 137100, 148600])

#Fit

#def screwpress_cost(xdata, a):
#    return (a**xdata) #Negative exp function

#def screwpress_cost(xdata, a, b, c, d):
#    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly

def screwpress_cost(xdata, a, b, c):
    return a*xdata*xdata+b*xdata+c #Second order poly

#def screwpress_cost(xdata, a, b, c, d, e):
#    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly

#def screwpress_cost(xdata, a, b, c):
#    return a/(1+((xdata)*b)**(c)) #Sigmoidal function

#def screwpress_cost(xdata, a, b):
#    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)

# Meters
plt.figure()
parameters_screwpress_cost_m, cov_screwpress_cost_m = curve_fit(screwpress_cost, diameter_m, cost_2014_USD)
#
#with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
#    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
plt.plot(diameter_m, cost_2014_USD)
plt.plot(diameter_m, screwpress_cost(diameter_m, *parameters_screwpress_cost_m), 'k--', label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_screwpress_cost_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
plt.legend(loc='upper left')
plt.title('Screw press (SI)')
plt.xlabel("Screw press diameter $ (m) $")
plt.ylabel('Cost 2014 USD')
plt.savefig("screwpress_cost_m.pdf",bbox_inches='tight')


#Inches
plt.figure()
parameters_screwpress_cost_inch, cov_screwpress_cost__inch = curve_fit(screwpress_cost, diameter_inch, cost_2014_USD)
#
#with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
#    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
plt.plot(diameter_inch, cost_2014_USD)
plt.plot(diameter_inch, screwpress_cost(diameter_inch, *parameters_screwpress_cost_inch), 'k--', label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_screwpress_cost_inch)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
plt.legend(loc='upper left')
plt.title('Screw press (British Imperial)')
plt.xlabel("Screw press diameter $ (inch) $")
plt.ylabel('Cost 2014 USD')
plt.savefig("screwpress_cost_inch.pdf",bbox_inches='tight')
    
