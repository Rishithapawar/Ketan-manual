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
from scipy.interpolate import interp1d

#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
s1 = signal.lti([1], [1,27,207,405])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)
sys = tf([1], [1,27,207,405])
gm, pm, Wgc, Wpc = control.margin(sys)

freq_as_fn_of_w = interp1d(phase, w)
Wgc = freq_as_fn_of_w(-140)
Gm= -64.66

print("Phase Margin=",pm) #Phase margin
print("Gain Margin=",Gm) #Gain margin
print("Gain crossover frequency(dB)=",Wgc) #Gain crossover freq.(dB)
print("Phase crossover frequency(dB)=",Wpc) #Phase crossover freq.(dB)

plt.subplot(2,1,1)
plt.ylabel('Magnitude(deg)')
plt.plot(Wgc,Gm,'o', label='_nolegend_')
plt.text(2,-90, '({}, {})'.format(Wgc.round(2),Gm))
plt.semilogx(w, mag,'b') 
plt.axhline(y = 0,xmin=0,xmax= 1,color = 'b',linestyle='dashed')
plt.axvline(x = Wgc, ymin = -140 ,color='k',linestyle='dashed')
plt.legend(['0 dB line'], loc= 'lower left')
plt.grid() 
      
plt.subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.plot(14.39,-180,'x')
plt.text(14.39,-180, '({}, {})'.format(14.39,-180))
plt.semilogx(w,phase, label='_nolegend_')    
plt.plot(Wgc,-140,'o', label='_nolegend_')
plt.axhline(y = -140,xmin=0,xmax= Wgc,color = 'r',linestyle='dashed')
plt.axvline(x = Wgc, ymin = -140 ,color='k',linestyle='dashed')
plt.text(2,-180, '({}, {})'.format(Wgc.round(2),-140))
plt.legend(['-140 deg line'], loc= 'lower left')
plt.grid() 


#if using termux

plt.savefig('./figs/ee18btech11033/ee18btech11033_2.pdf')
plt.savefig('./figs/ee18btech11033/ee18btech11033_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11033/ee18btech11033_2.pdf"))

#else    

      
#plt.show()
