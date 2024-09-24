#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Read Data

Helper functions to read well logging data files and return data arrays

Copyright 2024 Jenna Everard

"""

import numpy as np

def read_cal_file():
    
    cal_file_path = input("\nPath to Caliper file: ")
    
    depth_cal = []
    cal = []
    
    valid_cal_file = False
    while not valid_cal_file:
        try:
            file_type = 1
            with open(cal_file_path, 'r') as file:
                for line in file:
                    if line.startswith('DEPTH'):
                        break
                next(file)
                for line in file:
                    values = line.split(',')
                    if len(values) >= 2:
                        depth_cal.append(float(values[0]))
                        cal.append(float(values[1]))
            valid_cal_file = True
        except FileNotFoundError:
            print("***ERROR*** File Not Found")
            cal_file_path = input("\nPath to Caliper file: ")
        except ValueError:
            print("***ERROR*** Nonnumerical data in file")
            cal_file_path = input("\nPath to Caliper file: ")
        except Exception as e:
            print("***ERROR*** Unknown")
            cal_file_path = input("\nPath to Caliper file: ")
     
    depth_cal = np.array(depth_cal)
    cal = np.array(cal)
    
    return depth_cal, cal

def read_por_file():
    
    por_file_path = input("\nPath to Porosity file: ")
    
    depth_por = []
    por = []
    
    valid_por_file = False
    while not valid_por_file:
        try:
            file_type = 1
            with open(por_file_path, 'r') as file:
                for line in file:
                    if line.startswith('DEPTH'):
                        break
                next(file)
                for line in file:
                    values = line.split(',')
                    if len(values) >= 2:
                        depth_por.append(float(values[0]))
                        por.append(float(values[1]))
            valid_por_file = True
        except FileNotFoundError:
            print("***ERROR*** File Not Found")
            por_file_path = input("\nPath to Porosity file: ")
        except ValueError:
            print("***ERROR*** Nonnumerical data in file")
            por_file_path = input("\nPath to Porosity file: ")
        except Exception as e:
            print("***ERROR*** Unknown")
            por_file_path = input("\nPath to Porosity file: ")
     
    depth_por = np.array(depth_por)
    por = np.array(por)
    
    return depth_por, por

def read_den_file():

    den_file_path = input("\nPath to Density file: ")
    
    depth_den = []
    den = []
    
    valid_den_file = False
    while not valid_den_file:
        try:
            file_type = 1
            with open(den_file_path, 'r') as file:
                for line in file:
                    if line.startswith('DEPTH'):
                        break
                next(file)
                for line in file:
                    values = line.split(',')
                    if len(values) >= 2:
                        depth_den.append(float(values[0]))
                        den.append(float(values[1]))
            valid_den_file = True
        except FileNotFoundError:
            print("***ERROR*** File Not Found")
            den_file_path = input("\nPath to Density file: ")
        except ValueError:
            print("***ERROR*** Nonnumerical data in file")
            den_file_path = input("\nPath to Density file: ")
        except Exception as e:
            print("***ERROR*** Unknown")
            den_file_path = input("\nPath to Density file: ")
     
    depth_den = np.array(depth_den)
    den = np.array(den)
    
    return depth_den, den

def read_vp_file():
    
    vp_file_path = input("\nPath to Vp file: ")
    
    depth_vp = []
    vp = []
    
    valid_vp_file = False
    while not valid_vp_file:
        try:
            file_type = 1
            with open(vp_file_path, 'r') as file:
                for line in file:
                    if line.startswith('DEPTH'):
                        
                        headers = line.strip().split(',')
                        
                        if len(headers) > 3:
                            if len(headers) == 4:
                                file_types = 3
                            else:
                                file_type = 2
                        break
                next(file)
                for line in file:
                    values = line.split(',')
                    if len(values) >= 2:
                        depth_vp.append(float(values[0]))
                        if file_type == 1 or file_type == 3:
                            vp.append( (1000/float(values[2])) * 0.3048 )
                        else:
                            vp.append( (1000/float(values[3])) * 0.3048 )
            valid_vp_file = True
        except FileNotFoundError:
            print("***ERROR*** File Not Found")
            vp_file_path = input("\nPath to Vp file: ")
        except ValueError:
            print("***ERROR*** Nonnumerical data in file")
            vp_file_path = input("\nPath to Vp file: ")
        except Exception as e:
            print("***ERROR*** Unknown")
            vp_file_path = input("\nPath to Vp file: ")
     
    depth_vp = np.array(depth_vp)
    vp = np.array(vp)
    
    return depth_vp, vp

def read_gr_file():
    
    gr_file_path = input("\nPath to gamma ray file: ")
    
    depth_gr = []
    gr = []
    
    valid_gr_file = False
    while not valid_gr_file:
        try:
            with open(gr_file_path, 'r') as file:
                for line in file:
                    if line.startswith('DEPTH'):
                        break
                next(file)
                for line in file:
                    values = line.strip().split(',')
                    if len(values) >= 2:
                        depth_gr.append(float(values[0]))
                        gr.append(float(values[1]))
            valid_gr_file = True
        except FileNotFoundError:
            print("***ERROR*** File Not Found")
            gr_file_path = input("\nPath to gamma ray file: ")
        except ValueError:
            print("***ERROR*** Nonnumerical data in file")
            gr_file_path = input("\nPath to gamma ray file: ")
        except Exception as e:
            print("***ERROR*** Unknown")
            gr_file_path = input("\nPath to gamma ray file: ")
    
    depth_gr = np.array(depth_gr)
    gr = np.array(gr)
    
    return depth_gr, gr
 
def read_res_file():
    
    res_file_path = input("\nPath to button/bit/ring resistivity file: ")
    
    depth_res = []
    deep_res = []
    medium_res = []
    shallow_res = []
    bit_res = []
    ring_res = []
    
    valid_res_file = False
    while not valid_res_file:
        try:
            file_type = 1
            with open(res_file_path, 'r') as file:
                for line in file:
                    if line.startswith('DEPTH'):
                        
                        headers = line.strip().split(',')
                        if headers[1].startswith('BD'):
                            if len(headers) == 6:
                                file_type = 1
                            else:
                                if headers[2].startswith('BM'):
                                    file_type = 2
                                else:
                                    file_type = 5
                        elif headers[1].startswith('BS'):
                            file_type = 3
                        else:
                            file_type = 4
                        
                        break
                next(file)
                
                for line in file:
                    
                    values = line.strip().split(',')
                    
                    if len(values) >= 2:
                        depth_res.append(float(values[0]))
                        if file_type == 1:
                            deep_res.append(float(values[1]))
                            medium_res.append(float(values[2]))
                            shallow_res.append(float(values[3]))
                            ring_res.append(float(values[4]))
                            bit_res.append(float(values[5]))
                        elif file_type == 2:
                            deep_res.append(float(values[1]))
                            medium_res.append(float(values[2]))
                            shallow_res.append(float(values[3]))
                            ring_res.append(float(values[4]))
                            bit_res = None
                        elif file_type == 3:
                            shallow_res.append(float(values[1]))
                            medium_res.append(float(values[2]))
                            deep_res.append(float(values[3]))
                            ring_res.append(float(values[4]))
                            bit_res.append(float(values[5]))
                        elif file_type == 4:
                            deep_res.append(float(values[1]))
                            bit_res.append(float(values[2]))
                            medium_res.append(float(values[3]))
                            shallow_res.append(float(values[4]))
                            ring_res = None
                        else:
                            deep_res.append(float(values[1]))
                            bit_res.append(float(values[2]))
                            shallow_res.append(float(values[3]))
                            ring_res.append(float(values[4]))
                            medium_res = None
            valid_res_file = True
        except FileNotFoundError:
            print("***ERROR*** File Not Found")
            gr_file_path = input("\nPath to resistivity file: ")
        except ValueError:
            print("***ERROR*** Nonnumerical data in file")
            gr_file_path = input("\nPath to resistivity file: ")
        except Exception as e:
            print("***ERROR*** Unknown")
            gr_file_path = input("\nPath to resistivity file: ")
    
    deep_res = np.array(deep_res)
    if bit_res is None:
        bit_res = np.zeros(len(deep_res))
    else:
        bit_res = np.array(bit_res)
    if ring_res is None:
        ring_res = np.zeros(len(deep_res))
    else:
        ring_res = np.array(ring_res)
    if medium_res is None:
        medium_res = np.zeros(len(deep_res))
    else:
        medium_res = np.array(medium_res)
    shallow_res = np.array(shallow_res)
    depth_res = np.array(depth_res)
    
    return depth_res, deep_res, medium_res, shallow_res, ring_res, bit_res
    