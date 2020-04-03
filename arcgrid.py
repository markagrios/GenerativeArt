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
n = 6
cellRad = np.floor(CSIZE/(2*n))

WIDTH = np.arange(0,CSIZE+1)
pts = np.array(WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))])

colors = ['#ffffff','#ffffff','#ffffff','#ffffff','#ffffff','#cf8142','#8149d6','#ba148b']
stroke_colors = ['#cf8142','#8149d6','#ba148b']
# decide = [0,1]

angles = [0,90,180,270]
# angles = np.linspace(0,360,12)

iter = 7
rads = np.linspace(cellRad/4,1*cellRad,iter)

SW = np.linspace(1,5,iter)

############## drawing #########################################################

d = draw.Drawing(CSIZE,CSIZE)


for i in range(len(pts)):
    for j in range(len(pts)):
        thispoint = np.array([pts[i],pts[j]])
        arcstart = rnd.choice(angles)
        arcstop = rnd.choice(angles)
        clr = rnd.choice(colors)
        strkclr = rnd.choice(stroke_colors)

        # d.append(draw.ArcLine(thispoint[0],thispoint[1],2*cellRad, arcstart,arcstop, stroke=strkclr, stroke_width=2, fill=clr,fill_opacity=0.3))
        for n in range(iter):
            d.append(draw.ArcLine(thispoint[0],thispoint[1],rads[n], arcstart,arcstop, stroke=strkclr, stroke_width=SW[n], fill='red',fill_opacity=0.0))









d.saveSvg('arcgrid.svg')
