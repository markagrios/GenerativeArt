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
rows = 100

h = HEIGHT/rows

colors = ['#ffffff','#ff00ff','#ffff00','#00ffff','#000000']
color1 = webcolors.hex_to_rgb(rnd.choice(colors))
color2 =  webcolors.hex_to_rgb(rnd.choice(colors))
# color1 =  webcolors.hex_to_rgb('#ffffff')
# color2 =  webcolors.hex_to_rgb('#ff00ff')

amp = 100 + rnd.randint(-20,20)
# amp = WIDTH/20
per = rnd.random()/10

# gap = WIDTH/15
gap = 0

# print(x)
# print(y1)
########### drawing ############################################################
d = draw.Drawing(WIDTH,HEIGHT)


# d.append(draw.Rectangle(100,300, 200,200, fill='black'))


for i in range(rows):
    # the first side of the wave
    cells = rnd.randint(10,25)

    # create gradient and colormap
    Rlinspace = np.linspace(color1[0],color2[0],cells).astype(int)
    Glinspace = np.linspace(color1[1],color2[1],cells).astype(int)
    Blinspace = np.linspace(color1[2],color2[2],cells).astype(int)

    endX = amp*np.sin(per*i)+(WIDTH/2)
    x = np.arange(0,endX)
    corners = np.sort(np.random.choice(x,cells))

    for c in range(cells):
        this_color = webcolors.rgb_to_hex((Rlinspace[c],Glinspace[c],Blinspace[c]))
        bl = np.array([corners[c],i*h])
        dims = [2*h,h]
        clr = colors[np.mod(i,2)]
        d.append(draw.Rectangle(bl[0],bl[1], dims[0],dims[1], fill=this_color, fill_opacity=1.0))


    # the second side of the wave
    cells = rnd.randint(10,25)

    # create gradient and colormap
    Rlinspace = np.linspace(color2[0],color1[0],cells).astype(int)
    Glinspace = np.linspace(color2[1],color1[1],cells).astype(int)
    Blinspace = np.linspace(color2[2],color1[2],cells).astype(int)

    # endX = amp*np.sin(per*i)+(WIDTH/2)
    endX = WIDTH
    x = np.arange(amp*np.sin(per*i)+(WIDTH/2) + gap,endX)
    corners = np.sort(np.random.choice(x,cells))

    for c in range(cells):
        this_color = webcolors.rgb_to_hex((Rlinspace[c],Glinspace[c],Blinspace[c]))
        bl = np.array([corners[c],i*h])
        dims = [2*h,h]
        clr = colors[np.mod(i,2)]
        d.append(draw.Rectangle(bl[0],bl[1], dims[0],dims[1], fill=this_color, fill_opacity=1.0))








d.saveSvg('rectwave.svg')
