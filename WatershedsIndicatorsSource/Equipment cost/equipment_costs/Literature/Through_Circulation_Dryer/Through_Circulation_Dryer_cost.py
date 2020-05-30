import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


inch_to_m = 0.0254


#Perry Table 12-23
wide = 2.4
lenght = np.array([7.5, 15, 22.5, 30])
area = lenght*wide

cost_m2_1996 = np.array([8600, 6700, 6200, 5900])
cost_m2_1996 = cost_m2_1996*area

##def dryer_cost(xdata, a):
##    return (a**xdata) #Negative exp function
#
##def dryer_cost(xdata, a, b, c, d):
##    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly
#
#def dryer_cost(xdata, a, b, c):
#    return a*xdata*xdata+b*xdata+c #Second order poly

def dryer_cost(xdata, a, b):
    return a*xdata+b #First order poly

#
##def dryer_cost(xdata, a, b, c, d, e):
##    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly
#
##def dryer_cost(xdata, a, b, c):
##    return a/(1+((xdata)*b)**(c)) #Sigmoidal function
#
##def dryer_cost(xdata, a, b):
##    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
#
# Meters
plt.figure()
parameters_dryer_cost_m, cov_dryer_cost_m = curve_fit(dryer_cost, area, cost_m2_1996)
#
plt.plot(area, cost_m2_1996)
plt.plot(area, dryer_cost(area, *parameters_dryer_cost_m), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_dryer_cost_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
plt.legend(loc='upper left')
plt.title('Through Circulation Dryer (SI)')
plt.xlabel("Dryer area $ (m^{2}) $")
plt.ylabel('Cost 1996 USD')
plt.savefig("Through_Circulation_Dryer_cost.pdf")


    
