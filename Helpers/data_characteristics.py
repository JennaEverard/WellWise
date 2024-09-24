#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Data Characteristics

Helper functions to calculate various characteristics of well logging data

Copyright 2024 Jenna Everard

"""

import numpy as np

def calc_noise(gr, dr, mr, sr, rr, br, window):
    return (cn_helper(len(gr),gr,window), cn_helper(len(dr),dr,window),
            cn_helper(len(mr),mr,window), cn_helper(len(sr),sr,window),
            cn_helper(len(rr),rr,window), cn_helper(len(br),br,window))
        
def cn_helper(len_arr, arr, window):
    noise = []
    for i in range(0, len_arr):
        if i < (window / 2):
            sum_diffs = np.sum([np.abs(arr[j+1]-arr[j]) for j in range(0,window)])
        elif len_arr - i <= (window / 2):
            sum_diffs = np.sum([np.abs(arr[j+1]-arr[j]) for j in range(len_arr-window,len_arr-1)])
        else:
            sum_diffs = np.sum([np.abs(arr[j+1]-arr[j]) for j in range(i-int(window/2),i+int(window/2))])
        noise.append(sum_diffs / window)
    return noise

def calc_window_deriv(gr, dr, mr, sr, rr, br, window): 
    return (get_difference(gr,window), get_difference(dr,window),
            get_difference(mr,window), get_difference(sr,window),
            get_difference(rr,window), get_difference(br,window))

def get_difference(arr, window_size):
    arr_deriv = []
    for i in range(0,len(arr)):
        if i < len(arr) - window_size:
            arr_deriv.append(arr[i + window_size] - arr[i])
        else:
            arr_deriv.append(arr[len(arr)-1] - arr[i])
    return arr_deriv