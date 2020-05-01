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

#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
s1 = signal.lti([116.01], [1,27,207,405]) 

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)
sys = tf([116.01], [1,27,207,405])
gm, pm, Wgc, Wpc = control.margin(sys)
Gm = -20*log10(gm)

print("Phase Margin=",pm) #Phase margin
print("Gain Margin=",Gm) #Gain margin
print("Gain crossover frequency(dB)=",Wgc) #Gain crossover freq.(dB)
print("Phase crossover frequency(dB)=",Wpc) #Phase crossover freq.(dB)


plt.subplot(2,1,1)
plt.ylabel('Magnitude(deg)')
plt.semilogx(w, mag,'b') 
plt.axhline(y = -33,xmin=0,xmax= 14.39,color = 'r',linestyle='dashed')
plt.axvline(x = 14.39,ymin=-33,color='k',linestyle='dashed')
plt.plot(14.39,-33,'o')
plt.text(14.39,-33, '({}, {})'.format(14.39,-33))
plt.grid() 
      

plt.subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w,phase) 
plt.axvline(x = 14.39,ymin=-180,color='k',linestyle='dashed')
plt.axhline(y = -180,xmin=0,xmax=14.39,color = 'r',linestyle='dashed')
plt.plot(14.39,-180,'x')
plt.text(14.39,-180, '({}, {})'.format(14.39,-180))
plt.grid() 


#if using termux

plt.savefig('./figs/ee18btech11033/ee18btech11033_ver1.pdf')
plt.savefig('./figs/ee18btech11033/ee18btech11033_ver1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11033/ee18btech11033_ver1.pdf"))

#else    

#plt.show()
