#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Depth

Helper functions to handle varying depth scales between data

Copyright 2024 Jenna Everard

"""

import math
import numpy as np

def normalize_depth(d1, d2, d3=None):
    
    min_d1 = min(d1)
    min_d2 = min(d2)
    if d3 is not None:
        min_d3 = min(d3)
    else:
        min_d3 = -9999
    
    min_depth = math.ceil(max(min_d1,min_d2,min_d3))
    if min_depth < 0:
        min_depth = 0
    
    max_d1 = max(d1)
    max_d2 = max(d2)
    if d3 is not None:
        max_d3 = max(d3)
    else:
        max_d3 = 9999
    
    max_depth = math.floor(min(max_d1, max_d2, max_d3))
    
    depth = np.arange(min_depth, max_depth + 1, 0.03)
    return depth

def interpolate_data(depth, depth_gr, depth_res, gr, dr, mr, sr, rr, br):
    
    gr_n = []
    dr_n = []
    mr_n = []
    sr_n = []
    rr_n = []
    br_n = []
    
    for i in range(0, len(depth)):
        cur_depth = depth[i]
        
        depth_gr_i = np.argmin(np.abs(depth_gr - cur_depth))
        depth_res_i = np.argmin(np.abs(depth_res - cur_depth))
        
        gr_n.append(gr[depth_gr_i])
        
        dr_n.append(dr[depth_res_i])
        mr_n.append(mr[depth_res_i])
        sr_n.append(sr[depth_res_i])
        rr_n.append(rr[depth_res_i])
        br_n.append(br[depth_res_i])
    
    gr_n = np.array(gr_n)
    dr_n = np.array(dr_n)
    mr_n = np.array(mr_n)
    sr_n = np.array(sr_n)
    rr_n = np.array(rr_n)
    br_n = np.array(br_n)
    
    return gr_n,dr_n,mr_n,sr_n,rr_n,br_n

