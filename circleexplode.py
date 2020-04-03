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


########### parameters##########################################################

CSIZE = 800
n = 3                   # these are the fun parameters to change
nCircles = 8           # except I can't exactly pinpoint what they do
spokes = 10

cellRad = np.floor(CSIZE/(2*n))

minRad = round(cellRad*0.3)
maxRad = round(cellRad*0.9)

maxR = cellRad
swidths = [0.5,1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,5]


########### drawing ############################################################

d = draw.Drawing(CSIZE,CSIZE, origin='center')

thispoint = np.array([0,0])


for i in range(spokes):
    offsetLB = np.round((-1*CSIZE)*1.9)
    offsetUB = np.round((CSIZE)*1.9)
    offset = np.array([rnd.randint(offsetLB,offsetUB),rnd.randint(offsetLB,offsetUB)])
    centersx = np.linspace(offset[0], thispoint[0], nCircles)
    centersy = np.linspace(offset[1], thispoint[1], nCircles)

    lastCirc = rnd.choice([0,1])
    if(lastCirc == 0):
        this_n = nCircles-1
    else:
        this_n = nCircles
    for n in range(this_n):
        rad = rnd.randint(minRad,maxRad)
        sw = rnd.choice(swidths)
        clr = 'black'
        d.append(draw.Circle(centersx[n],centersy[n], rad, fill_opacity=0.0, stroke=clr, stroke_width=sw))




d.saveSvg('circleexplode.svg')
