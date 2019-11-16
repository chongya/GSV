import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.ticker as tk

'''
    This script shows how to fit multispectral soil reflectance
    and then reconstruct hyperspectral soil reflectance
    using the GSV model
'''

# The hyperspectral wavelengths
WVL = np.arange(400,2501,10)
# The general spectral vectors derived in the manuscript
GSV = np.vstack([np.loadtxt('MD.vec.txt'),np.loadtxt('SM.vec.txt')])
# The test hyperspectral data
hyper = np.loadtxt('TestSpectrum.csv',delimiter=',',skiprows=1)
# The wavelengths of multispectral data
wvl = np.array([450,550,650,850,1650,2150])
# The test multispectral data sliced from hyperspectral data
multi = hyper[np.in1d(WVL,wvl)]

fig = plt.figure()
ax = fig.add_subplot(1,2,1)

# Step 1: slice GSV according to the wavelengths of multispectral data
gsv = GSV[:,np.in1d(WVL,wvl)]

# Step 2: fit multispectral soil reflectance and reconstruct multispectral soil reflectance
X = multi
V = gsv
C = np.dot(X,la.pinv(V))
R = np.dot(C,V)
R[R<0] = 0
R[R>1] = 1
plt.scatter(X,R,c='k')
plt.plot([0,0.4],[0,0.4],'k')
plt.xlabel('Measurements')
plt.ylabel('Simulations')
plt.show()

# Step 3: reconstruct hyperspectral soil reflectance using coefficients fitted from multispectral data
X = hyper
V = GSV
R = np.dot(C,V)
R[R<0] = 0
R[R>1] = 1
plt.scatter(X,R,c='k')
plt.plot([0,0.4],[0,0.4],'k')
plt.xlabel('Measurements')
plt.ylabel('Simulations')
plt.show()

# Compare measured multispectral data and hyperspectral data with reconstructed ones
fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(WVL,hyper.T,'k--')
ax.plot(wvl,multi,'ko')
ax.plot(WVL,R,'r-')
ax.legend(['Actual hyperspectral reflectance','Observed multispectral reflectance','Simulated hyperspectral reflectance\nfitted from multispectral reflectance'],fontsize=6)

ax.set_xlim(400,2500)
ax.set_xlabel('Wavelength (nm)',labelpad=0)
ax.set_ylim(0,0.5)
ax.set_yticks(np.arange(0,0.51,0.1))
ax.set_ylabel('Reflectance',labelpad=2)
ax.xaxis.set_major_locator(tk.FixedLocator(locs=range(400,2501,700)))
ax.xaxis.set_minor_locator(tk.FixedLocator(locs=range(400,2501,100))) 
ax.text(0.05,0.95,'(a)',ha='left',va='top',size=12,transform=ax.transAxes)
[tl.set_markersize(3) for tl in ax.yaxis.get_ticklines(minor=False) + ax.xaxis.get_ticklines(minor=False)]
[tl.set_markersize(2) for tl in ax.yaxis.get_ticklines(minor=True) + ax.xaxis.get_ticklines(minor=True)]
[sp.set_linewidth(0.5) for sp in ax.spines.values()] 

'''
    This script shows how to simulate a series of soil spectra
    using combinations of four soil coefficients.
'''

ax = fig.add_subplot(1,2,2)
for c1 in [0.3,0.7]:
    for c2 in [-0.1,0]:
        for c3 in [0,0.05]:
            for cSM in [-0.2,0]:
                ax.plot(WVL,c1*V[0]+c2*V[1]+c3*V[2]+cSM*V[3],c=np.random.rand(3),lw=0.5)
ax.set_xlim(400,2500)
ax.set_xlabel('Wavelength (nm)',labelpad=0)
ax.set_ylim(0,1)
ax.set_yticks(np.arange(0,1.01,0.2))
ax.set_ylabel('Reflectance',labelpad=2)
ax.xaxis.set_major_locator(tk.FixedLocator(locs=range(400,2501,700)))
ax.xaxis.set_minor_locator(tk.FixedLocator(locs=range(400,2501,100))) 
ax.text(0.05,0.95,'(b)',ha='left',va='top',size=12,transform=ax.transAxes)
[tl.set_markersize(3) for tl in ax.yaxis.get_ticklines(minor=False) + ax.xaxis.get_ticklines(minor=False)]
[tl.set_markersize(2) for tl in ax.yaxis.get_ticklines(minor=True) + ax.xaxis.get_ticklines(minor=True)]
[sp.set_linewidth(0.5) for sp in ax.spines.values()] 
                
plt.rc('font',size=6)        
fig.subplots_adjust(left=0.08,right=0.97,bottom=0.19,top=0.97)
fig.set_size_inches(16.5/2.54,16.5/2.54*0.5*0.618)
plt.savefig('Examples.png',dpi=300)
