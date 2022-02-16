# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:31:26 2020

@author: mwnew
"""
# Mickie Newman 
#20/01/31
from turtle import *

window = Screen()
window.screensize(600,600)
window.update()

# the colors and lengths used colors found at https://coolors.co/bad1cd-f2d1c9-e086d3-8332ac-462749
colors = ['#BAD1CD','#F2D1C9','#E086D3','#8332AC','#462749']
lengths = [300, 360, 200,]

window.bgcolor(colors[4]) 

# create a pink diamond that is slightly off center to the right
pinkDiamond = Turtle()
pinkDiamond.color(colors[2])
pinkDiamond.width(5)
pinkDiamond.speed(10)
pinkDiamond.begin_fill()
pinkDiamond.up()
pinkDiamond.forward(lengths[2])
pinkDiamond.down()
pinkDiamond.right(135)
pinkDiamond.forward(lengths[1])
pinkDiamond.right(90)
pinkDiamond.forward(lengths[1])
pinkDiamond.right(90)
pinkDiamond.forward(lengths[1])
pinkDiamond.right(90)
pinkDiamond.forward(lengths[1])
pinkDiamond.end_fill()

#create a purple diamond slightly off center to the left
purpleDiamond = Turtle()
purpleDiamond.color(colors[3])
purpleDiamond.width(5)
purpleDiamond.speed(7)
purpleDiamond.begin_fill()
purpleDiamond.up()
purpleDiamond.forward(lengths[0])
purpleDiamond.down()
purpleDiamond.right(135)
purpleDiamond.forward(lengths[1])
purpleDiamond.right(90)
purpleDiamond.forward(lengths[1])
purpleDiamond.right(90)
purpleDiamond.forward(lengths[1])
purpleDiamond.right(90)
purpleDiamond.forward(lengths[1])
purpleDiamond.end_fill()

#create a yellow diamond in the middle of the two other diamonds
yellowDiamond = Turtle()
yellowDiamond.color(colors[1])
yellowDiamond.width(5)
yellowDiamond.speed(3)
yellowDiamond.begin_fill()
yellowDiamond.up()
yellowDiamond.forward(lengths[2])
yellowDiamond.down()
yellowDiamond.right(135)
yellowDiamond.forward(lengths[0])
yellowDiamond.right(90)
yellowDiamond.forward(lengths[0])
yellowDiamond.right(90)
yellowDiamond.forward(lengths[0])
yellowDiamond.right(90)
yellowDiamond.forward(lengths[0]) 
yellowDiamond.end_fill()



         
done()