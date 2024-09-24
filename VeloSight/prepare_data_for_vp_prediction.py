# -*- coding: utf-8 -*-
"""

Prepare Data for Vp Prediction

This program is designed to be run in the command line. 
It prompts users for information about their data and file locations.
After reading in data, it will generate the data structure necessary
for input into the machine learning model. It will also generate a 
pdf figure of the data for viewing/printing.

Copyright 2024 Jenna Everard

"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Helpers.read_data import read_res_gr_files, read_vp_files
from Helpers.depth import normalize_depth, interpolate_data
from Helpers.data_characteristics import calc_noise, calc_window_deriv

def main():
    
    print("For Version 1.0.1 users, please ensure gamma ray is reported in units of gAPI and resistivity is reported in units of ohm.m\n\n")
    
    site_name = input("Please Enter the Site/Hole Name: ")
    
    print("\nWhich data format are you using?\n\t1. csv\n\t2. dlis\n\t3. las")
    data_type = input("Enter an option (1-3): ")
    
    valid_data_type = False
    while not valid_data_type:
        try:
            data_type = int(data_type)
            if data_type == 1:
                valid_data_type = True
            elif data_type == 2:
                print("\nSupport for DLIS files coming soon. Terminating program now.\n")
                return
            elif data_type == 3:
                print("\nSupport for LAS files coming soon. Termining program now.\n")
                return
            else:
                data_type = input("Please enter either 1, 2, or 3: ")
        except ValueError:
            data_type = input("Please enter a number: ")
            
    if data_type == 1:
        print("\nReading data files...\n")
        depth_gr, gr, depth_res, deep_res, medium_res, shallow_res, ring_res, bit_res = read_res_gr_files()
    elif data_type == 2:
        # read dlis files - NOT YET IMPLEMENTED
        pass
    else:
        # read las files - NOT YET IMPLEMENTED
        pass
    
    print("\nIf you have VCO data already, would you like to plot it too?\n")
    plot_vp = input("Enter YES or NO: ")
    valid_answer = False
    while not valid_answer:
        if plot_vp.lower() == 'yes' or plot_vp.lower() == 'no':
            valid_answer = True
            if plot_vp.lower() == 'yes':
                print("\nReading VCO data files...\n")
                depth_vp, vp = read_vp_files()
        else:
            plot_vp = input("Not a valid input, please try again: ")
    
    print("\nWhat unit is depth reported in?\n\t1.m\n\t2.km\n\t3.ft")
    depth_unit_type = input("Enter an option (1-3): ")
    
    print("\nConverting depth to meters...\n")
    valid_data_type = False
    while not valid_data_type:
        try:
            depth_unit_type = int(depth_unit_type)
            if depth_unit_type == 1:
                valid_data_type = True
            elif depth_unit_type == 2:
                depth_gr = depth_gr / 1000
                depth_res = depth_res / 1000
                depth_vp = depth_vp / 1000
            elif depth_unit_type == 3:
                print("\nWhy would you use feet?! Oh well...guess I'll deal with it :/\n")
                depth_gr = depth_gr / 3.28
                depth_res = depth_res / 3.28
                depth_vp = depth_vp / 3.28
            else:
                depth_unit_type = input("Please enter either 1, 2, or 3: ")
        except ValueError:
            depth_unit_type = input("Please enter a number: ")
    
    if plot_vp.lower() == 'yes':
        depth = normalize_depth(depth_gr, depth_res, depth_vp)
    else:
        depth = normalize_depth(depth_gr, depth_res)
    
    gr,dr,mr,sr,rr,br = interpolate_data(depth, depth_gr, depth_res, gr, 
                                         deep_res, medium_res, shallow_res, 
                                         ring_res, bit_res)
    
    print("Calculating additional data parameters...\n")
    window_size = 20
    gr_d, dr_d, mr_d, sr_d, rr_d, br_d = calc_window_deriv(
        gr, dr, mr, sr, rr, br, window_size)
    
    gr_dd, dr_dd, mr_dd, sr_dd, rr_dd, br_dd = calc_window_deriv(
        gr_d, dr_d, mr_d, sr_d, rr_d, br_d, 20)
    
    gr_n, dr_n, mr_n, sr_n, rr_n, br_n = calc_noise(
        gr, dr, mr, sr, rr, br, window_size)
    
    print("\nSaving data as a csv file...\n")
    
    data = pd.DataFrame({
        'Depth (mbsf)': depth,
        'Gamma (gAPI)': gr,
        'Deep Button Resistivity (ohm.m)': dr,
        'Medium Button Resistivity (ohm.m)': mr,
        'Shallow Button Resistivity (ohm.m)': sr,
        'Ring Resistivity (ohm.m)': rr,
        'Bit Resistivity (ohm.m)': br,
        'Gamma Derivative': gr_d,
        'Deep Derivative': dr_d,
        'Medium Derivative': mr_d,
        'Shallow Derivative': sr_d,
        'Ring Derivative': rr_d,
        'Bit Derivative': br_d,
        'Gamma Second Derivative': gr_dd,
        'Deep Second Derivative': dr_dd,
        'Medium Second Derivative': mr_dd,
        'Shallow Second Derivative': sr_dd,
        'Ring Second Derivative': rr_dd,
        'Bit Second Derivative': br_dd,
        'Gamma Noise': gr_n,
        'Deep Noise': dr_n,
        'Medium Noise': mr_n,
        'Shallow Noise': sr_n,
        'Ring Noise': rr_n,
        'Bit Noise': br_n
    })
    
    data.to_csv('../Results/' + site_name + '.csv')
    
    print(f"\nData saved at ../Results/{site_name}.csv\n")
    
    print("\nPlotting data...\n")
    
    no_ring = not np.any(ring_res)
    no_bit = not np.any(bit_res)
    no_medium = not np.any(medium_res)
    
    fig,axs = plt.subplots(1,17,figsize=(25,15), sharey=True)
    
    axs[0].plot(gr,depth, c='darkgreen', lw=0.5)
    axs[0].invert_yaxis()
    axs[0].set_title('Gamma Ray \n(gAPI)', fontsize=10)
    axs[0].set_xlim(25,125)
    
    axs[1].plot(dr,depth, c='blue',lw=0.5, label='Deep')
    if not no_medium:
        axs[1].plot(mr,depth, c='cyan',lw=0.5, label='Medium')
    axs[1].plot(sr,depth, c='lime',lw=0.5, label='Shallow')
    axs[1].set_title('Button \nResistivity \n(ohm.m)', fontsize=10)
    axs[1].legend(fontsize=8)
    axs[1].invert_yaxis()
    axs[1].set_xlim(0,3)
    
    if not no_bit:
        axs[2].plot(br,depth, c='brown',lw=0.5, label='Bit')
    if not no_ring:
        axs[2].plot(rr,depth, c='black',lw=0.5, label='Ring')
    axs[2].set_title('Bit \nResistivity \n(ohm.m)', fontsize=10)
    axs[2].legend(fontsize=8)
    axs[2].invert_yaxis()
    axs[2].set_xlim(0.5,2.5)

    axs[3].axis('off')

    axs[4].plot(gr_d,depth, c='darkgreen',lw=0.5)
    axs[4].invert_yaxis()
    axs[4].set_title('Derivative\nGamma Ray\n(gAPI)', fontsize=10)
    axs[4].set_xlim(-25,25)
    
    axs[5].plot(dr_d,depth, c='blue',lw=0.5, label='Deep')
    if not no_medium:
        axs[5].plot(mr_d,depth, c='cyan',lw=0.5, label='Medium')
    axs[5].plot(sr_d,depth, c='lime',lw=0.5, label='Shallow')
    axs[5].set_title('Derivative\nButton\nResistivity\n(ohm.m)', fontsize=10)
    axs[5].legend(fontsize=8)
    axs[5].invert_yaxis()
    axs[5].set_xlim(-2.5,2.5)
    
    if not no_bit:
        axs[6].plot(br_d,depth, c='brown',lw=0.5, label='Bit')
    if not no_ring:
        axs[6].plot(rr_d,depth, c='black',lw=0.5, label='Ring')
    axs[6].set_title('Derivative\nBit\nResistivity\n(ohm.m)', fontsize=10)
    axs[6].legend(fontsize=8)
    axs[6].invert_yaxis()
    axs[6].set_xlim(-0.5,0.5)

    axs[7].axis('off')

    axs[8].plot(gr_dd,depth, c='darkgreen',lw=0.5)
    axs[8].invert_yaxis()
    axs[8].set_title('Second\nDerivative\nGamma Ray\n(gAPI)', fontsize=10)
    axs[8].set_xlim(-50,50)
    
    axs[9].plot(dr_dd,depth, c='blue',lw=0.5, label='Deep')
    if not no_medium:
        axs[9].plot(mr_dd,depth, c='cyan',lw=0.5, label='Medium')
    axs[9].plot(sr_dd,depth, c='lime',lw=0.5, label='Shallow')
    axs[9].set_title('Second\nDerivative\nButton\nResistivity\n(ohm.m)', fontsize=10)
    axs[9].legend(fontsize=8)
    axs[9].invert_yaxis()
    axs[9].set_xlim(-2.5,2.5)
    
    if not no_bit:
        axs[10].plot(br_dd,depth, c='brown',lw=0.5, label='Bit')
    if not no_ring:
       axs[10].plot(rr_dd,depth, c='black',lw=0.5, label='Ring')
    axs[10].set_title('Second\nDerivative\nBit\nResistivity\n(ohm.m)', fontsize=10)
    axs[10].legend(fontsize=8)
    axs[10].invert_yaxis()
    axs[10].set_xlim(-2,2)

    axs[11].axis('off')

    axs[12].plot(gr_n,depth, c='darkgreen',lw=0.5)
    axs[12].invert_yaxis()
    axs[12].set_title('Noise\nGamma Ray\n(gAPI)', fontsize=10)
    axs[12].set_xlim(0,2)
    
    axs[13].plot(dr_n,depth, c='blue',lw=0.5, label='Deep')
    if not no_medium:
        axs[13].plot(mr_n,depth, c='cyan',lw=0.5, label='Medium')
    axs[13].plot(sr_n,depth, c='lime',lw=0.5, label='Shallow')
    axs[13].set_title('Noise\nButton\nResistivity\n(ohm.m)', fontsize=10)
    axs[13].legend(fontsize=8)
    axs[13].invert_yaxis()
    axs[13].set_xlim(-0.05,0.25)
    
    axs[14].plot(br_n,depth, c='brown',lw=0.5, label='Bit')
    axs[14].plot(rr_n,depth, c='black',lw=0.5, label='Ring')
    axs[14].set_title('Noise\nBit\nResistivity\n(ohm.m)', fontsize=10)
    axs[14].legend(fontsize=8)
    axs[14].invert_yaxis()
    axs[14].set_xlim(-0.05,0.25)

    axs[15].axis('off')

    if plot_vp.lower() == 'yes':
        axs[16].plot(vp, depth_vp, c='blue', lw=0.5)
        axs[16].set_title('VP\nUnits ???', fontsize=10)
    axs[16].invert_yaxis()

    fig.suptitle(site_name, fontsize=14)
    
    fig.savefig('../Results/' + site_name + '_data.pdf')
    
    print("\nData plot saved at ../Results/{site_name}_data.pdf\n")

if __name__ == "__main__":
    
    print("---Preparing Data for Vp Prediction---\n\n")
    
    main()