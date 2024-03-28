import matplotlib.pyplot as plt
from io import BytesIO
from io import StringIO
import numpy as np
import base64
import os

def get_graph():
    #buffer =BytesIO()
    #plt.savefig(buffer, format='png')
    #buffer.seek(0)
    #image_png = buffer.getvalue()
    #graph=base64.b64encode(image_png)
    #graph=graph.decode('utf-8')
    #buffer.close()
    #return graphs
    #x = np.arange(0,np.pi*3,.1)
    #y = np.sin(x)
    #x=[4,6,9]
    #y=[5,23,34]

    #fig = plt.figure()
    #plt.plot(x,y)

    imgdata = StringIO()
    #fig.savefig(imgdata, format='svg')
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def get_plot(x,y,z):
    # give data here
    # switch backend
    #s=['bad','good','casting','kibru','woooooo','End of All']
    #z=[14,7,4,34,16,12]
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5)) 
    plt.title(' Product graph') 
    plt.plot(x,z,label="Ethiopian")
    #plt.scatter(s,z,label="Ethiopian")
    #plt.scatter(x,y)
    #bar_labels = ['red', 'blue', '_red', 'orange','blue','red',]
    #bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:red','tab:blue']

    #ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
    plt.bar(x,y,label="South African", color='r')
    plt.xticks(rotation=45)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.tight_layout()
    plt.legend()
    
    
    graph = get_graph()
    return graph








