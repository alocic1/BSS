import matplotlib.pyplot as plt
import csv
import datetime, time
import numpy as np
import matplotlib.gridspec as gridspec
from scipy.signal import find_peaks

def nadjiMax(niz, vrijeme, par):
    tacke = []
    poX = []
    max = par
    index = -1.
    ovdje = 0
    for i in range(len(niz)):
        if(niz[i] >= max):
            max = niz[i]
            index = vrijeme[i]
            ovdje = 1
        elif(niz[i] < max and  ovdje == 1):
            ovdje = 0
            tacke.append(max)
            poX.append(index)
            index = -1.
            max = par
    return tacke, poX

def nadjiMin(niz, vrijeme, par):
    tacke = []
    poX = []
    min = par
    index = -1.
    ovdje = 0
    for i in range(len(niz)):
        if(niz[i] <= min):
            min = niz[i]
            index = vrijeme[i]
            ovdje = 1
        elif(niz[i] > min and  ovdje == 1):
            ovdje = 0
            tacke.append(min)
            poX.append(index)
            index = -1.
            min = par
    return tacke, poX


vrijemeString = []
vrijeme = []
mili = []
II = []
AVR = []
V = []
RESP = []
PLETH = []
ABP = []

with open('samples.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        vrijemeString.append(str(row[0]))
        II.append(float(row[1]))
        AVR.append(float(row[2]))
        V.append(float(row[3]))
        #RESP.append(float(row[4]))
        #PLETH.append(float(row[5]))
        #ABP.append(float(row[6]))

for x in vrijemeString:
    x = x.replace("[", "")
    x = x.replace("]", "")
    x = x.replace("'", "")
    vrijeme.append(datetime.datetime.strptime(x, '%H:%M:%S.%f'))

for x in vrijeme:
    mili.append((x-datetime.datetime(1900,1,1)).total_seconds()-61649.564)

maxII, vrijemeII = nadjiMax(II, mili, 0.7)

minAVR, vrijemeAVR = nadjiMin(AVR, mili, 0.1)

maxV, vrijemeMaxV = nadjiMax(V, mili, 1.27)

minV, vrijemeMinV = nadjiMin(V, mili, 0)

#plt.plot(mili,II, label='Loaded from file!')
#plt.xlabel('vrijeme')
#plt.ylabel('II')
#plt.title('MIMIC II/III, part 2')
#plt.legend()
#plt.grid()
#plt.show()




fig = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(3, 1, figure=fig)
ax = fig.add_subplot(gs[0,0])
major_ticks = np.arange(0, 11, 0.2)
minor_ticks = np.arange(0, 11, 0.04)
major_ticks2 = np.arange(-1, 2, 0.5)
minor_ticks2 = np.arange(-1, 2, 0.1)
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks2)
ax.set_yticks(minor_ticks2, minor=True)

ax.grid(which='both')

ax.grid(which='minor',  color = 'red', linewidth = 0.2)
ax.grid(which='major', color = 'red', linewidth = 0.5)
plt.ylabel('II')
ax.grid(which='major', alpha=2)
plt.plot(mili,II)
plt.scatter(vrijemeII, maxII, color = 'black')
plt.plot(0,0)
 
#---------------------------------

ax2= fig.add_subplot(gs[1,0])

ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.spines['left'].set_position('zero')
ax2.spines['bottom'].set_position('zero')
ax2.set_xticks(major_ticks)
ax2.set_xticks(minor_ticks, minor=True)
ax2.set_yticks(major_ticks2)
ax2.set_yticks(minor_ticks2, minor=True)
plt.ylabel('AVR')
ax2.grid(which='both')

ax2.grid(which='minor',  color = 'red', linewidth = 0.2)
ax2.grid(which='major', color = 'red', linewidth = 0.5)

plt.plot(mili,AVR)
plt.scatter(vrijemeAVR, minAVR, color = 'black')
plt.plot(0,0)
plt.plot(0,1)

#--------------------------------

ax3= fig.add_subplot(gs[2,0])

ax3.set_yticklabels([])
ax3.set_xticklabels([])
ax3.spines['left'].set_position('zero')
ax3.set_xticks(major_ticks)
ax3.set_xticks(minor_ticks, minor=True)
ax3.set_yticks(major_ticks2)
ax3.set_yticks(minor_ticks2, minor=True)
ax3.grid(which='both')

ax3.grid(which='minor',  color = 'red', linewidth = 0.2)
ax3.grid(which='major', color = 'red', linewidth = 0.5)
plt.axhline(y=0, color='red', linestyle='-', linewidth=1.5);
plt.plot(mili,V)
plt.scatter(vrijemeMinV, minV, color = 'black')
plt.scatter(vrijemeMaxV, maxV, color = 'black')
plt.ylabel('V')
plt.plot(0,-0.3)
plt.plot(0,1.4)

#---------------------------------

#ax4= fig.add_subplot(gs[3,0])

#ax4.set_yticklabels([])
#ax4.set_xticklabels([])
#ax4.spines['left'].set_position('zero')
#ax4.spines['bottom'].set_position('zero')
#ax4.set_xticks(major_ticks)
#ax4.set_xticks(minor_ticks, minor=True)
#ax4.set_yticks(major_ticks2)
#ax4.set_yticks(minor_ticks2, minor=True)

#ax4.grid(which='both')

#ax4.grid(which='minor',  color = 'red', linewidth = 0.2)
#ax4.grid(which='major', color = 'red', linewidth = 0.5)

#plt.plot(mili,RESP, label='RESP')
#plt.plot(0,0)
#plt.plot(0,1)

#---------------------------------

#ax5= fig.add_subplot(gs[4,0])

#ax5.set_yticklabels([])
#ax5.set_xticklabels([])
#ax5.spines['left'].set_position('zero')
#ax5.spines['bottom'].set_position('zero')
#ax5.set_xticks(major_ticks)
#ax5.set_xticks(minor_ticks, minor=True)
#ax5.set_yticks(major_ticks2)
#ax5.set_yticks(minor_ticks2, minor=True)

#ax5.grid(which='both')

#ax5.grid(which='minor',  color = 'red', linewidth = 0.2)
#ax5.grid(which='major', color = 'red', linewidth = 0.5)

#plt.plot(mili,PLETH, label='PLETH')
#plt.plot(0,0)
#plt.plot(0,3)

#---------------------------------

#ax6= fig.add_subplot(gs[5,0])
#major_ticks3 = np.arange(0, 100, 0.04)
#minor_ticks3 = np.arange(-1, 150, 50)
#ax6.set_yticklabels([])
#ax6.set_xticklabels([])
#ax6.spines['left'].set_position('zero')
#ax6.spines['bottom'].set_position('zero')
#plt.minorticks_on()
#ax6.set_xticks(major_ticks)
#ax6.set_xticks(minor_ticks, minor=True)
#ax6.set_yticks(major_ticks3)
#ax6.set_yticks(minor_ticks3, minor=True)

#ax6.grid(which='minor', alpha=0.5)
#ax6.grid(which='major', alpha=2)

#plt.plot(mili,ABP, label='ABP')
#plt.plot(0,0)
#plt.plot(0,150)

plt.show()
