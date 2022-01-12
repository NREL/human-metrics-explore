import numpy as np
import matplotlib.pyplot as plt

from params.generate_all import generate_all
from functions.vphpl_pphpl_calc import vphpl_pphpl_calc

# Read the parameters and generate baseline values
params = generate_all()
results = vphpl_pphpl_calc(params)

#########Std dev varying functions#########

#Given binary inputs for ms, occ, fe, calculate the std dev version of PEIT1
def calculate_peit_var(ms_var, occ_var, FE_var, calc_fn):
    ms_bus_mod = stddev_gen(params["ms"]["bus"], ms_var)
    ms_wb_mod = stddev_gen(params["ms"]["wb"], ms_var)
    ms_pvt_mod = 1 - (ms_bus_mod + ms_wb_mod)

    pvt_peit_std=calc_fn(ms_pvt_mod,stddev_gen(params["occ"]["pvt"], occ_var),stddev_gen(params["FE"]["pvt"], FE_var))
    bus_peit_std=calc_fn(ms_bus_mod,stddev_gen(params["occ"]["bus"], occ_var),stddev_gen(params["FE"]["bus"], FE_var))
    wb_peit_std=calc_fn(ms_wb_mod,1,110)
    peit_vals_std = pvt_peit_std+bus_peit_std+wb_peit_std
    return peit_vals_std

#Given binary inputs for ms, occ, fe, pmt calculate the std dev version of PEIT2
#Input of 1 means increase that parameter value by a standard deviation of 1
def calculate_peit2_var(ms_var, occ_var, FE_var, pmt_var):
    ms_bus_mod = stddev_gen(params["ms"]["bus"], ms_var)
    ms_wb_mod = stddev_gen(params["ms"]["wb"], ms_var)
    ms_pvt_mod = 1 - (ms_bus_mod + ms_wb_mod)

    pvt_peit_std=peit1_calc(ms_pvt_mod,stddev_gen(params["occ"]["pvt"], occ_var),stddev_gen(params["FE"]["pvt"], FE_var))*stddev_gen(params["pmt"]["pvt"],pmt_var)
    bus_peit_std=peit1_calc(ms_bus_mod,stddev_gen(params["occ"]["bus"], occ_var),stddev_gen(params["FE"]["bus"], FE_var))*stddev_gen(params["pmt"]["bus"],pmt_var)
    wb_peit_std=peit1_calc(ms_wb_mod,1,110)*stddev_gen(params["pmt"]["wb"],pmt_var)
    peit_vals_std = pvt_peit_std+bus_peit_std+wb_peit_std
    return peit_vals_std

#Given binary inputs for ms, occ, fe, calculate the std dev version of PPHPL
#-1 for pmt so it is an improvement
def calculate_pphpl_var(occ, ms):
    ms_bus = stddev_gen(params["ms"]["bus"], ms)
    ms_wb = stddev_gen(params["ms"]["wb"], ms)
    ms_pvt = 1 - (ms_bus + ms_wb)

    pphpl_pvt_std=pphpl_by_mode(results["vphpl"]["pvt"],params['mpw']['pvt'],stddev_gen(params["occ"]["pvt"],occ)).tolist()
    pphpl_bus_std=pphpl_by_mode(results["vphpl"]["bus"],params['mpw']['bus'],stddev_gen(params["occ"]["bus"],occ)).tolist()
    pphpl_wb_std=np.array([i/j * 1000 * params['mpw']['wb'] * 1  for i,j in zip(params["speed"]["wb"],results['tl']['wb'])]).flatten().tolist()
    pphpl_combined_std = ((pphpl_pvt_std * ms_pvt) + (pphpl_bus_std*ms_bus) + (pphpl_wb_std*ms_wb)).flatten().tolist()
     
    return pphpl_combined_std

def calculate_pphpl2_var(occ, ms, pmt):
    road_len = 20 #km
    ms_bus = stddev_gen(params["ms"]["bus"], ms)
    ms_wb = stddev_gen(params["ms"]["wb"], ms)
    ms_pvt = 1 - (ms_bus + ms_wb)

    pphpl_pvt_std=pphpl_by_mode(results["vphpl"]["pvt"],params['mpw']['pvt'],stddev_gen(params["occ"]["pvt"],occ)).tolist()*stddev_gen(road_len/params['pmt']['pvt'],pmt)
    pphpl_bus_std=pphpl_by_mode(results["vphpl"]["bus"],params['mpw']['bus'],stddev_gen(params["occ"]["bus"],occ)).tolist()*stddev_gen(road_len/params['pmt']['bus'],pmt)
    pphpl_bus_std = [0 if i < 0 else i for i in pphpl_bus_std] #Ensure negative values are zeroed
    pphpl_wb_std=np.array([i/j * 1000 * params['mpw']['wb'] * 1  for i,j in zip(params["speed"]["wb"],results['tl']['wb'])]).flatten().tolist()*stddev_gen(road_len/params['pmt']['wb'],pmt)
    pphpl_combined_std = ((pphpl_pvt_std * ms_pvt) + (pphpl_bus_std*ms_bus) + (pphpl_wb_std*ms_wb)).flatten().tolist()
    return pphpl_combined_std

# Default parameter does not change anything
# 1 adds one standard deviation
# -1 removes one standard deviation
def stddev_gen(vals,stddev_ratio=1):
    stddev = np.std(vals)
    new_vals = vals + stddev_ratio * stddev
    new_vals=new_vals.flatten()
    return new_vals


def add_label(violin, label):
    color = violin["bodies"][0].get_facecolor().flatten()
    labels.append((mpatches.Patch(color=color), label))

#CDFs of modes all in a single plot
#Colors MUST be passed in as a list even if there's only one color
def cdf_plot(data, labels, xaxis_title = "",colors = ['blue','orange','green']):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    if (isinstance(data[0],np.ndarray) or isinstance(data[0],list)): #If we pass in a list of datasets
        for idx in range(0,len(data)):
            if labels[idx]=="Baseline":
                linewidth=3
                linestyle="--"
            else:
                linewidth=2
                linestyle="-"
            print("About to print data at index %d with label %s " % (idx, labels[idx]))
            values, base = np.histogram(data[idx], bins=41)
            # print("About to print %s" % data)
            base[-1]= max([max(x) for x in data])
            cumulative = np.cumsum(values)
            cumulative = np.append(cumulative,100)
            
            ######
            median=np.percentile(data[idx], 50) #Using 47th percentile to make lines intersect with trends visually- unsure why 50th percentile doesn't lie on curve
            plt.axhline(y=.5, xmin=0, xmax=1, color='red',linestyle=":",linewidth=1)
            plt.axvline(x=median, ymin=0, ymax=0.5,color=colors[idx],linestyle=":",linewidth=2)
            #plt.text(median, idx/20, round(median,3), color=colors[idx], fontsize=14)
            print("summary stats: mean %.6f, median: %.6f" % (np.mean(data[idx]), median))
            ######
            
            plt.plot(base, cumulative/100, linewidth=linewidth,linestyle=linestyle,label = labels[idx],c=colors[idx])
            plt.fill_between(base, cumulative/100, 0, alpha=0.05,color=colors[idx])
    else: #There is only one dataset being passed in
        values, base = np.histogram(data, bins=41)
        base[-1]= max(data)
        cumulative = np.cumsum(values)
        cumulative = np.append(cumulative,100)
        plt.plot(base, cumulative/100, linewidth=2,label = labels,c=colors[0])
        plt.fill_between(base, cumulative/100, 0, alpha=0.05,color=colors[0])
    plt.text(np.percentile(data[idx], 90), 0.5, 'Median', color="red", fontsize=14)
    ax.set_xlabel(xaxis_title)
    plt.legend(loc="lower right")
    plt.show()

def get_raw_data():
    return params, results

def summarize_params():
    summary = {}
    for param in params:
        # param is "ms", "occ", "FE" etc
        summary[param] = {}
        for mode in params[param]:
            # mode is "wb", "pvt" "bus"
            summary[param][mode] = {"mean": np.mean(params[param][mode]), "std": np.std(params[param][mode])}
            summary[param][mode]["min"] = max(summary[param][mode]["mean"] - 3.0 * summary[param][mode]["std"], 0)
            summary[param][mode]["max"] = summary[param][mode]["mean"] + 3.0 * summary[param][mode]["std"]
            summary[param][mode]["step"] = (summary[param][mode]["max"] - summary[param][mode]["min"]) / 10
    return summary
