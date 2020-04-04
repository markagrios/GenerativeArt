import drawSvg as draw
import numpy as np
import random as rnd
import hashlib
import time
import webcolors


t = str(time.time())
s = t.encode()
hash_object = hashlib.sha256(s)
seed = hash_object.hexdigest()
print(seed)

rnd.seed(seed,version=2)


########### parameters##########################################################

HEIGHT = 800
WIDTH = 600

divider = 5

SW = [0.5,0.5,1,1,1,1,1,2,2,2,2,3,3]

nLayers = rnd.randint(3,10)
layers = np.round(np.linspace(0,HEIGHT,nLayers)).astype(int)

points_per_layer = np.round((np.random.random(nLayers)*10) + 1).astype(int)

points_per_layer[::2] = points_per_layer[::2]*5


points = []
for i in range(nLayers):
    row = np.arange(0,WIDTH)
    this_row = np.sort(np.random.choice(row,points_per_layer[i]))
    points.append(this_row)



# print(points_per_layer)
# print(layers)
# print(points)

########### drawing ############################################################
d = draw.Drawing(WIDTH,HEIGHT)

d.append(draw.Line(0,0, WIDTH,0, stroke_width=int(divider*2), stroke='black'))
d.append(draw.Line(0,HEIGHT, WIDTH,HEIGHT, stroke_width=int(divider*2), stroke='black'))

for r in range(len(points)-1):
    L = draw.Line(0,layers[r], WIDTH,layers[r], stroke_width=divider, stroke='black')
    d.append(L)

    for p in range(len(points[r])):
        sw = rnd.choice(SW)
        adder = rnd.randint(0,5)
        line = draw.Line(points[r][p],layers[r], points[r+1][np.mod(p+adder,len(points[r+1]))],layers[r+1], stroke_width=sw, stroke='black')

        d.append(line)




# d.append(draw.Line(thispoint[0],thispoint[1], newpt[0],newpt[1], stroke_width=sw, stroke='black'))


d.saveSvg('bipart.svg')
