# License
'''
Code by Rishitha
April 29,2020
Released under GNU GPL
'''
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
import control
from control import tf
import numpy as np
from scipy.optimize import fmin
import scipy 

#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
k=920
sys = signal.lti([k], [1,27,207,405+k])
t,y = signal.step(sys)
max(y)
plt.plot(t,y)
ss = k/(405+k)
po = ((max(y)-ss)/ss)*100

print("peak value = ",max(y).round(2))
print("steady state value=",round(ss,2))
print("PO=",po.round(2))

plt.plot(0.48,max(y),'o', label='_nolegend_')
plt.text(0.48,max(y),'({}, {})'.format(0.48,max(y).round(2)))
plt.plot(2,ss,'o', label='_nolegend_')
plt.text(2,ss,'({}, {})'.format(2,round(ss,2)))
plt.grid()

#if using termux

plt.savefig('./figs/ee18btech11033/ee18btech11033_3.pdf')
plt.savefig('./figs/ee18btech11033/ee18btech11033_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11033/ee18btech11033_3.pdf"))

#else      

#plt.show()
