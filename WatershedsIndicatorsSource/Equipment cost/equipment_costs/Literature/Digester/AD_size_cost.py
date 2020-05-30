# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:33:53 2019

@author: Edgar
"""

import numpy as np
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import curve_fit
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.interpolate import make_interp_spline, BSpline
from matplotlib import style
#style.use('bmh')
import matplotlib.font_manager
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)



AD_size_cost_array = pd.read_csv('AD_size_cost.csv', sep=",", header=0)
AD_size_OMcost_array = pd.read_csv('OM_Unit_cost_ratio.csv', sep=",", header=0)


#Regression fits

#def fit(xdata, a):
#    return (a**xdata) #Negative exp function

#def fit(xdata, a,b):
#    return (a*xdata**b) # exp function

#def fit(xdata, a,b):
#    return (a*np.log(xdata)+b) # log function

#def fit(xdata, a, b, c, d):
#    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly

#def fit(xdata, a, b, c):
#    return a*xdata*xdata+b*xdata+c #Second order poly

def fit(xdata, a, b):
    return a*xdata+b #First order poly

#def fit(xdata, a, b, c, d, e):
#    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly

#def fit(xdata, a, b, c):
#    return a/(1+((xdata)*b)**(c)) #Sigmoidal function

#def fit(xdata, a, b):
#    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
    
#AD_size_cost
parameters_AD_cost, cov__AD_cost = curve_fit(fit, AD_size_cost_array['Animal population'], AD_size_cost_array['Cost'])
#parameters_food = [0.4004, -0.187]
x_smooth = np.linspace(AD_size_cost_array['Animal population'].min(), AD_size_cost_array['Animal population'].max(),100)

plt.figure(0, figsize=(8,6))
plt.scatter(AD_size_cost_array['Animal population'], AD_size_cost_array['Cost'], color='red',label=None)
#plt.scatter(AD_size_OMcost_array['Animal population'], AD_size_OMcost_array['Cost'], color='blue',label=None)
plt.plot(x_smooth, fit(x_smooth, *parameters_AD_cost), 'k--',)# label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_AD_cost)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('AD cost vs. animal population', fontsize=12, fontweight="bold")
plt.xlabel("Animal population")
plt.ylabel('Installing cost (2003 USD)')
plt.grid(True)
plt.savefig("AD_size_cost.pdf", bbox_inches='tight')

#plt.figure(1)
#plt.plot(np.linspace(AD_size_cost_array['Animal population'].min(), 20E3,100), fit(np.linspace(AD_size_cost_array['Animal population'].min(), 20E3,100), *parameters_AD_cost), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_AD_cost))


# =============================================================================
# OM costs
# =============================================================================
#Regression fits

#def fit(xdata, a):
#    return (a**xdata) #Negative exp function

#def fit(xdata, a,b):
#    return (a*xdata**b) # exp function

#def fit(xdata, a,b):
#    return (a*np.log(xdata)+b) # log function

#def fit(xdata, a, b, c, d):
#    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly

#def fit(xdata, a, b, c):
#    return a*xdata*xdata+b*xdata+c #Second order poly

#def fit(xdata, a, b):
#    return a*xdata+b #First order poly

#def fit(xdata, a, b, c, d, e):
#    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly

def fit(xdata, a, b, c):
    return a/(1+((xdata)*b)**(c)) #Sigmoidal function

#def fit(xdata, a, b):
#    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
    
##AD_size_cost
#parameters_AD_OMcost, cov__AD_OMcost = curve_fit(fit, AD_size_OMcost_array['Animal population'], AD_size_OMcost_array['OM Cost'])
##parameters_food = [0.4004, -0.187]
#x_smooth = np.linspace(AD_size_OMcost_array['Animal population'].min(), AD_size_OMcost_array['Animal population'].max(),100)
#
#plt.figure(2)
#plt.scatter(AD_size_OMcost_array['Animal population'], AD_size_OMcost_array['OM Cost'], color='red',label=None)
#plt.plot(x_smooth, fit(x_smooth, *parameters_AD_OMcost), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_AD_cost)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('AD O&M cost vs. animal population', fontsize=12, fontweight="bold")
#plt.xlabel("Animal population")
#plt.ylabel('O&M cost (USD)')
#plt.grid(True)
#plt.savefig("AD_size_OMcost.pdf", bbox_inches='tight')
#
##plt.figure(1)
##plt.plot(np.linspace(AD_size_cost_array['Animal population'].min(), 20E3,100), fit(np.linspace(AD_size_cost_array['Animal population'].min(), 20E3,100), *parameters_AD_cost), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_AD_cost))

parameters_AD_OMcost, cov__AD_OMcost = curve_fit(fit, AD_size_OMcost_array['Animal population'], AD_size_OMcost_array['OM:Unit'],maxfev = 2000)
#parameters_food = [0.4004, -0.187]
x_smooth = np.linspace(AD_size_OMcost_array['Animal population'].min(), AD_size_OMcost_array['Animal population'].max(),100)

plt.figure(3, figsize=(8,6))
plt.scatter(AD_size_OMcost_array['Animal population'], AD_size_OMcost_array['OM:Unit'], color='red',label=None)
plt.plot(x_smooth, fit(x_smooth, *parameters_AD_OMcost), 'k--',)# label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_AD_OMcost)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper right')
#plt.title('O&M:Unit cost ratio vs. animal population', fontsize=12, fontweight="bold")
plt.xlabel("Animal population")
plt.ylabel('O&M cost / Digester cost rplt.figsize(8,6)atio')
plt.grid(True)
plt.savefig("AD_size_OM_Unit_cost.pdf", bbox_inches='tight')

#plt.figure(4)
#plt.plot(np.linspace(AD_size_OMcost_array['Animal population'].min(), 20E3,100), fit(np.linspace(AD_size_OMcost_array['Animal population'].min(), 20E3,100), *parameters_AD_OMcost), 'k--', label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_AD_OMcost))


plt.show()
