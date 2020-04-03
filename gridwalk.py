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
n = 20
cellRad = np.floor(CSIZE/(2*n))

WIDTH = np.arange(0,CSIZE+1)
pts = WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))]

colors = ['#8ab7ff','#aad186','#e85d9e']
strokeWidths = [1,1,1,2,2,2,2,2,3,3,3,6,6,12]


step = cellRad*2
nSteps = [2,2,2,2,2,2,2,3,3,3,10]
special = nSteps[-1]
cardinal = [0,1,-1]

############## drawing #########################################################
d = draw.Drawing(CSIZE,CSIZE)


for i in range(len(pts)):
    for j in range(len(pts)):
        thispoint = np.array([pts[i],pts[j]])
        iter = rnd.choice(nSteps)

        if(iter==special):
            clr = rnd.choice(colors)
            sw = strokeWidths[-1]
        else:
            clr = '#000000'
            sw = rnd.choice(strokeWidths[0:-2])

        for n in range(iter):
            vert = rnd.choice(cardinal)
            if(vert!=0):
                horiz = 0
            else:
                horiz = rnd.choice(cardinal)
            newpt = thispoint + (step * np.array([horiz,vert]))
            d.append(draw.Line(thispoint[0],thispoint[1], newpt[0],newpt[1], stroke_width=sw, stroke=clr))
            thispoint = newpt



# d.append(draw.Text("seed", 20, 90,90, font="arial", fill='black'))
d.saveSvg('gridwalk.svg')
