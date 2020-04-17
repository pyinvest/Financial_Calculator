#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Financial_calculator():
    PV=float(input("Please enter the principal (If you don't know, please enter 0): "))
    r=float(input("Please enter the interest rate (return rate), e.g. 2 for 2% (If you don't know, please enter 0): "))/100
    y=float(input("Please enter the years (If you don't know, please enter 0): "))
    FV=float(input("Please the amount you need in the future (If you don't know, please enter 0): "))
    if FV==0:
        FV=PV*(1+r)**y
        print('You will have '+str(round(FV,2))+' after '+str(y)+' years.')
        FV_list=[]
        for i in range(int(y)+1):
            FV=PV*(1+r)**i
            FV_list.append(FV)
        FV_list=pd.Series(FV_list)
        FV_list.plot()
        plt.title('Accumulated Asset')
    elif PV==0:
        PV=FV/(1+r)**y
        print('You need to deposit $'+str(round(PV,2))+ ' today')
    elif r==0:
        r=(FV/PV)**(1/y)-1
        r=r*100
        print('You need to find an financial product with '+str(round(r,2))+ '% per year')
    elif y==0:
        y=np.log(FV/PV)/np.log(1+r)
        print('You will achieve your goal in '+str(round(y,2))+ ' years')
        
Financial_calculator()

