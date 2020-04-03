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

CSIZE = 800
n = 6
nCircles = 7
colors = ['#ffffff','#ffffff','#8ab7ff','#aad186','#e85d9e','#8ab7ff','#aad186','#e85d9e','#8ab7ff','#aad186','#e85d9e','#8ab7ff','#aad186','#e85d9e']


cellRad = np.floor(CSIZE/(2*n))


WIDTH = np.arange(0,CSIZE+1)
pts = WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))]

# print(cellRad)
# print(pts)




d = draw.Drawing(CSIZE,CSIZE)

maxR = cellRad
swidths = [1,1,1,1,1,1,1,1,2,2,2,3,3,4,5]

for i in range(len(pts)):
    for j in range(len(pts)):
        for n in range(nCircles):
            rad = rnd.randint(round(cellRad*0.2),round(cellRad*0.9))
            sw = rnd.choice(swidths)
            clr = rnd.choice(colors)
            d.append(draw.Circle(pts[i],pts[j], rad, fill_opacity=0.0, stroke=clr, stroke_width=sw))

# for i in range(nCircles):
#     rad = rnd.randint(20,maxR)
#     sw = rnd.choice(swidths)
#     d.append(draw.Circle(0,0, rad, fill_opacity=0.0, stroke='black', stroke_width=sw))
#



d.saveSvg('circles.svg')
