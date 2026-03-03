# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:41:22 2024

@author: Sarthak
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:19:52 2024

@author: Sarthak
"""

import numpy as np ; import matplotlib.pyplot as plt ; from matplotlib import style

m1=1; m2=1;m3=1

def f1(r):
    r1,r2,r3=r
    a1= m2*(r2-r1)/np.linalg.norm(r1-r2)**3 + m3*(r3-r1)/np.linalg.norm(r1-r3)**3
    a2= m1*(r1-r2)/np.linalg.norm(r2-r1)**3 + m3*(r3-r2)/np.linalg.norm(r2-r3)**3
    a3= m1*(r1-r3)/np.linalg.norm(r3-r1)**3 + m2*(r2-r3)/np.linalg.norm(r3-r2)**3
    return np.array([a1,a2,a3])
   
#Initial Conditions
G=1 
r1= np.array([-1,0])
r2=np.array([1,0])
r3= np.array([0,0])

v1= np.array([ 0.61504, 0.52261])
v2= v1
v3= -2*v1
h=0.01
t= np.arange(0,43+h,h)
r= np.zeros((len(t),3,2))
v= np.zeros((len(t),3,2))
r[0]=np.array([r1,r2,r3])
v[0]=np.array([v1,v2,v3])

for i in range(len(t)-1):
    v12= v[i]+ 0.5*h*f1(r[i])
    r[i+1]= r[i]+ h*v12
    v[i+1]= v12 + 0.5*h*f1(r[i+1])
    
collision_time=[]  
for i in range(len(t)):
    r1,r2,r3=r[i]
    if np.array_equal(r1,r2) or np.array_equal(r2,r3) or np.array_equal(r3,r1):
        collision_time.append(t[i])
        
if collision_time:
    print(f'collision detected at time:{collision_time}')
else:
    print("No collision")
        

x1, y1 = r[:, 0, 0], r[:, 0, 1]
x2 ,y2= r[:,1,0],r[:,1,1]
x3,y3= r[:,2,0], r[:,2,1]

plt.figure(figsize=(10,7))
plt.plot(x1,y1,linestyle='solid',label='body 1')
plt.plot(x2,y2,linestyle='solid',label='body 2')
plt.plot(x3,y3,linestyle='solid',color='red',label='body 3')
plt.legend()
plt.title("3- body problem butterfly orbit")
plt.grid(True)
plt.show()

#%% 
## Phase space for x components , similarly it can be done for y 

m1=1; m2=1;m3=1

def a1(r1,r2,r3):
    return m2*(r2-r1)/np.linalg.norm(r1-r2)**3 + m3*(r3-r1)/np.linalg.norm(r1-r3)**3
def a2(r1,r2,r3):
    return m1*(r1-r2)/np.linalg.norm(r2-r1)**3 + m3*(r3-r2)/np.linalg.norm(r2-r3)**3
def a3(r1,r2,r3):
    return m1*(r1-r3)/np.linalg.norm(r3-r1)**3 + m2*(r2-r3)/np.linalg.norm(r3-r2)**3

    
#Initial Conditions

G=1 

h=0.01
t= np.arange(0,100+h,h)
r1= np.empty((len(t),2))
r2= np.empty((len(t),2))
r3= np.empty((len(t),2))
v1=np.empty((len(t),2))
v2=np.empty((len(t),2))
v3=np.empty((len(t),2))

r1[0]= np.array([-1.0024277970,0.0041695061])
r2[0]= np.array([1.0024277970,-0.0041695061])
r3[0]= np.array([0,0])

v1[0]= np.array([0.3489048974,0.5306305100])
v2[0]= np.array([0.3489048974,0.5306305100])
v3[0]= -2*v1[0]

for i in range(len(t)-1):
    a1_= a1(r1[i],r2[i],r3[i]) # a1,a2,a3 are defined fns for acc of m1,m2,m3
    a2_= a2(r1[i],r2[i],r3[i])
    a3_= a3(r1[i],r2[i],r3[i])
    
    v12= v1[i]+ 0.5*h*a1_
    v22= v2[i]+ 0.5*h*a2_
    v32= v3[i]+ 0.5*h*a3_
    
    r1[i+1]=r1[i]+h*v12
    r2[i+1]=r2[i]+h*v22
    r3[i+1]=r3[i]+h*v32
    
    a1_new= a1(r1[i+1],r2[i+1],r3[i+1])
    a2_new= a2(r1[i+1],r2[i+1],r3[i+1])
    a3_new= a3(r1[i+1],r2[i+1],r3[i+1])
    
    v1[i+1]= v12 + h*0.5*a1_new 
    v2[i+1]= v22 + h*0.5*a2_new
    v3[i+1]= v32 + h*0.5*a3_new
    
    
    
r1x= r1[:,0]
v1v= v1[:,0]

r2x= r2[:,0]
v2v= v2[:,0]

r3x= r3[:,0]
v3v= v3[:,0]

r1y= r1[:,1]
v1vs= v1[:,1]

r2y= r2[:,1]
v2vs= v2[:,1]

r3y= r3[:,1]
v3vs= v3[:,1]


plt.figure(figsize=(15,20))

plt.subplot(3,3,1)
plt.plot(r1x,v1v, color='r')
plt.plot(r1y,v1vs, color='r')
plt.xlabel('x1')
plt.ylabel('vx1')
plt.grid()


plt.subplot(3,3,2)
plt.plot(r2x,v2v, color='b')
plt.plot(r2y,v2vs, color='b')
plt.xlabel('x2')
plt.ylabel('vx2')
plt.grid()

plt.subplot(3,3,3)
plt.plot(r3x,v3v, color='g')
plt.plot(r3y,v3vs, color='r')
plt.xlabel('x3')
plt.ylabel('vx3')
plt.grid()

plt.suptitle("Figure 8 Phase space- X components",fontsize=25)
plt.tight_layout(rect=[0,0,1,0.99])
plt.show()