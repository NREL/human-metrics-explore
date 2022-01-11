import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def violin(data, title, yaxis_title = "", yaxis_scale = "linear", ):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.violinplot(data)
    ax.set_title(title+" Distribution")
    
    # add x-tick labels
    #If we don't include walk/bike (for mpg or occupancy?), only label private vehicle vs bus
    if len(data)==3:
        xticklabels = ['Private vehicle', 'Transit bus', 'Walk & bike']
        ax.set_xticks([1,2,3])
    elif len(data)==2:
        xticklabels = ['Private vehicle', 'Transit bus']
        ax.set_xticks([1,2])
    else:
        xticklabels = [title]
        ax.set_xticks = ([1])
    ax.set_xticklabels(xticklabels)
    #ax.set_xlabel('x-axis')
    ax.set_ylabel(yaxis_title)
    
    ax.set_yscale(yaxis_scale)
    plt.show()
    
    
def pdf_plot(data, labels, title, xaxis_title = "", yaxis_scale = "linear"):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    for idx in range(0,len(data)):
        sns.distplot(data[idx], hist = False, kde = True,
                 kde_kws = {'shade': True, 'linewidth': 3},label = labels[idx])
    ax.set_title(title+" Distribution")
    #ax.set_xlabel('x-axis')
    ax.set_xlabel(xaxis_title)
    
    ax.set_yscale(yaxis_scale)
    plt.show()
    
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
            values, base = np.histogram(data[idx], bins=41)
            base[-1]= max([max(x) for x in data])
            cumulative = np.cumsum(values)
            cumulative = np.append(cumulative,100)
            plt.plot(base, cumulative/100, linewidth=linewidth,linestyle=linestyle,label = labels[idx],c=colors[idx])
            plt.fill_between(base, cumulative/100, 0, alpha=0.05,color=colors[idx])
    else: #There is only one dataset being passed in
        values, base = np.histogram(data, bins=41)
        base[-1]= max(data)
        cumulative = np.cumsum(values)
        cumulative = np.append(cumulative,100)
        plt.plot(base, cumulative/100, linewidth=2,label = labels,c=colors[0])
        plt.fill_between(base, cumulative/100, 0, alpha=0.05,color=colors[0])
    ax.set_xlabel(xaxis_title)
    plt.legend(loc="lower right")
    plt.show()
    
    
#Gives CDF with subplots (each mode is separate)
def cdf_subplots(data, labels, xaxis_title = "", colors = ['blue','orange','green']):
    fig,ax = plt.subplots(nrows=1,ncols=len(data))
    for (col,idx,c) in zip(ax,range(0,len(data)),colors):
        values, base = np.histogram(data[idx], bins=41)
        cumulative = np.cumsum(values)
        col.plot(base[:-1], cumulative/100, linewidth=2,label = labels[idx],c=c)
        col.fill_between(base[:-1], cumulative/100, 0, alpha=0.05,color=c)
        col.set_title(labels[idx])
        #col.set_xlabel(xaxis_title)
    fig.text(0.5, 0.06, xaxis_title, ha='center', va='center',fontsize=14)
    plt.show()

#Calculate mode share for pvt given ms for wb and bus
def calc_ms_pvt(ms_bus,ms_wb):
    ms_pvt = 1-(ms_bus+ms_wb)
    return ms_pvt