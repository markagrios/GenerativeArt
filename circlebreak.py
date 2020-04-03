import drawSvg as draw
import numpy as np
import random as rnd
import hashlib
import time

t = str(time.time())
s = t.encode()
hash_object = hashlib.sha256(s)
seed = hash_object.hexdigest()
print(seed)

rnd.seed(seed,version=2)

############## parameters ######################################################
CSIZE = 800
mainSize = 100
maxWidth = 3

layers = 7

# angles = [0,90,180,270]
angles = np.linspace(0,360,12)

factor = 4

############## drawing #########################################################

d = draw.Drawing(CSIZE,CSIZE, origin='center')

# d.append(draw.ArcLine(0,0,mainSize, 0,360, stroke='black', stroke_width=2, fill='black',fill_opacity=0.0))

for i in range(layers):
    # iter = rnd.randint(3,10)
    iter = 10
    radii = mainSize + (np.arange(iter)*factor)
    strokeWidths = np.linspace(2,maxWidth,iter)
    arcstart = rnd.choice(angles)
    arcstop = rnd.choice(angles)
    clr = 'black'
    strkclr = 'black'

    for n in range(iter):
        d.append(draw.ArcLine(0,0,radii[n], arcstart,arcstop, stroke=strkclr, stroke_width=strokeWidths[n], fill='red',fill_opacity=0.0))

    mainSize = radii[-1]+factor










d.saveSvg("circlebreak.svg")
