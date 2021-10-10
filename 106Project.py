from numpy.lib.function_base import corrcoef
import pandas as pd
import plotly.express as px
import csv 
import numpy as np

with open(r"C:\Users\Chiranjeev\Downloads\Data-visualization-master\Student Marks vs Days Present.csv") as f:
          csvr=csv.DictReader(f)
          M=[]
          DP=[]
          for i in csvr:
                    M.append(float(i["Marks"]))
                    DP.append(float(i["Days"]))

          corelation=np.corrcoef(M,DP)

          print(corelation)

