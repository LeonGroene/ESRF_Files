import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Import the relevant parts of DAXS
from daxs.measurements import Source, Xes


###########################################################################################################################
# Sample 
###########################################################################################################################

# Define the counters to process for xes:
counters_xes = {
    "x": "xes_en",                # Define the x-axis, here the emission energy
    "signal": ["det_dtc_apd"],    # Define the data counter, here the main apd detector with dead-time correction
    "monitor": "I02",             # Define the counter used for normalization
}

# Define the datafile and the scan numbers
fname = "/data/visitor/hc4929/id26/cell_22_xanes_ZnS_olga/cell_22_xanes_ZnS_olga_0001/cell_22_xanes_ZnS_olga_0001.h5"
source1 = Source(fname, 10, None)
source2 = Source(fname, 12, None)
source3 = Source(fname, 14, None)   # Give first filename, then numbers of scans to include, then numbers of scans to exclude (if any, here None)
conc_corr_scan1 = 11     # Define the scan number for the concentration correction
conc_corr_scan2 = 13 
conc_corr_scan3 = 15 
                               
# Create an object that contains the data
measurement1 = Xes(source1, counters=counters_xes)   # Sets the measurement type to Xes. The data is from the source object above and counters to process are the ones defined above in counters dictionary
measurement2 = Xes(source2, counters=counters_xes)
measurement3 = Xes(source3, counters=counters_xes)

# Adjusts the measured data by the concentration correction
measurement1.concentration_correction(conc_corr_scan1)
measurement2.concentration_correction(conc_corr_scan2)
measurement3.concentration_correction(conc_corr_scan3)

#measurement1.normalize(mode="maximum")   # Optional, can leave out. How to normalize the data, can be 'area' or 'maximum'
#measurement2.normalize(mode="maximum") 
#measurement3.normalize(mode="maximum") 


############# new normalisation for 3 plot with 3 parts
measurement2_norm  = measurement2.signal * (measurement1.signal[0]/measurement2.signal[-1] )








###########################################################################################################################
# Reference Cu2O
###########################################################################################################################
counters_xes_Cu2O = {
    "x": "xes_en",                # Define the x-axis, here the emission energy
    "signal": ["det_dtc_apd"],    # Define the data counter, here the main apd detector with dead-time correction
    "monitor": "I02",             # Define the counter used for normalization
}

measurements_Cu2O = list()
# Define the datafile and the scan numbers
fname_Cu2O = "/data/visitor/hc4929/id26/Cu2O-exsitu-XES/Cu2O-exsitu-XES_0001/Cu2O-exsitu-XES_0001.h5"   # Give first filename, then numbers of scans to include, then numbers of scans to exclude (if any, here None)                                  # Define the scan number for the concentration correction

source_Cu2O1 = Source(fname_Cu2O, 1, None)
source_Cu2O2 = Source(fname_Cu2O, 3, None)
source_Cu2O3 = Source(fname_Cu2O, 5, None)
        
conc_corr_scan_Cu2O1 = 2  
conc_corr_scan_Cu2O2 = 4  
conc_corr_scan_Cu2O3 = 6  

# Create an object that contains the data
measurement_Cu2O1 = Xes(source_Cu2O1, counters=counters_xes_Cu2O)   # Sets the measurement type to Xes. The data is from the source object above and counters to process are the ones defined above in counters dictionary
measurement_Cu2O2 = Xes(source_Cu2O2, counters=counters_xes_Cu2O) 
measurement_Cu2O3 = Xes(source_Cu2O3, counters=counters_xes_Cu2O) 

# Adjusts the measured data by the concentration correction
measurement_Cu2O1.concentration_correction(conc_corr_scan_Cu2O1)
measurement_Cu2O2.concentration_correction(conc_corr_scan_Cu2O2)
measurement_Cu2O3.concentration_correction(conc_corr_scan_Cu2O3)

#measurement_Cu2O.normalize(mode="area")   # Optional, can leave out. How to normalize the data, can be 'area' or 'maximum'


###########################################################################################################################
# Reference CuO
###########################################################################################################################
### CuO_1 #2 reference measurements pf CuO, will be averaged in plotting section
counters_xes_CuO_1 = {
    "x": "xes_en",                # Define the x-axis, here the emission energy
    "signal": ["det_dtc_apd"],    # Define the data counter, here the main apd detector with dead-time correction
    "monitor": "I02",             # Define the counter used for normalization
}

# Define the datafile and the scan numbers
fname_CuO_1 = "/data/visitor/hc4929/id26/CuO-exsitu-XES/CuO-exsitu-XES_0001/CuO-exsitu-XES_0001.h5"
source_CuO1_1 = Source(fname_CuO_1, 1, None)   # Give first filename, then numbers of scans to include, then numbers of scans to exclude (if any, here None)
source_CuO2_1 = Source(fname_CuO_1, 3, None)
source_CuO3_1 = Source(fname_CuO_1, 5, None)

conc_corr_scan_CuO1_1 = 2                                    # Define the scan number for the concentration correction
conc_corr_scan_CuO2_1 = 4 
conc_corr_scan_CuO3_1 = 6 
# Create an object that contains the data
measurement_CuO1_1 = Xes(source_CuO1_1, counters=counters_xes_CuO_1)   # Sets the measurement type to Xes. The data is from the source object above and counters to process are the ones defined above in counters dictionary
measurement_CuO2_1 = Xes(source_CuO2_1, counters=counters_xes_CuO_1)
measurement_CuO3_1 = Xes(source_CuO3_1, counters=counters_xes_CuO_1)

# Adjusts the measured data by the concentration correction
measurement_CuO1_1.concentration_correction(conc_corr_scan_CuO1_1)
measurement_CuO2_1.concentration_correction(conc_corr_scan_CuO2_1)
measurement_CuO3_1.concentration_correction(conc_corr_scan_CuO3_1)

#measurement_CuO.normalize(mode="area")   # Optional, can leave out. How to normalize the data, can be 'area' or 'maximum'

### CuO_2
counters_xes_CuO_2= {
    "x": "xes_en",                # Define the x-axis, here the emission energy
    "signal": ["det_dtc_apd"],    # Define the data counter, here the main apd detector with dead-time correction
    "monitor": "I02",             # Define the counter used for normalization
}

# Define the datafile and the scan numbers
fname_CuO_2 = "/data/visitor/hc4929/id26/CuO-exsitu-Xes-2/CuO-exsitu-Xes-2_0001/CuO-exsitu-Xes-2_0001.h5"
source_CuO1_2 = Source(fname_CuO_2, 1, None)   # Give first filename, then numbers of scans to include, then numbers of scans to exclude (if any, here None)
source_CuO2_2 = Source(fname_CuO_2, 3, None)
source_CuO3_2 = Source(fname_CuO_2, 5, None)

conc_corr_scan_CuO1_2 = 2                                    # Define the scan number for the concentration correction
conc_corr_scan_CuO2_2 = 4 
conc_corr_scan_CuO3_2 = 6 
# Create an object that contains the data
measurement_CuO1_2 = Xes(source_CuO1_2, counters=counters_xes_CuO_2)   # Sets the measurement type to Xes. The data is from the source object above and counters to process are the ones defined above in counters dictionary
measurement_CuO2_2 = Xes(source_CuO2_2, counters=counters_xes_CuO_2)
measurement_CuO3_2 = Xes(source_CuO3_2, counters=counters_xes_CuO_2)

# Adjusts the measured data by the concentration correction
measurement_CuO1_2.concentration_correction(conc_corr_scan_CuO1_2)
measurement_CuO2_2.concentration_correction(conc_corr_scan_CuO2_2)
measurement_CuO3_2.concentration_correction(conc_corr_scan_CuO3_2)

#measurement_CuO.normalize(mode="area")   # Optional, can leave out. How to normalize the data, can be 'area' or 'maximum'

###########################################################################################################################
# Reference Cu3N
###########################################################################################################################
counters_xes_Cu3N = {
    "x": "xes_en",                # Define the x-axis, here the emission energy
    "signal": ["det_dtc_apd"],    # Define the data counter, here the main apd detector with dead-time correction
    "monitor": "I02",             # Define the counter used for normalization
}

# Define the datafile and the scan numbers
fname_Cu3N = "/data/visitor/hc4929/id26/Cu3N-exsitu-XES/Cu3N-exsitu-XES_0001/Cu3N-exsitu-XES_0001.h5"
source_Cu3N1 = Source(fname_Cu3N, 1, None)   # Give first filename, then numbers of scans to include, then numbers of scans to exclude (if any, here None)
source_Cu3N2 = Source(fname_Cu3N, 3, None)
source_Cu3N3 = Source(fname_Cu3N, 5, None)

conc_corr_scan_Cu3N1 = 2                                    # Define the scan number for the concentration correction
conc_corr_scan_Cu3N2 = 4
conc_corr_scan_Cu3N3 = 6

# Create an object that contains the data
measurement_Cu3N1 = Xes(source_Cu3N1, counters=counters_xes_Cu3N)   # Sets the measurement type to Xes. The data is from the source object above and counters to process are the ones defined above in counters dictionary
measurement_Cu3N2 = Xes(source_Cu3N2, counters=counters_xes_Cu3N)
measurement_Cu3N3 = Xes(source_Cu3N3, counters=counters_xes_Cu3N)

# Adjusts the measured data by the concentration correction
measurement_Cu3N1.concentration_correction(conc_corr_scan_Cu3N1)
measurement_Cu3N2.concentration_correction(conc_corr_scan_Cu3N2)
measurement_Cu3N3.concentration_correction(conc_corr_scan_Cu3N3)

#measurement_Cu3N.normalize(mode="area")   # Optional, can leave out. How to normalize the data, can be 'area' or 'maximum'

###########################################################################################################################
# Reference CuOCH3
###########################################################################################################################
counters_xes_CuOCH3 = {
    "x": "xes_en",                # Define the x-axis, here the emission energy
    "signal": ["det_dtc_apd"],    # Define the data counter, here the main apd detector with dead-time correction
    "monitor": "I02",             # Define the counter used for normalization
}

# Define the datafile and the scan numbers
fname_CuOCH3 = "/data/visitor/hc4929/id26/CuOCH3-exsitu-XES/CuOCH3-exsitu-XES_0001/CuOCH3-exsitu-XES_0001.h5"
source_CuOCH31 = Source(fname_CuOCH3, 6, None)   # Give first filename, then numbers of scans to include, then numbers of scans to exclude (if any, here None)
source_CuOCH32 = Source(fname_CuOCH3, 8, None)
source_CuOCH33 = Source(fname_CuOCH3, 10, None)

conc_corr_scan_CuOCH31 = 7                                    # Define the scan number for the concentration correction
conc_corr_scan_CuOCH32 = 9
conc_corr_scan_CuOCH33 = 11

# Create an object that contains the data
measurement_CuOCH31 = Xes(source_CuOCH31, counters=counters_xes_CuOCH3)   # Sets the measurement type to Xes. The data is from the source object above and counters to process are the ones defined above in counters dictionary
measurement_CuOCH32 = Xes(source_CuOCH32, counters=counters_xes_CuOCH3)
measurement_CuOCH33 = Xes(source_CuOCH33, counters=counters_xes_CuOCH3)

# Adjusts the measured data by the concentration correction
measurement_CuOCH31.concentration_correction(conc_corr_scan_CuOCH31)
measurement_CuOCH32.concentration_correction(conc_corr_scan_CuOCH32)
measurement_CuOCH33.concentration_correction(conc_corr_scan_CuOCH33)

#measurement_Cu3N.normalize(mode="area")   # Optional, can leave out. How to normalize the data, can be 'area' or 'maximum'

###########################################################################################################################
# Reference Cuacac2
###########################################################################################################################
counters_xes_Cuacac2 = {
    "x": "xes_en",                # Define the x-axis, here the emission energy
    "signal": ["det_dtc_apd"],    # Define the data counter, here the main apd detector with dead-time correction
    "monitor": "I02",             # Define the counter used for normalization
}

# Define the datafile and the scan numbers
fname_Cuacac2 = "/data/visitor/hc4929/id26/Cuacac2-exsitu-XES/Cuacac2-exsitu-XES_0001/Cuacac2-exsitu-XES_0001.h5"
source_Cuacac21 = Source(fname_Cuacac2, 1, None)   # Give first filename, then numbers of scans to include, then numbers of scans to exclude (if any, here None)
source_Cuacac22 = Source(fname_Cuacac2, 3, None)
source_Cuacac23 = Source(fname_Cuacac2, 5, None)

conc_corr_scan_Cuacac21 = 2                                    # Define the scan number for the concentration correction
conc_corr_scan_Cuacac22 = 4
conc_corr_scan_Cuacac23 = 6

# Create an object that contains the data
measurement_Cuacac21 = Xes(source_Cuacac21, counters=counters_xes_Cuacac2)   # Sets the measurement type to Xes. The data is from the source object above and counters to process are the ones defined above in counters dictionary
measurement_Cuacac22 = Xes(source_Cuacac22, counters=counters_xes_Cuacac2)
measurement_Cuacac23 = Xes(source_Cuacac23, counters=counters_xes_Cuacac2)

# Adjusts the measured data by the concentration correction
measurement_Cuacac21.concentration_correction(conc_corr_scan_Cuacac21)
measurement_Cuacac22.concentration_correction(conc_corr_scan_Cuacac22)
measurement_Cuacac23.concentration_correction(conc_corr_scan_Cuacac23)

#measurement_Cu3N.normalize(mode="area")   # Optional, can leave out. How to normalize the data, can be 'area' or 'maximum'


###########################################################################################################################
# Plotting
###########################################################################################################################
# plots the x, y data of the measurement defined above
fig, ax = plt.subplots(figsize=(7, 5))  
ax.title.set_text('Single VtC scan with concentration correction') 
ax.set_xlabel("Energy (keV)")
ax.set_ylabel("Intensity (arb. units)")
l0, = ax.plot(measurement1.x, measurement1.signal, label="Sample", color="red") 
l02, = ax.plot(measurement2.x, measurement2_norm, color="red") 
l03, = ax.plot(measurement3.x, measurement3.signal, color="red")   # The x and y values to plot
l1, = ax.plot(measurement_CuO1_1.x, (measurement_CuO1_1.signal + measurement_CuO1_2.signal) / 2, label="CuO", color="blue")  
l12, = ax.plot(measurement_CuO2_1.x, (measurement_CuO2_1.signal + measurement_CuO2_2.signal) / 2, color="blue")  
l13, = ax.plot(measurement_CuO3_1.x, (measurement_CuO3_1.signal + measurement_CuO3_2.signal) / 2, color="blue")  
l2, = ax.plot(measurement_Cu2O1.x, measurement_Cu2O1.signal, label="Cu$_{2}$O", color="orange")  
l22, = ax.plot(measurement_Cu2O2.x, measurement_Cu2O2.signal, color="orange") 
l23, = ax.plot(measurement_Cu2O3.x, measurement_Cu2O3.signal, color="orange") 
l3, = ax.plot(measurement_Cu3N1.x, measurement_Cu3N1.signal, label="Cu$_{3}$N", color="limegreen") 
l32, = ax.plot(measurement_Cu3N2.x, measurement_Cu3N2.signal, color="limegreen") 
l33, = ax.plot(measurement_Cu3N3.x, measurement_Cu3N3.signal, color="limegreen")
l4, = ax.plot(measurement_CuOCH31.x, measurement_CuOCH31.signal, label="Cu(OMe)$_{2}$", color="darkgreen") 
l42, = ax.plot(measurement_CuOCH32.x, measurement_CuOCH32.signal, color="darkgreen") 
l43, = ax.plot(measurement_CuOCH33.x, measurement_CuOCH33.signal, color="darkgreen")
l5, = ax.plot(measurement_Cuacac21.x, measurement_Cuacac21.signal, label="Cuacac$_{2}$", color="magenta") 
l52, = ax.plot(measurement_Cuacac22.x, measurement_Cuacac22.signal, color="magenta") 
l53, = ax.plot(measurement_Cuacac23.x, measurement_Cuacac23.signal, color="magenta")
ax.legend()
plt.subplots_adjust(left=0.3)
plt.tight_layout()



lines = [l0,l1,l2,l3,l4,l5]

rax = plt.axes([0.15,0.15,0.1,0.15])
labels = [str(line.get_label()) for line in lines]
visibility = [str(line.get_visible()) for line in lines]
check = CheckButtons(rax, labels, visibility)

def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    if index == 0:
        l02.set_visible(not l02.get_visible())
        l03.set_visible(not l03.get_visible())
    if index == 1:
        l12.set_visible(not l12.get_visible())
        l13.set_visible(not l13.get_visible())
    if index == 2:
        l22.set_visible(not l22.get_visible())
        l23.set_visible(not l23.get_visible())
    if index == 3:
        l32.set_visible(not l32.get_visible())
        l33.set_visible(not l33.get_visible())
    if index == 4:
        l42.set_visible(not l42.get_visible())
        l43.set_visible(not l43.get_visible())
    if index == 5:
        l52.set_visible(not l52.get_visible())
        l53.set_visible(not l53.get_visible())
    plt.draw()
    
check.on_clicked(func)
plt.show()