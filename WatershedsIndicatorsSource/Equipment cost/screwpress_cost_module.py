# ===============================================================================================================================================================================================================================
# ###############################################################################################################################################################################################################################
# ===============================================================================================================================================================================================================================
# IMPORT LIBRARIES MODULE
import numpy as np
import pandas as pd
import scipy.optimize as opt
from scipy.integrate import odeint, solve_bvp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

F_tot_list=np.arange(0.1,1600,5)
Flow=[]
Op_cost=[]
Cap_cost=[]

for F_tot in F_tot_list:
#def screw_press_cost_module(F_tot): #F_tot is measured in m3/day

    from global_parameters_module import UnitConv, MW, c_p_liq_sol, dH_vap_0, Tc, Tb, dH_f, dH_c, c_p_v_1, c_p_v_2, c_p_v_3, c_p_v_4, coef_vapor_pressure_1, coef_vapor_pressure_2, coef_vapor_pressure_3, CEI, price, nu_p, k_p, n_watson, epsilon, T_amb, P_ref, density, latent_heat_evap, nat_gas_heat_value
    #from feedstock_input_module import elements_wet, elements_dry, nutrients, feedstock_parameters, elements_dry_comp
    from economic_parameters_module import ec_param
    
    
    #SIZES FOR SCREW PRESS FOR SLUDGE DEWATERING (PWTech)
    
    #PWTech http://pwtech.us/HTML/addResources.html
    diameter_inch = np.array([9.1, 13.8, 16.5, 16.5, 16.5, 22.25, 22.25, 22.25])
    diameter_m = diameter_inch*UnitConv['inch_to_m']
    
    n_units = np.array([1, 1, 1, 2, 3, 2, 3, 4])
    
    flow_GPM = np.array([8, 15, 35, 70, 105, 130, 200, 265])
    flow_cuft_hr = flow_GPM*UnitConv['GPM_to_cuft_hr']
    flow_m3_day = flow_cuft_hr*UnitConv['cuft_to_m3']*24
    
    power_HP = np.array([0.4, 0.6, 1.2, 1.7, 2.7, 5.2, 8.5, 10.5])
    power_kW = power_HP*UnitConv['HP_to_kW']
    
    ScrewPress_diameter = []
    n_ScrewPress = []
    power_kW_ScrewPress = []
    
    if F_tot <= flow_m3_day[0]:
        ScrewPress_diameter = diameter_m[0]
        n_ScrewPress = n_units[0]
        power_kW_ScrewPress = power_kW[0]
    
    elif flow_m3_day[0] < F_tot <= flow_m3_day[-1]:
        for i in flow_m3_day[:-1]:
            index = np.int(np.where(flow_m3_day == i)[0])
            if flow_m3_day[index] < F_tot <= flow_m3_day[index+1]:
                ScrewPress_diameter = diameter_m[index+1]
                n_ScrewPress = n_units[index+1]
                power_kW_ScrewPress = power_kW[index+1]
                break
                
    elif F_tot > flow_m3_day[-1]:
        ScrewPress_diameter = diameter_m[-1]
        n_ScrewPress = np.ceil(F_tot/(flow_m3_day[5]/2))
        power_kW_ScrewPress = power_kW[-1]
        
        
    # =============================================================================
    # Cost
    # =============================================================================
    screwpress_cost_2014_USD = n_ScrewPress*(23221.804*ScrewPress_diameter**2+24708.740*ScrewPress_diameter - 2547.881)
    screwpress_cost_2016_USD = screwpress_cost_2014_USD*(CEI[2016]/CEI[2014])
    
    screwpress_PPC_2016_USD = 3.15*screwpress_cost_2016_USD
    investment_cost = 1.4*screwpress_PPC_2016_USD
    
    if F_tot <= flow_m3_day[-1]:
        operation_cost_2016_non_amortized = power_kW_ScrewPress*3600*24*365/3600*price['electricity'] #USD/year
        operation_cost_2016_amortized = power_kW_ScrewPress*3600*24*365/3600*price['electricity']+investment_cost/ec_param['plant_lifetime'] #USD/year
    elif F_tot > flow_m3_day[-1]:
        operation_cost_2016_non_amortized = power_kW_ScrewPress*3600*24*365/3600*price['electricity']*(n_ScrewPress/4) #USD/year
        operation_cost_2016_amortized = power_kW_ScrewPress*3600*24*365/3600*price['electricity']*(n_ScrewPress/4)+investment_cost/ec_param['plant_lifetime'] #USD/year
        
    Flow.append(F_tot)
    Op_cost.append(operation_cost_2016_non_amortized)
    Cap_cost.append(screwpress_cost_2016_USD)
    
    #return {'ScrewPress_diameter':ScrewPress_diameter, 'n_ScrewPress':n_ScrewPress, 'power_kW_ScrewPress':power_kW_ScrewPress, 
            #'equipment_cost':screwpress_cost_2016_USD,
            #'screwpress_PPC':screwpress_PPC_2016_USD,
            #'investment_cost':investment_cost,
            #'operation_cost_2016_non_amortized':operation_cost_2016_non_amortized,
            #'operation_cost_2016_amortized':operation_cost_2016_amortized,
            #}
ScrewpressCost_df = pd.DataFrame()
ScrewpressCost_df['Flow (m3/day)']=Flow
ScrewpressCost_df['Operation cost (USD/year)']=Op_cost
ScrewpressCost_df['Capital cost (USD)']=Cap_cost
ScrewpressCost_df.to_csv('ScrewpressCost_df')

plt.figure()
plt.plot(Flow, Op_cost)
#plt.title('Screw press (SI) Op Cost')
plt.xlabel("Flow (m3/day)")
plt.ylabel('Cost (2016 USD/year)')
plt.savefig("screwpress_Op_cost.pdf",bbox_inches='tight')  

plt.figure()
plt.plot(Flow, Cap_cost)
#plt.title('Screw press (SI) Capt Cost')
plt.xlabel("Flow (m3/day)")
plt.ylabel('Cost (2016 USD)')
plt.savefig("screwpress_Cap_cost.pdf",bbox_inches='tight') 
