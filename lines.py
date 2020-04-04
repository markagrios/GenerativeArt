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

cardinal = [-1,1]               # directions the lines can go
lenFactors = [1,1,1,1,2,2,3,4,10]     # how long the lines can be
strokeFactors = [1,1,1,2,2,2,2,2,3,3,3,6,6,10]
SW = 2                          # stroke width


WIDTH = np.arange(0,CSIZE+1)
pts = WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))]


############## drawing #########################################################
d = draw.Drawing(CSIZE,CSIZE)

for i in range(len(pts)):
    for j in range(len(pts)):
        direction = [rnd.choice(cardinal),rnd.choice(cardinal)]
        thispoint = np.array([pts[i],pts[j]])
        fctr = rnd.choice(lenFactors)
        sfctr = rnd.choice(strokeFactors)
        newpt = [thispoint[0]+(direction[0]*(cellRad*fctr)), thispoint[1]+(direction[1]*(cellRad*fctr))]
        # newpt = [thispoint[0]+(direction[0]*(cellRad)), thispoint[1]+(direction[1]*(cellRad))]
        d.append(draw.Line(thispoint[0],thispoint[1], newpt[0],newpt[1], stroke_width=sfctr, stroke='black'))











d.saveSvg('lines.svg')
d.savePng('lines.png')
