import drawSvg as draw
import numpy as np
import random as rnd
import hashlib
import time
from construct_utils import *

t = str(time.time())
s = t.encode()
hash_object = hashlib.sha256(s)
seed = hash_object.hexdigest()
print(seed)

rnd.seed(seed,version=2)

############## parameters ######################################################
CSIZE = 800
iter = 10

strokeWidths = [1,1,1,2,2,2,2,2,3,3,3,6,6,10]
strokeColors = ['#000000','#f5bc2c','#c4375f']
fillColors = ['#fcc2d3','#c0faea','#af91ed']



func_dict = {0:draw_circle,1:draw_triangle}

############## drawing #########################################################
d = draw.Drawing(CSIZE,CSIZE)

thispoint = [CSIZE/2,CSIZE/2]
for i in range(iter):

    func = rnd.choice(func_dict)
    strclr = rnd.choice(strokeColors)
    fillclr = rnd.choice(fillColors)
    sz = rnd.randint(30,100)

    (fig,newpt) = func(draw, thispoint, sz, fillclr, strclr)
    d.append(fig)
    thispoint = [np.mod(newpt[0],CSIZE),np.mod(newpt[1],CSIZE)]


# func_dict = {0:draw_circle,1:draw_triangle}
# (a,b) = func_dict[1](draw, [0,0], 100, '#000000', '#000000')
# d.append(a)

# (f1,p1) = draw_triangle(draw, [0,0], 400, '#000000', '#000000')
# (f2,p2) = draw_circle(draw, p1, 20, '#000000', '#000000')
#
# d.append(f1)
# d.append(f2)

# (a,b) = draw_circle(draw, [0,0], 20, '#000000', '#000000')
# (a2,b2) = draw_circle(draw, b, 20, '#000000', '#000000')
# print(b)
# d.append(a)
# d.append(a2)



















d.saveSvg('construct.svg')
