### Fibonacci apples designs, by Henry Segerman http://segerman.org 
### 17/07/15

### This python code produces a design of apple logos for lasering on your macbook.
### The pattern includes an apple where the backlit apple logo is, so that the backlit apple
### fits into the pattern. REMEMBER TO DELETE THE CENTRAL APPLE BEFORE LASERING YOUR LAPTOP!

### Unfortunately, this code produces very large .eps files. Opening them in a vector graphics 
### program (e.g. Adobe Illustrator) takes a while, but then saving to .pdf makes the files
### much more manageable. For testing purposes, have the code generate a smaller number of apples.

### Process:
### 1) Play with the settings to get whatever effect you want. Don't use a design that has any apples
###    overlapping with the central apple logo, since you will likely end up lasering through the 
###    backlit apple logo that's already on your laptop.
### 2) Open the .eps file in a vector graphics program and set the artboard size to the 
###    dimensions of your laser etcher. Save a copy as a pdf.
### 3) Save a second copy of the file, having deleted the central apple and the border rectangle.
### 4) Position your laptop in the laser etcher using the first pdf (so you can use the non-cutting
###    "line things up" laser on the cutter to position the laptop correctly, matching with the 
###    border rectangle and the central apple)
### 5) If the central apple isn't lining up well with the border rectangle, play with the 
###    center_apple_offset variable below to shift them relative to each other. 
### 6) Once everything is lined up, switch to the second pdf (which won't laser through the backlit
###    apple and destroy your laptop).
### 7) For that matter, maybe it would be a good idea to put a small sheet of something durable over
###    the backlit apple logo before you laser anything.
### 8) Get the "material thickness" settings correct so that the laser focuses on the top surface of
###    your laptop. For mackbook airs, you will need to prop up the front so that the surface doesn't
###    slope.
### 9) Laser away!

### Use this code and the designs produced by it at your own risk. I take no responsibility if you 
### accidentally (or deliberately) destroy your laptop with lasers.

from pyx import *  ### vector graphics library
from math import *

def offset_insert(can, pos, filename, scl): 
    can.insert(epsfile.epsfile(pos[0] - 0.5 * scl, pos[1] -0.5 * scl, filename, scale = scl))

def get_rad(t, k, alpha, init_rad):
    return init_rad*((t + k))**(1/(2.0-alpha))

def get_scl(radius, alpha):
    return sqrt(radius**alpha)  #magic here to keep average apple density constant

def get_pos(radius, t, center_t, offset_angle, offset_pos):
    return [-radius * sin(t-center_t+offset_angle) + offset_pos[0], radius * cos(t-center_t+offset_angle) + offset_pos[1]]  #center_t points straight up, unless modified by offset angle

c = canvas.canvas()

phi2pi = pi * (sqrt(5) - 1)
bleed = 2.54*0.1 #0.1 inches

center_apple_offset = [0, 0]  #might be worth messing with this if the apple logo is offset relative to the border rectangle

#### example settings ----
alpha = -17.9  
init_rad = 2.54*10.2
center_index = 12
offset_angle = -pi*0.2
range_width = 300000
k = -center_index
start_num = center_index
# -----

center_t = center_index * phi2pi  
center_rad = get_rad(center_t, k, alpha, init_rad)
center_scl = get_scl(center_rad, alpha) ##this is scale before we normalise
normalise_scl = 2.54*1.5/center_scl ##scale everything up by this to get 1.5inch wide central logo, seems to be about correct in 2015

true_center = get_pos(center_rad, center_t, center_t, offset_angle, [0,0])  ##different from center if there is an offset
center = get_pos(center_rad, center_t, center_t, offset_angle, center_apple_offset)

### --- 15 inch mbp retina 2015 (look up specs online, or measure yourself)
rect_width = 2.54*14.13 #inches wide
rect_height = 2.54*9.73 #inches high

### --- 13 inch mb air 2015 (note the air slopes, so needs to be propped up to give a horizontal surface for the laser)
# rect_width = 2.54*12.8 #inches wide
# rect_height = 2.54*8.94 #inches high

p,q,r,s = true_center[0] - rect_width*0.5, true_center[1] - rect_height*0.5, true_center[0] + rect_width*0.5, true_center[1] + rect_height*0.5
boundary_rect = path.rect(p,q,r-p,s-q)
c.stroke(boundary_rect) #draw a rectangle for the edges of the laptop

range_start = 0
# range_width = 100   ###useful to test a design without making an enormous .eps file

count = 0
scales = []
radii = []
for i in range(start_num+range_start, start_num+range_start+range_width):  
    t = i * phi2pi
    radius = get_rad(t, k, alpha, init_rad)
    x,y = get_pos(radius, t, center_t, offset_angle, center_apple_offset)
    scl = get_scl(radius,alpha) * normalise_scl
    if p - 0.5*scl - bleed < x < r + 0.5*scl + bleed and q - 0.5*scl - bleed < y < s + 0.5*scl + bleed:  
        count += 1
        radii.append(radius)
        scales.append(scl)
        offset_insert(c, [x,y], "apple_logo.eps", scl)
print 'done inserts:', count
print 'min, max scl in mm:', 10*min(scales), 10*max(scales)
print 'min, max rad in mm:', 10*min(radii), 10*max(radii)
c.writeEPSfile("output")
print 'done saving'
