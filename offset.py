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
n = 4
nCircles = 7
# colors = ['#ffffff','#8ab7ff','#aad186','#e85d9e','#8ab7ff','#aad186','#e85d9e']


cellRad = np.floor(CSIZE/(2*n))


WIDTH = np.arange(0,CSIZE+1)
pts = WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))]

minRad = round(cellRad*0.4)
maxRad = round(cellRad*0.7)



########### drawing ############################################################

d = draw.Drawing(CSIZE,CSIZE)

maxR = cellRad
swidths = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,5]

for i in range(len(pts)):
    for j in range(len(pts)):
        thispoint = np.array([pts[i],pts[j]])
        offsetLB = np.round((-1*cellRad)*0.3)
        offsetUB = np.round((cellRad)*0.3)
        offset = np.array([rnd.randint(offsetLB,offsetUB),rnd.randint(offsetLB,offsetUB)])
        offset = thispoint + offset
        centersx = np.linspace(offset[0], thispoint[0], nCircles)
        centersy = np.linspace(offset[1], thispoint[1], nCircles)
        for n in range(nCircles):
            rad = rnd.randint(minRad,maxRad)
            sw = rnd.choice(swidths)
            clr = 'black'
            d.append(draw.Circle(centersx[n],centersy[n], rad, fill_opacity=0.0, stroke=clr, stroke_width=sw))

# for i in range(nCircles):
#     rad = rnd.randint(20,maxR)
#     sw = rnd.choice(swidths)
#     d.append(draw.Circle(0,0, rad, fill_opacity=0.0, stroke='black', stroke_width=sw))
#



d.saveSvg('offset.svg')
# d.savePng('offset.png')
