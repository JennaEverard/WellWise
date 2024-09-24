#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

GraphWell

Generate pdf plots of well logging data

Copyright 2024 Jenna Everard

"""

import numpy as np

import plotly.io as pio
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from Helpers.read_data import read_gr_file, read_res_file, read_vp_file, read_cal_file, read_por_file, read_den_file

def graphwell():
    
    print("---GraphWell---\n\n")
    
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
        
        print("\nDo you have gamma ray data?\n")
        plot_gr = input("Enter YES or NO: ")
        valid_answer = False
        while not valid_answer:
            if plot_gr.lower() == 'yes' or plot_gr.lower() == 'no':
                valid_answer = True
                if plot_gr.lower() == 'yes':
                    print("\nReading Gamma Ray data files...\n")
                    depth_gr, gr = read_gr_file()
            else:
                plot_gr = input("Not a valid input, please try again: ")
        
        
        print("\nDo you have resistivity data?\n")
        plot_res = input("Enter YES or NO: ")
        valid_answer = False
        while not valid_answer:
            if plot_res.lower() == 'yes' or plot_res.lower() == 'no':
                valid_answer = True
                if plot_res.lower() == 'yes':
                    print("\nReading Resistivity data files...\n")
                    depth_res, deep_res, medium_res, shallow_res, ring_res, bit_res = read_res_file()
            else:
                plot_res = input("Not a valid input, please try again: ")
        
        
        print("\nDo you have Vp data?\n")
        plot_vp = input("Enter YES or NO: ")
        valid_answer = False
        while not valid_answer:
            if plot_vp.lower() == 'yes' or plot_vp.lower() == 'no':
                valid_answer = True
                if plot_vp.lower() == 'yes':
                    print("\nReading Vp data files...\n")
                    depth_vp, vp = read_vp_file()
            else:
                plot_vp = input("Not a valid input, please try again: ")
        
        
        print("\nDo you have density data?\n")
        plot_den = input("Enter YES or NO: ")
        valid_answer = False
        while not valid_answer:
            if plot_den.lower() == 'yes' or plot_den.lower() == 'no':
                valid_answer = True
                if plot_den.lower() == 'yes':
                    print("\nReading Density data files...\n")
                    depth_den, den = read_den_file()
            else:
                plot_den = input("Not a valid input, please try again: ")
        
        
        print("\nDo you have porosity data?\n")
        plot_por = input("Enter YES or NO: ")
        valid_answer = False
        while not valid_answer:
            if plot_por.lower() == 'yes' or plot_por.lower() == 'no':
                valid_answer = True
                if plot_por.lower() == 'yes':
                    print("\nReading Porosity data files...\n")
                    depth_por, por = read_por_file()
            else:
                plot_por = input("Not a valid input, please try again: ")
        
        
        print("\nDo you have caliper data?\n")
        plot_cal = input("Enter YES or NO: ")
        valid_answer = False
        while not valid_answer:
            if plot_cal.lower() == 'yes' or plot_cal.lower() == 'no':
                valid_answer = True
                if plot_cal.lower() == 'yes':
                    print("\nReading Caliper data files...\n")
                    depth_cal, cal = read_cal_file()
            else:
                plot_cal = input("Not a valid input, please try again: ")
        
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
        
        print("\nPlotting data...\n")    
        
        total_col = 0
        col_names = []

        if plot_cal.lower() == 'yes':
            total_col += 1
            col_names.append('Caliper')
        if plot_gr.lower() == 'yes':
            total_col += 1
            col_names.append('Gamma Ray')
        if plot_res.lower() == 'yes':
            total_col += 2
            col_names.append('Button\nResistivity')
            col_names.append('Other\nResistivity')
        if plot_por.lower() == 'yes':
            total_col += 1
            col_names.append('Porosity')
        if plot_den.lower() == 'yes':
            total_col += 1
            col_names.append('Density')
        if plot_vp.lower() == 'yes':
            total_col += 1
            col_names.append('Vp')
                
        fig = make_subplots(rows = 1, cols = total_col, 
                            shared_yaxes = True,
                            subplot_titles = col_names)
        
        current_col = 1
        threshhold = -500
        
        if plot_cal.lower() == 'yes':
            
            filter_i = cal >= threshhold
            filtered_cal_depth = depth_cal[filter_i]
            filtered_cal = cal[filter_i]
            
            fig.add_trace(go.Scatter(x=filtered_cal, y=filtered_cal_depth, 
                                     mode='lines', name='Caliper', 
                                     line=dict(color='sienna', width=0.5)), 
                          row=1, col=current_col)
            current_col += 1
            
        if plot_gr.lower() == 'yes':
            
            filter_i = gr >= threshhold
            filtered_gr_depth = depth_gr[filter_i]
            filtered_gr = gr[filter_i]
            
            fig.add_trace(go.Scatter(x=filtered_gr, y=filtered_gr_depth, 
                                     mode='lines', name='Gamma Ray', 
                                     line=dict(color='darkgreen', width=0.5)), 
                          row=1, col=current_col)
            current_col += 1
        
        if plot_res.lower() == 'yes':
            
            no_shallow = not np.any(shallow_res)
            no_medium = not np.any(medium_res)
            no_deep = not np.any(deep_res)
            no_bit = not np.any(bit_res)
            no_ring = not np.any(ring_res)
            
            if not no_deep:
                filter_i = deep_res >= threshhold
                filtered_deep_depth = depth_res[filter_i]
                filtered_deep = deep_res[filter_i]
                fig.add_trace(go.Scatter(x=filtered_deep, y=filtered_deep_depth, 
                                         mode='lines', name='Deep Resistivity', 
                                         line=dict(color='steelblue', width=0.5)), 
                              row=1, col=current_col)
                
            if not no_medium:
                filter_i = medium_res >= threshhold
                filtered_medium_depth = depth_res[filter_i]
                filtered_medium = medium_res[filter_i]
                fig.add_trace(go.Scatter(x=filtered_medium, y=filtered_medium_depth, 
                                         mode='lines', name='Medium Resistivity', 
                                         line=dict(color='cyan', width=0.5)), 
                              row=1, col=current_col)
                
            if not no_shallow:
                filter_i = shallow_res >= threshhold
                filtered_shallow_depth = depth_res[filter_i]
                filtered_shallow = shallow_res[filter_i]
                fig.add_trace(go.Scatter(x=filtered_shallow, y=filtered_shallow_depth, 
                                         mode='lines', name='Shallow Resistivity', 
                                         line=dict(color='lime', width=0.5)), 
                              row=1, col=current_col)
            
            current_col += 1
            
            if not no_bit:
                filter_i = bit_res >= threshhold
                filtered_bit_depth = depth_res[filter_i]
                filtered_bit = bit_res[filter_i]
                fig.add_trace(go.Scatter(x=filtered_bit, y=filtered_bit_depth, 
                                         mode='lines', name='Bit Resistivity', 
                                         line=dict(color='peru', width=0.5)), 
                              row=1, col=current_col)
            if not no_ring:
                filter_i = ring_res >= threshhold
                filtered_ring_depth = depth_res[filter_i]
                filtered_ring = ring_res[filter_i]
                fig.add_trace(go.Scatter(x=filtered_ring, y=filtered_ring_depth, 
                                         mode='lines', name='Ring Resistivity', 
                                         line=dict(color='black', width=0.5)), 
                              row=1, col=current_col)
            current_col += 1
            
        if plot_por.lower() == 'yes':
            filter_i = por >= threshhold
            filtered_por_depth = depth_por[filter_i]
            filtered_por = por[filter_i]
            
            fig.add_trace(go.Scatter(x=filtered_por, y=filtered_por_depth, 
                                     mode='lines', name='Porosity', 
                                     line=dict(color='palevioletred', width=0.5)), 
                          row=1, col=current_col)
            current_col += 1
            
        if plot_den.lower() == 'yes':
            filter_i = den >= threshhold
            filtered_den_depth = depth_den[filter_i]
            filtered_den = den[filter_i]
            
            fig.add_trace(go.Scatter(x=filtered_den, y=filtered_den_depth, 
                                     mode='lines', name='Density', 
                                     line=dict(color='mediumorchid', width=0.5)), 
                          row=1, col=current_col)
            current_col += 1
            
        if plot_vp.lower() == 'yes':
            filter_i = vp >= threshhold
            filtered_vp_depth = depth_vp[filter_i]
            filtered_vp = vp[filter_i]
            
            fig.add_trace(go.Scatter(x=filtered_vp, y=filtered_vp_depth, 
                                     mode='lines', name='Vp', 
                                     line=dict(color='lightsalmon', width=0.5)), 
                          row=1, col=current_col)
            current_col += 1
            
        fig.update_yaxes(autorange="reversed")
        
        fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)
        fig.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)

        fig.update_layout(
            title= site_name,
            title_font=dict(size=14),
            legend = dict(font=dict(size=8),
                          itemsizing='constant',
                          orientation = 'h',
                          xanchor = 'center',
                          x = 0.5),
            plot_bgcolor='white',
            width=1200,
            height=1800
        )
        
        fig.write_image('Results/' + site_name + '_data.pdf')
        fig.write_html('Results/' + site_name + '_interactive.html')
        
        print("\nData plot saved at Results/{site_name}_data.pdf\n")
        print("\nInteractive Data plot saved at Results/{site_name}_interactive.html\n")

        
    elif data_type == 2:
        # read dlis files - NOT YET IMPLEMENTED
        print("\nSupport for DLIS files coming soon. Terminating program now.\n")
        return
    else:
        # read las files - NOT YET IMPLEMENTED
        print("\nSupport for LAS files coming soon. Termining program now.\n")
        return
    
    return