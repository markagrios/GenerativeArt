import numpy as np
import random as rnd

def draw_circle(svg, refpt, size, fillclr,strclr):

    obj = svg.Circle(refpt[0], refpt[1], size, fill=fillclr, fill_opacity=0.2, stroke=strclr, stroke_width=4)

    ang = 2*np.pi*np.random.random()
    newpt = [refpt[0]+(size*np.cos(ang)), refpt[1]+(size*np.sin(ang))]

    return (obj,newpt)


def draw_triangle(svg, refpt, size, fillclr,strclr):
    scale1 = np.random.random()
    scale2 = np.random.random()
    pt2 = [refpt[0]+(size*(0.2+scale1)), refpt[1]+(size*(1-scale2))]
    pt3 = [refpt[0]+(size*(1-scale1)), refpt[1]+(size*(0.2+scale2))]

    obj = svg.Lines(refpt[0],refpt[1], pt2[0],pt2[1], pt3[0],pt3[1], close=True, fill=fillclr, fill_opacity=0.2, stroke_width=4, stroke=strclr)

    newpt = rnd.choice([pt2,pt3])

    return (obj,newpt)
