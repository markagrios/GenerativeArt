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


########### parameters ##########################################################
CSIZE = 800
n = 15
cellRad = np.floor(CSIZE/(2*n))

cardinal = [-1,1]               # directions the lines can go
lenFactors = [1,1,1,1,2,2,3,4,10]     # how long the lines can be
strokeFactors = [1,1,1,2,2,2,2,2,3,3,3,6,6,10]
SW = 2                          # stroke width


WIDTH = np.arange(0,CSIZE+1)
pts = WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))]



########### drawing ############################################################
d = draw.Drawing(CSIZE,CSIZE)

d.append(draw.Line(pts[4],pts[2], pts[4],pts[3], stroke_width=20, stroke='black'))
d.append(draw.ArcLine(pts[3],pts[3],cellRad*2, 0,90, stroke='black', stroke_width=20, fill='black',fill_opacity=0.0))
d.append(draw.Line(pts[3],pts[4], pts[2],pts[4], stroke_width=20, stroke='black'))













d.saveSvg('worm.svg')
