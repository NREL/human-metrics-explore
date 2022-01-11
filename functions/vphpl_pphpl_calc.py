import numpy as np
import matplotlib.patches as mpatches


#New PPHPL Calculation using formula from paper
def pphpl_by_mode(vphpl,mpw,occ):
    pphpl = vphpl*mpw*occ
    return pphpl 



def vphpl_pphpl_calc(variables):

    ##updated by swaroop to account for list of following distance
    #unit = metre
    tl_wb = [i+j for i,j in zip(variables["fd"]["wb"],variables["lm"]["wb"])]
    tl_pvt = [i+j for i,j in zip(variables["fd"]["pvt"],variables["lm"]["pvt"])]
    tl_bus = [i+j for i,j in zip(variables["fd"]["bus"],variables["lm"]["bus"])]

    ##updated by swaroop to account for list of following distance
    #VPHPL
    vphpl_wb = 0
    vphpl_pvt = [i/j *1000 for i,j in zip(variables["speed"]["pvt"],tl_pvt)]
    vphpl_bus = [i/j * 1000 for i,j in zip(variables["speed"]["bus"],tl_bus)]
    vphpl_combined = vphpl_wb * variables["ms"]["wb"] + [i*j + k*l for i,j,k,l in zip(vphpl_pvt, variables["ms"]["pvt"],vphpl_bus,variables["ms"]["bus"])]
 #############################################################################################################################
    #PPHPL Calculation
    #Assume occupancy for walk/bike is 1
    pphpl_wb = np.array([i/j * 1000 * variables['mpw']['wb'] * 1  for i,j in zip(variables["speed"]["wb"],tl_wb)]).flatten().tolist()
    pphpl_pvt = pphpl_by_mode(vphpl_pvt,variables['mpw']['pvt'],variables["occ"]["pvt"]).flatten().tolist()
    pphpl_bus = pphpl_by_mode(vphpl_bus,variables['mpw']['bus'],variables["occ"]["bus"]).flatten().tolist()
    pphpl_combined = ((pphpl_wb * variables["ms"]["wb"]) + (pphpl_bus*variables["ms"]["bus"]) + (pphpl_pvt*variables["ms"]["pvt"])).flatten().tolist()
   

    #PPHPL2 Calculation
    #PPHPL2 = PPHPL1 * (Trip Distance/20 km) where 20 km is ~max travel distance in dataset
    road_len=20 #km
    pphpl2_wb = (pphpl_wb*(road_len/variables["pmt"]['wb'])).flatten().tolist()
    pphpl2_pvt = (pphpl_pvt*(variables["pmt"]['pvt']/road_len)).flatten().tolist()
    pphpl2_bus = (pphpl_bus*(variables["pmt"]['bus']/road_len)).flatten().tolist()
    pphpl2_combined = ((pphpl2_wb * variables["ms"]["wb"]) + (pphpl2_bus*variables["ms"]["bus"]) + (pphpl2_pvt*variables["ms"]["pvt"])).flatten().tolist()
    
    
 #############################################################################################################################   #PEIT Calculations 
    def peit1_calc(ms, avo, ee):
        return ms * (1/avo) * (1/ee)
    
    #Calculate each individually and then sum to get PEIT1
    peit_pvt = peit1_calc(variables["ms"]["pvt"],variables["occ"]["pvt"],variables["FE"]["pvt"]).flatten()
    peit_bus = peit1_calc(variables["ms"]["bus"],variables["occ"]["bus"],variables["FE"]["bus"]).flatten()
    #wb FE roughly drawn from https://dothemath.ucsd.edu/2011/11/mpg-of-a-human/ (~250 mpg = ~110 kpl)
    peit_wb = peit1_calc(variables["ms"]["wb"],1,110).flatten()
    peit_vals = (peit_pvt+peit_bus+peit_wb).flatten()

    #Calculate each individually and then sum and multiply by trip distance to get PEIT2
    peit2_pvt = variables["pmt"]["pvt"]*peit_pvt
    peit2_bus = variables["pmt"]["bus"]*peit_bus
    #wb FE roughly drawn from https://dothemath.ucsd.edu/2011/11/mpg-of-a-human/ (~250 mpg = ~110 kpl)
    peit2_wb = variables["pmt"]["wb"]*peit_wb
    peit2_vals = (peit2_pvt+peit2_bus+peit2_wb)
    


    return {"vphpl": {"pvt": vphpl_pvt, "bus": vphpl_bus, "wb": vphpl_wb, "combined": vphpl_combined}, 
    "pphpl1": {"pvt": pphpl_pvt, "bus": pphpl_bus, "wb": pphpl_wb, "combined": pphpl_combined},
    "pphpl2": {"pvt": pphpl2_pvt, "bus": pphpl2_bus, "wb": pphpl2_wb, "combined": pphpl2_combined},
    'peit1': {"pvt": peit_pvt, "bus": peit_bus, "wb": peit_wb, "combined": peit_vals},  
    'peit2': {"pvt": peit2_pvt, "bus": peit2_bus, "wb": peit2_wb, "combined": peit2_vals},
    'tl':{"pvt":tl_pvt,"bus":tl_bus,"wb":tl_wb}
           }#, 
    #"pphpl_1": {"pvt": pphpl_1_pvt, "bus": pphpl_1_bus, "wb": pphpl_1_wb, "combined": pphpl_1_combined}} )

