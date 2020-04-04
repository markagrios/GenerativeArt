import drawSvg as draw
import numpy as np
import random as rnd
import hashlib
import time
import webcolors as wc

t = str(time.time())
s = t.encode()
hash_object = hashlib.sha256(s)
seed = hash_object.hexdigest()
print(seed)

rnd.seed(seed,version=2)

############## parameters ######################################################
CSIZE = 800
n = 2    # don't change this
cellRad = np.floor(CSIZE/(2*n))

WIDTH = np.arange(0,CSIZE+1)
pts = WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))]


iter = 20


############## drawing #########################################################
d = draw.Drawing(CSIZE,CSIZE)

# initialize the first four circles
init_colors = ['#a2aeb0','#d1c5b0','#916c87','#467c7d','#857999','#bfa782']
# init_colors = ['#ff00ff']
circles = [(pts[0],pts[0],cellRad,rnd.choice(init_colors)),(pts[0],pts[1],cellRad,rnd.choice(init_colors)),(pts[1],pts[0],cellRad,rnd.choice(init_colors)),(pts[1],pts[1],cellRad,rnd.choice(init_colors))]

# now iterate through the list and randomly split them
for i in range(iter):
    split = rnd.choice([0,0,0,1])
    if(split==1):
        ind = rnd.choice([0,len(circles)-1])
        this_circle = circles[ind]
        del(circles[ind])

        this_color = wc.hex_to_rgb(this_circle[3])
        R = int((255-this_color[0])/2)
        G = int((255-this_color[1])/2)
        B = int((255-this_color[2])/2)
        clr = wc.rgb_to_hex((R,G,B))


        x = this_circle[0]
        y = this_circle[1]
        rad = this_circle[2]/2
        # clr = rnd.choice(init_colors)
        q1 = (x+rad,y+rad,rad,clr)
        q2 = (x-rad,y+rad,rad,clr)
        q3 = (x+rad,y-rad,rad,clr)
        q4 = (x-rad,y-rad,rad,clr)
        new_circles = [q1,q2,q3,q4]
        circles = circles + new_circles

# draw the circles
for i in range(len(circles)):
    d.append(draw.Circle(circles[i][0],circles[i][1], circles[i][2], fill=circles[i][3]))

















d.saveSvg('divcircle.svg')
d.savePng('divcircle.png')
