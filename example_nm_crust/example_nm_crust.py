#!/usr/bin/python3

# Before run:
# Get wata lib:
#   pip3 install wdata
# (add -U if you want to update)
# For more info see:
#   https://pypi.org/project/wdata/


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from wdata.io import WData, Var

fwtxt="example.wtxt"
data = WData.load(fwtxt)

ratio=data.Nxyz[2]/data.Nxyz[1]
scale=2.0
fig, ax = plt.subplots(figsize=(scale*ratio,1.2*scale))

cross=int(data.Nxyz[0]/2)
im = ax.imshow(data.rho_n[0][cross,:,:], interpolation='bilinear', extent=[0, data.Nxyz[2], 0, data.Nxyz[1]], aspect='auto')
fig.colorbar(im, ax=ax, orientation="horizontal")

plt.tight_layout()
# fig.savefig("rho_n.png")
plt.show()
