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
n = 50
cellRad = np.floor(CSIZE/(2*n))

WIDTH = np.arange(0,CSIZE+1)
pts = np.array(WIDTH[int(np.round(cellRad))::int(np.round(2*cellRad))])

perturb = np.random.normal(0,n*2, len(pts))
pts1 = pts+perturb

perturb = np.random.normal(0,CSIZE/10, len(pts))
pts2 = pts+perturb



############## drawing #########################################################

d = draw.Drawing(CSIZE,CSIZE)


for i in range(len(pts)):
    for j in range(len(pts)):










d.saveSvg('droop.svg')
