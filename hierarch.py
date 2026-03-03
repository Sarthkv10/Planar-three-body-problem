# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:34:49 2024

@author: Sarthak
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
m1,m2,m3=1,1,3
G,h=1,0.01
dt=0.01
t=np.arange(0,255.5+dt,dt)
r1=np.empty((len(t),2))
r2=np.empty((len(t),2))
r3=np.empty((len(t),2))
v1=np.empty((len(t),2))
v2=np.empty((len(t),2))
v3=np.empty((len(t),2))
def dv1t(r1,r2,r3):
    return G*(m2*(r2-r1)/((np.linalg.norm(r1-r2))**3)+m3*(r3-r1)/((np.linalg.norm(r1-r3))**3))
def dv2t(r1,r2,r3):
    return G*(m1*(-r2+r1)/((np.linalg.norm(r1-r2))**3)+m3*(-r2+r3)/((np.linalg.norm(r2-r3))**3))
def dv3t(r1,r2,r3):
    return G*(m1*(-r3+r1)/((np.linalg.norm(r1-r3))**3)+m2*(-r3+r2)/((np.linalg.norm(r2-r3))**3))
def PTBP2(c,d):
   
    r1[0]=[-1.00,0.00]
    v1[0]=[0.3489,0.5306]
    r2[0]=[-10.00,5.00]
    v2[0]=v1[0]
    v3[0]=[-2*(m1/m3)*v1[0][0],-2*(m2/m3)*v1[0][1]]
    for i in range(len(t)-1):
        x,y,z=r1[i],r2[i],r3[i]
        v1[i+1]=v1[i]+h*dv1t(x,y,z)
        r1[i+1]=r1[i]+h*v1[i+1]
        v2[i+1]=v2[i]+h*dv2t(x,y,z)
        r2[i+1]=r2[i]+h*v2[i+1]
        v3[i+1]=v3[i]+h*dv3t(x,y,z)
        r3[i+1]=r3[i]+h*v3[i+1]
        
    plt.figure(figsize=(10,7))
    plt.plot(r1[:,0],r1[:,1],linestyle='solid',alpha=0.7)
    plt.plot(r2[:,0],r2[:,1],linestyle=':',color='red')
    plt.plot(r3[:,0],r3[:,1],linestyle='solid',color='green',alpha=0.7)
    plt.scatter(r1[len(t)-1,0],r1[len(t)-1,1])
    plt.scatter(r2[len(t)-1,0],r2[len(t)-1,1])
    plt.scatter(r3[len(t)-1,0],r3[len(t)-1,1]) 
    plt.title("Hierarichal orbit")
    plt.grid()
    plt.xlabel('$x- axis$')
    plt.ylabel('$y- axis$')
    plt.tight_layout()
   
    plt.legend(['Body-1','Body-2','Body-3'],fontsize='10')
    plt.show()
    collision_time=[]
    for i in range(len(t)):
        if np.array_equal(r1[i],r2[i]) or np.array_equal(r2[i],r3[i]) or np.array_equal(r1[i],r3[i]):
            collision_time.append(t[i])
    if collision_time:
        print('Collision detected at time :{collision_time} ')
    else:
        print('No collision')
    
  
PTBP2(0.213841083,0.054293840)

