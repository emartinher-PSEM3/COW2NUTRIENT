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

inch_to_m = 0.0254
inch_to_m = 0.0254
GPM_to_cuft_hr = 0.1336801*60
cuft_to_m3 = 0.02831685
HP_to_kW = 0.7456
sqft_to_m2 = 0.09290304

#EPA Estimating Water Treatment Costs 1979 Package Gravity and Pressure Filter Plants
filter_package_intervalsflow_gpm = np.array([0.7, 1.7, 7, 17, 28, 80, 170, 287.5, 420, 630, 1400])
filter_package_flow_m3_hr = filter_package_intervalsflow_gpm*GPM_to_cuft_hr*cuft_to_m3

filter_type = ['Pressure', 'Gravity']

filter_package_investment_cost_1979_USD = np.array([19020, 30250, 41480, 52610, 63740, 151320, 189850, 214280, 254750, 463450])

filter_package_investment_cost_1979_USD_store=[]
filter_type_store = []
n_filters = []
flow_vector = np.arange(0.16, 318, 0.1)
for flow in flow_vector:
    if filter_package_flow_m3_hr[0] <= flow < filter_package_flow_m3_hr[1]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[0])
        
    elif filter_package_flow_m3_hr[1] <= flow < filter_package_flow_m3_hr[2]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[1])
        
    elif filter_package_flow_m3_hr[2] <= flow < filter_package_flow_m3_hr[3]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[2])
        
    elif filter_package_flow_m3_hr[3] <= flow < filter_package_flow_m3_hr[4]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[3])
        
    elif filter_package_flow_m3_hr[4] <= flow < filter_package_flow_m3_hr[5]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[4])
        
    elif filter_package_flow_m3_hr[5] <= flow < filter_package_flow_m3_hr[6]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[5])
        
    elif filter_package_flow_m3_hr[6] <= flow < filter_package_flow_m3_hr[7]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[6])
        
    elif filter_package_flow_m3_hr[7] <= flow < filter_package_flow_m3_hr[8]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[7])
        
    elif filter_package_flow_m3_hr[8] <= flow < filter_package_flow_m3_hr[9]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[8])
        
    elif filter_package_flow_m3_hr[9] <= flow <= filter_package_flow_m3_hr[10]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_investment_cost_1979_USD_store.append(filter_package_investment_cost_1979_USD[9])
        
pressure_filter_flow = [i for i in flow_vector if i<=19]
gravity_filter_flow = [i for i in flow_vector if i>19]

plt.figure()
plt.plot(pressure_filter_flow, filter_package_investment_cost_1979_USD_store[:len(pressure_filter_flow)])
plt.plot(gravity_filter_flow,filter_package_investment_cost_1979_USD_store[len(pressure_filter_flow):])
#plt.legend(loc='upper left')
plt.title('Filter (package, gravity) investment cost (SI) \n (all costs included except filtration media)')
plt.xlabel("Filter flow $ (m^{3}/h) $")
plt.ylabel('Cost (1979 USD)')
plt.savefig("filter_pressure_gravity_investment_cost_m.pdf", bbox_inches='tight')


#EPA Estimating Water Treatment Costs 1979 Package Gravity and Pressure Filter Plants
filter_package_operation_cost_1979_USD = np.array([4440, 4600, 4760, 5400, 6040, 35090, 36375, 43990, 44345, 58680])

filter_package_operation_cost_1979_USD_store=[]
filter_type_store = []
n_filters = []
flow_vector = np.arange(0.16, 318, 0.1)
for flow in flow_vector:
    if filter_package_flow_m3_hr[0] <= flow < filter_package_flow_m3_hr[1]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[0])
        
    elif filter_package_flow_m3_hr[1] <= flow < filter_package_flow_m3_hr[2]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[1])
        
    elif filter_package_flow_m3_hr[2] <= flow < filter_package_flow_m3_hr[3]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[2])
        
    elif filter_package_flow_m3_hr[3] <= flow < filter_package_flow_m3_hr[4]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[3])
        
    elif filter_package_flow_m3_hr[4] <= flow < filter_package_flow_m3_hr[5]:
        filter_type_store = filter_type[0]
        n_filters = 1
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[4])
        
    elif filter_package_flow_m3_hr[5] <= flow < filter_package_flow_m3_hr[6]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[5])
        
    elif filter_package_flow_m3_hr[6] <= flow < filter_package_flow_m3_hr[7]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[6])
        
    elif filter_package_flow_m3_hr[7] <= flow < filter_package_flow_m3_hr[8]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[7])
        
    elif filter_package_flow_m3_hr[8] <= flow < filter_package_flow_m3_hr[9]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[8])
        
    elif filter_package_flow_m3_hr[9] <= flow <= filter_package_flow_m3_hr[10]:
        filter_type_store = filter_type[1]
        n_filters = 2
        filter_package_operation_cost_1979_USD_store.append(filter_package_operation_cost_1979_USD[9])
        
pressure_filter_flow = [i for i in flow_vector if i<=19]
gravity_filter_flow = [i for i in flow_vector if i>19]

plt.figure()
plt.plot(pressure_filter_flow, filter_package_operation_cost_1979_USD_store[:len(pressure_filter_flow)])
plt.plot(gravity_filter_flow,filter_package_operation_cost_1979_USD_store[len(pressure_filter_flow):])
#plt.legend(loc='upper left')
plt.title('Filter (package, gravity) operation cost (SI) \n (all costs included except filtration media)')
plt.xlabel("Filter flow $ (m^{3}/h) $")
plt.ylabel('Cost (1979 USD)')
plt.savefig("filter_pressure_gravity_operation_cost_m.pdf", bbox_inches='tight')





#
## Filter (container) Area < 350 ft2
##Matches http://matche.com/equipcost/Filter.html
#filter_container_area_sqft = np.arange(12, 350, 20)
#filter_container_area_m2 = filter_container_area_sqft*sqft_to_m2
#filter_container_cost_2014_USD = np.array([28800, 46700, 59300, 69600, 78500, 86500, 93800, 100500, 106800, 112700, 118400, 123700, 128900, 133800, 138600, 143100, 147600])
#
##Fit investment cost
#
##def filter_container_cost(xdata, a):
##    return (a**xdata) #Negative exp function
#
##def filter_container_cost(xdata, a):
##    return (xdata**a) # exp function
#
##def filter_container_cost(xdata, a, b, c, d):
##    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly
#
#def filter_container_cost(xdata, a, b, c):
#    return a*xdata*xdata+b*xdata+c #Second order poly
#
##def filter_container_cost(xdata, a, b):
##    return a*xdata+b #First order poly
#
##def filter_container_cost(xdata, a, b, c, d, e):
##    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly
#
##def filter_container_cost(xdata, a, b, c):
##    return a/(1+((xdata)*b)**(c)) #Sigmoidal function
#
##def filter_container_cost(xdata, a, b):
##    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
#
## m2
#plt.figure()
#parameters_filter_container_cost_m, cov_filter_container_cost_m = curve_fit(filter_container_cost, filter_container_area_m2, filter_container_cost_2014_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_container_area_m2, filter_container_cost_2014_USD)
#plt.plot(filter_container_area_m2, filter_container_cost(filter_container_area_m2, *parameters_filter_container_cost_m), 'k--', label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_filter_container_cost_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Filter (container) investment cost (SI) \n  (all costs included except filtration media)')
#plt.xlabel("Filter area $ (m^{2}) $")
#plt.ylabel('Cost 2014 USD')
#plt.savefig("filter_container_cost_m.pdf", bbox_inches='tight')
#
##sqft
#plt.figure()
#parameters_filter_container_cost_sqft, cov_filter_container_cost_sqft = curve_fit(filter_container_cost, filter_container_area_sqft, filter_container_cost_2014_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_container_area_sqft, filter_container_cost_2014_USD)
#plt.plot(filter_container_area_sqft, filter_container_cost(filter_container_area_sqft, *parameters_filter_container_cost_sqft), 'k--', label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_filter_container_cost_sqft)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Filter (container) investment cost (British Empire) \n  (all costs included except filtration media)')
#plt.xlabel("Filter area $ (sqft) $")
#plt.ylabel('Cost 2014 USD')
#plt.savefig("filter_container_cost_sqft.pdf", bbox_inches='tight')
#
#
#
#
## Filter ((civil construction)) Area > 350 ft2
##EPA Estimating Water Treatment Costs 1979
#
##Filter investment and operation cost (all costs included except filtration media)
#filter_civil_area_sqft = np.array([140, 700, 1400, 7000, 14000, 28000])
#filter_civil_area_m2 = filter_civil_area_sqft*sqft_to_m2
#
#filter_civil_cost_1979_USD = np.array([166990, 407080, 624230, 1907320, 3007480,  5602030])
#operation_cost_1979_USD = np.array([11120, 22070, 33390, 94900, 156580,  340400])
#
##Backwash investment and operation cost
#pumping_capacity_GPM = np.array([1.8, 4.5, 9.1, 25.9, 33])
#pumping_capacity_cuft_hr = pumping_capacity_GPM*GPM_to_cuft_hr
#pumping_capacity_m3_day = pumping_capacity_cuft_hr*cuft_to_m3*24
#
#backwash_cost_1979_USD = np.array([43220, 60650, 89340, 169660, 214410])
#backwash_operation_cost_1979_USD = np.array([2700, 3700, 5300, 11420, 17730, 29500])
#
#
##Fit investment cost
#
##def filter_civil_cost(xdata, a):
##    return (a**xdata) #Negative exp function
#
##def filter_civil_cost(xdata, a, b, c, d):
##    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly
#
##def filter_civil_cost(xdata, a, b, c):
##    return a*xdata*xdata+b*xdata+c #Second order poly
#
#def filter_civil_cost(xdata, a, b):
#    return a*xdata+b #First order poly
#
##def filter_civil_cost(xdata, a, b, c, d, e):
##    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly
#
##def filter_civil_cost(xdata, a, b, c):
##    return a/(1+((xdata)*b)**(c)) #Sigmoidal function
#
##def filter_civil_cost(xdata, a, b):
##    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
#
## m2
#plt.figure()
#parameters_filter_civil_cost_m, cov_filter_civil_cost_m = curve_fit(filter_civil_cost, filter_civil_area_m2, filter_civil_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_civil_area_m2, filter_civil_cost_1979_USD)
#plt.plot(filter_civil_area_m2, filter_civil_cost(filter_civil_area_m2, *parameters_filter_civil_cost_m), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_filter_civil_cost_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Filter (civil) investment cost (SI) \n  (all costs included except filtration media)')
#plt.xlabel("Filter area $ (m^{2}) $")
#plt.ylabel('Cost 1979 USD')
#plt.savefig("filter_civil_cost_m.pdf", bbox_inches='tight')
#
#
##sqft
#plt.figure()
#parameters_filter_civil_cost_sqft, cov_filter_civil_cost_sqft = curve_fit(filter_civil_cost, filter_civil_area_sqft, filter_civil_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_civil_area_sqft, filter_civil_cost_1979_USD)
#plt.plot(filter_civil_area_sqft, filter_civil_cost(filter_civil_area_sqft, *parameters_filter_civil_cost_sqft), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_filter_civil_cost_sqft)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Filter (civil) investment cost (British Empire) \n (all costs included except filtration media)')
#plt.xlabel("Filter area $ (ft^{2}) $")
#plt.ylabel('Cost 1979 USD')
#plt.savefig("filter_civil_cost_sqft.pdf", bbox_inches='tight')
#
#
##Fit operation cost
#
##def filter_operation_cost(xdata, a):
##    return (a**xdata) #Negative exp function
#
##def filter_operation_cost(xdata, a, b, c, d):
##    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly
#
##def filter_operation_cost(xdata, a, b, c):
##    return a*xdata*xdata+b*xdata+c #Second order poly
#
#def filter_operation_cost(xdata, a, b):
#    return a*xdata+b #First order poly
#
##def filter_operation_cost(xdata, a, b, c, d, e):
##    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly
#
##def filter_operation_cost(xdata, a, b, c):
##    return a/(1+((xdata)*b)**(c)) #Sigmoidal function
#
##def filter_operation_cost(xdata, a, b):
##    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
#    
## m2   
#plt.figure()
##plt.tight_layout()
#parameters_filter_operation_cost_m, cov_filter_operation_cost_m = curve_fit(filter_operation_cost, filter_civil_area_m2, operation_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_civil_area_m2, operation_cost_1979_USD)
#plt.plot(filter_civil_area_m2, filter_operation_cost(filter_civil_area_m2, *parameters_filter_operation_cost_m), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_filter_operation_cost_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Filter operation cost (SI)')
#plt.xlabel("Filter area $ (m^{2}) $")
#plt.ylabel('Cost 1979 USD / year')
#plt.savefig("filter_operation_cost_m.pdf", bbox_inches='tight')
#
#
##sqft
#plt.figure()
#parameters_filter_operation_cost_sqft, cov_filter_operation_cost_sqft = curve_fit(filter_operation_cost, filter_civil_area_sqft, operation_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_civil_area_sqft, operation_cost_1979_USD)
#plt.plot(filter_civil_area_sqft, filter_operation_cost(filter_civil_area_sqft, *parameters_filter_operation_cost_sqft), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_filter_operation_cost_sqft)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Filter investment cost (British Empire)')
#plt.xlabel("Filter area $ (ft^{2}) $")
#plt.ylabel('Cost 1979 USD / year')
#plt.savefig("filter_operation_cost_sqft.pdf", bbox_inches='tight')
#
#
##Fit backwash investment cost
#
##def backwash_cost(xdata, a):
##    return (a**xdata) #Negative exp function
#
##def backwash_cost(xdata, a, b, c, d):
##    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly
#
##def backwash_cost(xdata, a, b, c):
##    return a*xdata*xdata+b*xdata+c #Second order poly
#
#def backwash_cost(xdata, a, b):
#    return a*xdata+b #First order poly
#
##def backwash_cost(xdata, a, b, c, d, e):
##    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly
#
##def backwash_cost(xdata, a, b, c):
##    return a/(1+((xdata)*b)**(c)) #Sigmoidal function
#
##def backwash_cost(xdata, a, b):
##    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
#
## m3/day
#plt.figure()
#parameters_backwash_cost_m, cov_backwash_cost_m = curve_fit(backwash_cost, pumping_capacity_m3_day, backwash_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(pumping_capacity_m3_day, backwash_cost_1979_USD)
#plt.plot(pumping_capacity_m3_day, backwash_cost(pumping_capacity_m3_day, *parameters_backwash_cost_m), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_backwash_cost_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Backwash investment cost (SI)')
#plt.xlabel("Pumping capacity $ (m^{3} / day) $")
#plt.ylabel('Cost 1979 USD')
#plt.savefig("backwash_cost_m.pdf", bbox_inches='tight')
#
## cuft/hr
#plt.figure()
#parameters_backwash_cost_cuft, cov_backwash_cost_cuft = curve_fit(backwash_cost, pumping_capacity_cuft_hr, backwash_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(pumping_capacity_cuft_hr, backwash_cost_1979_USD)
#plt.plot(pumping_capacity_cuft_hr, backwash_cost(pumping_capacity_cuft_hr, *parameters_backwash_cost_cuft), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_backwash_cost_cuft)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Backwash investment cost (Bristish Empire)')
#plt.xlabel("Pumping capacity $ (cuft / hr) $")
#plt.ylabel('Cost 1979 USD')
#plt.savefig("backwash_cost_cuft.pdf", bbox_inches='tight')
#
##Fit backwash operation cost
#
##def backwash_operation_cost(xdata, a):
##    return (a**xdata) #Negative exp function
#
##def backwash_operation_cost(xdata, a, b, c, d):
##    return a*xdata*xdata*xdata+b*xdata*xdata+c*xdata+d #Third order poly
#
##def backwash_operation_cost(xdata, a, b, c):
##    return a*xdata*xdata+b*xdata+c #Second order poly
#
#def backwash_operation_cost(xdata, a, b):
#    return a*xdata+b #First order poly
#
##def backwash_operation_cost(xdata, a, b, c, d, e):
##    return a*xdata*xdata*xdata*xdata+b*xdata*xdata*xdata+c*xdata*xdata+d*xdata+e #Fourth order poly
#
##def backwash_operation_cost(xdata, a, b, c):
##    return a/(1+((xdata)*b)**(c)) #Sigmoidal function
#
##def backwash_operation_cost(xdata, a, b):
##    return a*(np.tanh(xdata))+b #-tanh function (hyperbolic)
#
## m2
#plt.figure()
#parameters_backwash_operation_cost_m, cov_backwash_operation_cost_m = curve_fit(backwash_operation_cost, filter_civil_area_m2, backwash_operation_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_civil_area_m2, backwash_operation_cost_1979_USD)
#plt.plot(filter_civil_area_m2, backwash_operation_cost(filter_civil_area_m2, *parameters_backwash_operation_cost_m), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_backwash_operation_cost_m)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Backwash operation cost (SI)')
#plt.xlabel("Filter area $ (m^{2}) $")
#plt.ylabel('Cost 1979 USD / year')
#plt.savefig("backwash_operation_cost_m.pdf", bbox_inches='tight')
#
## sqrt
#plt.figure()
#parameters_backwash_operation_cost_sqft, cov_backwash_operation_cost_sqft = curve_fit(backwash_operation_cost, filter_civil_area_sqft, backwash_operation_cost_1979_USD)
##
##with sns.plotting_context("paper") and sns.axes_style("darkgrid"):
##    sns.relplot(x="Ca", y="StrYield", kind="line", ci=90, color="red", data=bigdata, label='Average results and 90% confidence interval')
#plt.plot(filter_civil_area_sqft, backwash_operation_cost_1979_USD)
#plt.plot(filter_civil_area_sqft, backwash_operation_cost(filter_civil_area_sqft, *parameters_backwash_operation_cost_sqft), 'k--', label='Fit: a=%5.3f, b=%5.3f' % tuple(parameters_backwash_operation_cost_sqft)) #label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(parameters_StrYield)
#plt.legend(loc='upper left')
#plt.title('Backwash operation cost (British Empire)')
#plt.xlabel("Filter area $ (ft^{2}) $")
#plt.ylabel('Cost 1979 USD / year')
#plt.savefig("backwash_operation_cost_sqft.pdf", bbox_inches='tight')
