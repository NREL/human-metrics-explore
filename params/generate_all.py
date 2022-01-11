import numpy as np
import matplotlib.patches as mpatches
import params.Occupancy.generate_pvt_occ as pvt_occ
import params.Occupancy.generate_bus_occ as bus_occ

import params.MS.generate_bus_ms as bus_ms
import params.MS.generate_pvt_ms as pvt_ms
import params.MS.generate_wb_ms as wb_ms

import params.PMT.generate_bus_pmt as bus_pmt
import params.PMT.generate_pvt_pmt as pvt_pmt
import params.PMT.generate_wb_pmt as wb_pmt

from params.speed.generate_bus_speed import generate_bus_speed
from params.speed.generate_pvt_speed import generate_pvt_speed
from params.speed.generate_wb_speed import generate_wb_speed

from params.Follow_Dist.generate_bus_fd import generate_bus_fd
from params.Follow_Dist.generate_pvt_fd import generate_pvt_fd
from params.Follow_Dist.generate_wb_fd import generate_wb_fd

from params.lm.generate_bus_lm import generate_bus_lm
from params.lm.generate_pvt_lm import generate_pvt_lm
from params.lm.generate_wb_lm import generate_wb_lm

import params.FE.generate as FE

def generate_all():
    
    occ_pvt_gen = pvt_occ.Generator("params/Occupancy/PvtOccupancyFreq.csv")
    occ_bus_gen = bus_occ.Generator("params/Occupancy/BusOccFreq.csv")
    
    occ_pvt_vals = occ_pvt_gen.generate_pvt_occ(100)
    occ_bus_vals = occ_bus_gen.generate_bus_occ(100)
    
    ms_pvt_gen = pvt_ms.Generator("params/MS/PVT_MS_freq.csv")
    ms_bus_gen = bus_ms.Generator("params/MS/BUS_MS_freq.csv")
    ms_wb_gen = wb_ms.Generator("params/MS/WB_MS_freq.csv")

    #Ensure these sum to 1
    ms_bus_vals = ms_bus_gen.generate_bus_ms(100).flatten()
    ms_wb_vals = ms_wb_gen.generate_wb_ms(100).flatten()
    ms_pvt_vals = 1 - (ms_bus_vals + ms_wb_vals).flatten() #ms_pvt_gen.generate_pvt_ms(100)

    pmt_pvt_gen = pvt_pmt.Generator("params/PMT/PVT_PMT_freq.csv")
    pmt_bus_gen = bus_pmt.Generator("params/PMT/BUS_PMT_freq.csv")
    pmt_wb_gen = wb_pmt.Generator("params/PMT/WB_PMT_freq.csv")

    #Generated in miles so convert to km by multiplying by 1.6
    pmt_bus_vals = pmt_bus_gen.generate_bus_pmt(100).flatten()*1.6
    pmt_pvt_vals = pmt_pvt_gen.generate_pvt_pmt(100).flatten()*1.6
    pmt_wb_vals = pmt_wb_gen.generate_wb_pmt(100).flatten()*1.6

    #unit = km/hr
    #Don't need to flatten because data structure is generated from random uniform distribution rather than randomly selecting from data
    speed_pvt_vals = generate_pvt_speed(100) 
    speed_bus_vals = generate_bus_speed(100)
    speed_wb_vals = generate_wb_speed(100)

    fd_pvt_vals = generate_pvt_fd(speed_pvt_vals)
    fd_bus_vals = generate_bus_fd(speed_bus_vals)
    fd_wb_vals = generate_wb_fd(speed_wb_vals)
    
    FE_pvt_gen = FE.Generator("params/FE/pvt_FE.csv")
    FE_bus_gen = FE.Generator("params/FE/bus_FE.csv")

    FE_pvt_vals = FE_pvt_gen.generate(100).flatten()
    FE_bus_vals = FE_bus_gen.generate(100).flatten()
    
    #length of mode
    #unit=meter
    lm_pvt_vals = np.array(generate_pvt_lm(100))
    lm_bus_vals = np.array(generate_bus_lm(100))
    lm_wb_vals = np.array(generate_wb_lm(100))
    
    ###modes per width
    mpw_wb = 2.5
    mpw_pvt = 1
    mpw_bus = 1
 
    return {"occ": {"pvt": occ_pvt_vals, "bus": occ_bus_vals}, ##occ =1 for walking and biking
            "ms": {"pvt": ms_pvt_vals, "bus": ms_bus_vals, "wb": ms_wb_vals}, ##mode share
            "pmt": {"pvt": pmt_pvt_vals, "bus": pmt_bus_vals, "wb": pmt_wb_vals}, ##person miles travelled
            "speed":{"pvt": speed_pvt_vals, "bus": speed_bus_vals, "wb": speed_wb_vals}, 
            "fd": {"pvt": fd_pvt_vals, "bus": fd_bus_vals, "wb": fd_wb_vals}, ##following distance
            "FE": {"pvt": FE_pvt_vals,"bus": FE_bus_vals},
            "lm": {"pvt":lm_pvt_vals,"bus":lm_bus_vals,"wb":lm_wb_vals}, #length of mode
            "mpw":{"pvt":mpw_pvt,"bus":mpw_bus,"wb":mpw_wb}
           } 
