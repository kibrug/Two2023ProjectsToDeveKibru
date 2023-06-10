import matplotlib.pyplot as plt
from io import BytesIO
from io import StringIO
import numpy as np
import base64
import os

def get_graph():
  

    imgdata = StringIO()
    #fig.savefig(imgdata, format='svg')
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def get_plot(x,y,z,zy):
   
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5)) 
    plt.title("Graph Data") 
    plt.plot(x,z,label=zy[0])
   
    plt.bar(x,y,label=zy[1], color='r')
    plt.xticks(rotation=45)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.tight_layout()
    plt.legend()
    
    
    graph = get_graph()
    return graph








