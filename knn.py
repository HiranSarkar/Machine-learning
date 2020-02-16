import pandas as pd
import math
import numpy as np
from scipy.stats import mode
df=pd.read_csv("")
pf=np.array(df)
l=[]
k=3
def norm():
    for i in range(1,pf.shape[1]):
        mi=min(pf[0:,i])
        ma=max(pf[0:,i])
        pf[0:,i]=(pf[0:,i]-mi)/(ma-mi)
    return pf
def eucl_dist(r1,r2):
    pf=norm()
    d=0
    for i in range(1,pf.shape[1]):
        if i in l:
            if r1[i]!=r2[i]:
                d+=1
        else:
            d+=((r1[i]-r2[i])**2)
    d=math.sqrt(d)
    return d
def k_classes(r,k):
    cf=pf
    e=[]
    for i in range (k):
        s=eucl_dist(r,cf[0,1:],)
        for j in range(pf.shape[0]):
            d=eucl_dist(r,cf[j,1:])
            if d<s:
                s=d
                q=j
        e.append(cf[j,0])
        cf=np.delete(cf,q,0)
    return e
def predict(pf,test,k):
    for r in test:
        p=k_classes(r,k)
        p=np.array(p)
        print(mode(p)[0][0])
predict(pf,test,k)
