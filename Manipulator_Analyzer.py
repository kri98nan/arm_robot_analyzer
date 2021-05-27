import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import platform
from PIL import ImageTk,Image

root = Tk(className = ' Manipulator Analyser')
root.geometry('700x665')
photo = PhotoImage(file = r'.\logo.png')
root.iconphoto(False,photo)
root.resizable(False,False)
img = ImageTk.PhotoImage(Image.open("./bgMA2.png")) 
background_label = tk.Label(root, image=img)
background_label.place(x=0, y=0, relwidth = 1, relheight = 1)
color = 'cyan'

def draw_cylinder(radius, height, num_slices,l2=5):
    r2 = radius
    h2 = height
    n2 = float(num_slices)

    r = 1
    if l2 <=5 and l2 >=-5:
        h = 5
    else:
        h = l2
    n = float(20)
    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)
    if l2<-5:
        glBegin(GL_TRIANGLE_FAN)
        glColor(1, 0, 0)
        glVertex(0, 0, 5/2.0)
        for (x, y) in circle_pts:
            z = 5/2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor(0, 0, 1)
        glVertex(0, 0, 5/2.0)
        for (x, y) in circle_pts:
            z = h/2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glColor(0, 1, 0)
        mx = circle_pts[0][0]
        my = circle_pts[0][1]
        for (x, y) in circle_pts:
            z = h/2.0
            glVertex(x,y,z)
            glVertex(x,y,5/2.0)
        
        glEnd()
        circle_link = []
        for i in range(int(n2) + 1):
            angle = 2 * math.pi * (i/n2)
            x = r2 * math.cos(angle)
            y = r2 * math.sin(angle)
            pt = (x,y)
            circle_link.append(pt)
        glBegin(GL_TRIANGLE_STRIP)
        glColor(0, 1, 0)
        for (x, y) in circle_link:
            z = h2/2.0
            glVertex(z/2.0,y,x+(h/2.0)+1.5)
            glVertex(0.5,y,x+(h/2.0)+1.5)


        glEnd()
    elif l2>5:
        glBegin(GL_TRIANGLE_FAN)
        glColor(1, 0, 0)
        glVertex(0, 0, 5/2.0)
        for (x, y) in circle_pts:
            z = h/2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor(0, 0, 1)
        glVertex(0, 0, 5/2.0)
        for (x, y) in circle_pts:
            z = 5/2.0
            glVertex(x, y, z)
        glEnd()
        
        glBegin(GL_TRIANGLE_STRIP)
        glColor(0, 1, 0)
        for (x, y) in circle_pts:
            z = h/2.0
            glVertex(x,y, -5/2.0)
            glVertex(x,y, z)
        glEnd()
        circle_link = []
        glTranslate(0.8, 0, 0)
        for i in range(int(n2) + 1):
            angle = 2 * math.pi * (i/n2)
            x = r2 * math.cos(angle)
            y = r2 * math.sin(angle)
            pt = (x,y)
            circle_link.append(pt)
        glBegin(GL_TRIANGLE_STRIP)
        glColor(0, 1, 0)
        for (x, y) in circle_link:
            z = h2/2.0
            glVertex(z/2.0,y,x+(h/2.0)-1.5)
            glVertex(0,y,x+(h/2.0)-1.5)
        glEnd()



    else:
        glBegin(GL_TRIANGLE_FAN)
        glColor(1, 0, 0)
        glVertex(0, 0, h/2.0)
        for (x, y) in circle_pts:
            z = h/2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor(0, 0, 1)
        glVertex(0, 0, h/2.0)
        for (x, y) in circle_pts:
            z = -h/2.0
            glVertex(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glColor(0, 1, 0)
        for (x, y) in circle_pts:
            z = h/2.0
            glVertex(x,y, z)
            glVertex(x,y, -z)
        glEnd()

        circle_link = []
        for i in range(int(n2) + 1):
            angle = 2 * math.pi * (i/n2)
            x = r2 * math.cos(angle)
            y = r2 * math.sin(angle)
            pt = (x,y)
            circle_link.append(pt)
        glBegin(GL_TRIANGLE_STRIP)
        glColor(0, 1, 0)
        for (x, y) in circle_link:
            z = h2/2.0
            glVertex(z/2.0,y,x)
            glVertex(0.5,y,x)


        glEnd()
        

embed = tk.Frame(root,width=600,height=600)
embed.pack(side=tk.TOP)
    
   
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.init()
icon = pygame.image.load('./logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Graphic Window')
(width, height) = (600,500)
screen = pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)
screen.fill((255,255,255))
clock = pygame.time.Clock()
img1 = ImageTk.PhotoImage(Image.open("./bgMA2.png"))  # PIL solution
background_label1 = tk.Label(embed, image=img1)
background_label1.place(x=0, y=0, relwidth = 1, relheight = 1)




    


def check(*args):
    rotation  = rot.get()
    alpha  = al.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glDisable(GL_BLEND)
    glEnable(GL_DEPTH_TEST)
    glDepthMask(GL_TRUE)
    glDepthFunc(GL_LEQUAL)
    glDepthRange(0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(width)/height, 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(-9, -8, -70)
    try:
        if al.get()<0:
            glRotate(alpha, -al.get(), 0,0)
        else:
            glRotate(alpha, al.get(), 0,0)
        if rotz.get()<0:
            glRotate(rotz.get(), 0, -rotz.get(),0)
        else:
            glRotate(rotz.get(), 0, rotz.get(),0)
        if Checkbutton1.get() == 1:
                glRotate(-90, 1, 0, 0)
    except:
        pass
    
    if rot.get()<0:
        glRotate(rotation, 0, 0, -rot.get())
    else:
        glRotate(rotation, 0, 0, rot.get())
    draw_cylinder(0.5,var.get(), 20,offset.get())
    if int(config_var.get()) >= 2:
        if config_var.get() == 2 or (config_var.get()) >= 2:
            rotation2  = rot2.get()
            alpha2  = al2.get()
            try:
                if al2.get()<0:
                    if d1.get()<=5 and d1.get()>=-5:
                        glTranslate(var.get()/4, 0, 0)
                    elif d1.get()>5 :
                        glTranslate(var.get()/4, 0, (d1.get()/2)-1.5)
                    else:
                        glTranslate(var.get()/4, 0, (d1.get()/2)+1.5)
                    glRotate(alpha2, -al2.get(), 0,0)
                    glRotate(rotation2, 0,0,var2.get())
                else:
                    if d1.get()<=5 and d1.get()>=-5:
                        glTranslate(var.get()/4, 0, 0)
                    elif d1.get()>5 :
                        glTranslate(var.get()/4, 0, (d1.get()/2)-1.5)
                    else:
                        glTranslate(var.get()/4, 0, (d1.get()/2)+1.5)
                    glRotate(alpha2, al2.get(), 0,0)
                    glRotate(rotation2, 0,0,var2.get())
            except:
                pass
            draw_cylinder(0.5,var2.get(), 20,offset2.get())
            if config_var.get() == 3 or (config_var.get()) >= 3:
                rotation3  = rot3.get()
                alpha3  = al3.get()
                try:
                    if al3.get()<0:
                        if d2.get()<=5 and d2.get()>=-5:
                            glTranslate(var2.get()/4, 0, 0)
                        elif d2.get()>5 :
                            glTranslate(var2.get()/4, 0, (d2.get()/2)-1.5)
                        else:
                            glTranslate(var2.get()/4, 0, (d2.get()/2)+1.5)
                        glRotate(alpha3, -al3.get(), 0,0)
                        glRotate(rotation3, 0,0,var3.get())
                        draw_cylinder(0.5,var3.get(), 20,offset3.get())
                    else:
                        if d2.get()<=5 and d2.get()>=-5:
                            glTranslate(var2.get()/4, 0, 0)
                        elif d2.get()>5 :
                            glTranslate(var2.get()/4, 0, (d2.get()/2)-1.5)
                        else:
                            glTranslate(var2.get()/4, 0, (d2.get()/2)+1.5)
                        glRotate(alpha3, al3.get(), 0,0)
                        glRotate(rotation3, 0,0,var3.get())
                        draw_cylinder(0.5,var3.get(), 20,offset3.get())
                except:
                    pass
                if config_var.get() == 4 or (config_var.get()) >= 4:
                    rotation4  = rot4.get()
                    alpha4  = al4.get()
                    try:
                        if al4.get()<0:
                            if d3.get()<=5 and d3.get()>=-5:
                                glTranslate(var3.get()/4, 0, 0)
                            elif d3.get()>5 :
                                glTranslate(var3.get()/4, 0, (d3.get()/2)-1.5)
                            else:
                                glTranslate(var3.get()/4, 0, (d3.get()/2)+1.5)
                            glRotate(alpha4, -al4.get(), 0,0)
                            glRotate(rotation4, 0,0,var4.get())
                        else:
                            if d3.get()<=5 and d3.get()>=-5:
                                glTranslate(var3.get()/4, 0, 0)
                            elif d3.get()>5 :
                                glTranslate(var3.get()/4, 0, (d3.get()/2)-1.5)
                            else:
                                glTranslate(var3.get()/4, 0, (d3.get()/2)+1.5)
                            glRotate(alpha4, al4.get(), 0,0)
                            glRotate(rotation4, 0,0,var4.get())
                    except:
                        pass
                    draw_cylinder(0.5,var4.get(), 20,offset4.get())
                    if config_var.get() == 5 or (config_var.get()) >= 5:
                        rotation5  = rot5.get()
                        alpha5  = al5.get()
                        try:
                            if al5.get()<0:
                                if d4.get()<=5 and d4.get()>=-5:
                                    glTranslate(var4.get()/4, 0, 0)
                                elif d4.get()>5 :
                                    glTranslate(var4.get()/4, 0, (d4.get()/2)-1.5)
                                else:
                                    glTranslate(var4.get()/4, 0, (d4.get()/2)+1.5)
                                glRotate(alpha5, -al5.get(), 0,0)
                                glRotate(rotation5, 0,0,var5.get())
                            else:
                                if d4.get()<=5 and d4.get()>=-5:
                                    glTranslate(var4.get()/4, 0, 0)
                                elif d4.get()>5 :
                                    glTranslate(var4.get()/4, 0, (d4.get()/2)-1.5)
                                else:
                                    glTranslate(var4.get()/4, 0, (d4.get()/2)+1.5)
                                glRotate(alpha5, al5.get(), 0,0)
                                glRotate(rotation5, 0,0,var5.get())
                        except:
                            pass
                        draw_cylinder(0.5,var5.get(), 20,offset5.get())
                        if config_var.get() == 6 or (config_var.get()) >= 6:
                            rotation6  = rot6.get()
                            alpha6  = al6.get()
                            try:
                                if al6.get()<0:
                                    if d5.get()<=5 and d5.get()>=-5:
                                        glTranslate(var5.get()/4, 0, 0)
                                    elif d5.get()>5 :
                                        glTranslate(var5.get()/4, 0, (d5.get()/2)-1.5)
                                    else:
                                        glTranslate(var5.get()/4, 0, (d5.get()/2)+1.5)
                                    glRotate(alpha6, -al6.get(), 0,0)
                                    glRotate(rotation6, 0,0,var6.get())
                                else:
                                    if d5.get()<=5 and d5.get()>=-5:
                                        glTranslate(var5.get()/4, 0, 0)
                                    elif d5.get()>5 :
                                        glTranslate(var5.get()/4, 0, (d5.get()/2)-1.5)
                                    else:
                                        glTranslate(var5.get()/4, 0, (d5.get()/2)+1.5)
                                    glRotate(alpha6, al6.get(), 0,0)
                                    glRotate(rotation6, 0,0,var6.get())
                            except:
                                pass
                            draw_cylinder(0.5,var6.get(), 20,offset6.get())

    

    

    
    pygame.display.flip()
    clock.tick(60)








config_var= IntVar(root, "1")
values = {"2 Joint Manipulator" : "2", 
          "3 Joint Manipulator" : "3", 
          "4 Joint Manipulator" : "4", 
          "5 Joint Manipulator" : "5", 
          "6 Joint Manipulator" : "6"}

i = 0
for (text, value) in values.items(): 
    Radiobutton(root, text = text, variable = config_var,value = value,bg=color).place(x = 510,y = 60+i)
    i = i+40

config_var.trace_variable('w',check)


Label(root, text = "Joint-1:", font = ("Times New Roman", 11), bg = color).place(x=10,y=20)
Label(root, text = 'a\u2081:', font = ("Times New Roman", 11), bg = color).place(x=10,y=63)

var = DoubleVar()
w = Scale(root, from_=0, to=25, orient=HORIZONTAL,variable = var)
w.place(x=30,y=45)
var.trace_variable('w',check) 
aj1 = ttk.Combobox(root, width = 3, textvariable = var)
aj1['values'] = (0,5,10,15,20)
aj1.place(x = 140, y = 64)


Label(root, text = 'θ\u2081:', font = ("Times New Roman", 11), bg = color).place(x=10,y=103)
rot = DoubleVar()
r = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = rot)
r.place(x=30,y=85)
rot.trace_variable('w',check) 
thetaj1 = ttk.Combobox(root, width = 3, textvariable = rot)
thetaj1['values'] = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360)
thetaj1.place(x = 140, y = 104)

Label(root, text = "Rotational View:", font = ("Times New Roman", 11), bg = 'SeaGreen1').place(x=570,y=555)
Label(root, text = 'X:', font = ("Times New Roman", 11), bg = 'SeaGreen1').place(x=570,y=598)
al = DoubleVar()
alph = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = al, bg = 'SeaGreen1')
alph.place(x=590,y=580)
al.trace_variable('w',check)

Label(root, text = 'Y:', font = ("Times New Roman", 11), bg = 'SeaGreen1').place(x=570,y=638)
rotz = DoubleVar()
rz = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = rotz, bg = 'SeaGreen1')
rz.place(x=590,y=620)
rotz.trace_variable('w',check)

Label(root, text = 'α\u2081:', font = ("Times New Roman", 11), bg = color).place(x=10,y=143)
al2 = DoubleVar()
alph2 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = al2)
alph2.place(x=30,y=125)
al2.trace_variable('w',check)
twistj1 = ttk.Combobox(root, width = 3, textvariable = al2)
twistj1['values'] = (0,-270,-180,-90,90,180,270)
twistj1.place(x = 140, y = 144)


Label(root, text = "d\u2081:", font = ("Times New Roman", 11), bg = color).place(x=10,y=183)
offset = DoubleVar()
d1 = Scale(root, from_=-25, to=25, orient=HORIZONTAL,variable = offset)
d1.place(x=30,y=165)
offset.trace_variable('w',check)
offj1 = ttk.Combobox(root, width = 3, textvariable = offset)
offj1['values'] = (0,-5,-10,-15,-20,5,10,15,20)
offj1.place(x = 140, y = 184)





Label(root, text = "Joint-2:", font = ("Times New Roman", 11), bg = color).place(x=10,y=225)
Label(root, text = "a\u2082:", font = ("Times New Roman", 11), bg = color).place(x=10,y=268)

var2 = DoubleVar()
w2 = Scale(root, from_=0, to=25, orient=HORIZONTAL,variable = var2)
w2.place(x=30,y=250)
var2.trace_variable('w',check)
aj2 = ttk.Combobox(root, width = 3, textvariable = var2)
aj2['values'] = (0,5,10,15,20)
aj2.place(x = 140, y = 269)



Label(root, text = "θ\u2082:", font = ("Times New Roman", 11), bg = color).place(x=10,y=308)
rot2 = DoubleVar()
r2 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = rot2)
r2.place(x=30,y=290)
rot2.trace_variable('w',check) 
thetaj2 = ttk.Combobox(root, width = 3, textvariable = rot2)
thetaj2['values'] = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360)
thetaj2.place(x = 140, y = 309)

Label(root, text = "α\u2082:", font = ("Times New Roman", 11), bg = color).place(x=10,y=348)
al3 = DoubleVar()
alph3 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = al3)
alph3.place(x=30,y=330)
al3.trace_variable('w',check)
twistj2 = ttk.Combobox(root, width = 3, textvariable = al3)
twistj2['values'] = (0,-270,-180,-90,90,180,270)
twistj2.place(x = 140, y = 349)



Label(root, text = "d\u2082:", font = ("Times New Roman", 11), bg = color).place(x=10,y=388)
offset2 = DoubleVar()
d2 = Scale(root, from_=-25, to=25, orient=HORIZONTAL,variable = offset2)
d2.place(x=30,y=370)
offset2.trace_variable('w',check)
offj2 = ttk.Combobox(root, width = 3, textvariable = offset2)
offj2['values'] = (0,-5,-10,-15,-20,5,10,15,20)
offj2.place(x = 140, y = 389)



Label(root, text = "Joint-3:", font = ("Times New Roman", 11), bg = color).place(x=10,y=430)
Label(root, text = "a\u2083:", font = ("Times New Roman", 11), bg = color).place(x=10,y=473)


var3 = DoubleVar()
w3 = Scale(root, from_=0, to=25, orient=HORIZONTAL,variable = var3)
w3.place(x=30,y=455)
var3.trace_variable('w',check) 
aj3 = ttk.Combobox(root, width = 3, textvariable = var3)
aj3['values'] = (0,5,10,15,20)
aj3.place(x = 140, y = 474)


Label(root, text = "θ\u2083:", font = ("Times New Roman", 11), bg = color).place(x=10,y=513)
rot3 = DoubleVar()
r3 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = rot3)
r3.place(x=30,y=495)
rot3.trace_variable('w',check) 
thetaj3 = ttk.Combobox(root, width = 3, textvariable = rot3)
thetaj3['values'] = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360)
thetaj3.place(x = 140, y = 514)



Label(root, text = "α\u2083:", font = ("Times New Roman", 11), bg = color).place(x=10,y=553)
al4 = DoubleVar()
alph4 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = al4)
alph4.place(x=30,y=535)
al4.trace_variable('w',check)
twistj3 = ttk.Combobox(root, width = 3, textvariable = al4)
twistj3['values'] = (0,-270,-180,-90,90,180,270)
twistj3.place(x = 140, y = 554)


Label(root, text = "d\u2083:", font = ("Times New Roman", 11), bg = color).place(x=10,y=593)
offset3 = DoubleVar()
d3 = Scale(root, from_=-25, to=25, orient=HORIZONTAL,variable = offset3)
d3.place(x=30,y=575)
offset3.trace_variable('w',check)
offj3 = ttk.Combobox(root, width = 3, textvariable = offset3)
offj3['values'] = (0,-5,-10,-15,-20,5,10,15,20)
offj3.place(x = 140, y = 594)




Label(root, text = "Joint-4:", font = ("Times New Roman", 11), bg = color).place(x=260,y=20)
Label(root, text = "a\u2084:", font = ("Times New Roman", 11), bg = color).place(x=260,y=63)
var4 = DoubleVar()
w4 = Scale(root, from_=0, to=25, orient=HORIZONTAL,variable = var4)
w4.place(x=280,y=45)
var4.trace_variable('w',check)
aj4 = ttk.Combobox(root, width = 3, textvariable = var4)
aj4['values'] = (0,5,10,15,20)
aj4.place(x = 390, y = 64)


Label(root, text = "θ\u2084:", font = ("Times New Roman", 11), bg = color).place(x=260,y=103)
rot4 = DoubleVar()
r4 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = rot4)
r4.place(x=280,y=85)
rot4.trace_variable('w',check)
thetaj4 = ttk.Combobox(root, width = 3, textvariable = rot4)
thetaj4['values'] = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360)
thetaj4.place(x = 390, y = 104)




Label(root, text = "α\u2084:", font = ("Times New Roman", 11), bg = color).place(x=260,y=143)
al5 = DoubleVar()
alph5 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = al5)
alph5.place(x=280,y=125)
al5.trace_variable('w',check)
twistj4 = ttk.Combobox(root, width = 3, textvariable = al5)
twistj4['values'] = (0,-270,-180,-90,90,180,270)
twistj4.place(x = 390, y = 144)



Label(root, text = "d\u2084:", font = ("Times New Roman", 11), bg = color).place(x=260,y=183)
offset4 = DoubleVar()
d4 = Scale(root, from_=-25, to=25, orient=HORIZONTAL,variable = offset4)
d4.place(x=280,y=165)
offset4.trace_variable('w',check) 
offj4 = ttk.Combobox(root, width = 3, textvariable = offset4)
offj4['values'] = (0,-5,-10,-15,-20,5,10,15,20)
offj4.place(x = 390, y = 184)




Label(root, text = "Joint-5:", font = ("Times New Roman", 11), bg = color).place(x=260,y=225)
Label(root, text = "a\u2085:", font = ("Times New Roman", 11), bg = color).place(x=260,y=268)
var5 = DoubleVar()
w5 = Scale(root, from_=0, to=25, orient=HORIZONTAL,variable = var5)
w5.place(x=280,y=250)
var5.trace_variable('w',check)
aj5 = ttk.Combobox(root, width = 3, textvariable =var5)
aj5['values'] = (0,5,10,15,20)
aj5.place(x = 390, y = 269)





Label(root, text = "θ\u2085:", font = ("Times New Roman", 11), bg = color).place(x=260,y=308)
rot5 = DoubleVar()
r5 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = rot5)
r5.place(x=280,y=290)
rot5.trace_variable('w',check)
thetaj5 = ttk.Combobox(root, width = 3, textvariable = rot5)
thetaj5['values'] = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360)
thetaj5.place(x = 390, y = 309)


Label(root, text = "α\u2085:", font = ("Times New Roman", 11), bg = color).place(x=260,y=348)
al6 = DoubleVar()
alph6 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = al6)
alph6.place(x=280,y=330)
al6.trace_variable('w',check)
twistj5 = ttk.Combobox(root, width = 3, textvariable = al6)
twistj5['values'] = (0,-270,-180,-90,90,180,270)
twistj5.place(x = 390, y = 349)


Label(root, text = "d\u2085:", font = ("Times New Roman", 11), bg = color).place(x=260,y=388)
offset5 = DoubleVar()
d5 = Scale(root, from_=-25, to=25, orient=HORIZONTAL,variable = offset5)
d5.place(x=280,y=370)
d5.set(5)
offset5.trace_variable('w',check)
offj5 = ttk.Combobox(root, width = 3, textvariable = offset5)
offj5['values'] = (0,-5,-10,-15,-20,5,10,15,20)
offj5.place(x = 390, y = 389)



Label(root, text = "Joint-6:", font = ("Times New Roman", 11), bg = color).place(x=260,y=430)
Label(root, text = "a\u2086:", font = ("Times New Roman", 11), bg = color).place(x=260,y=473)
var6 = DoubleVar()
w6 = Scale(root, from_=0, to=25, orient=HORIZONTAL,variable = var6)
w6.place(x=280,y=455)
var6.trace_variable('w',check)
aj6 = ttk.Combobox(root, width = 3, textvariable = var6)
aj6['values'] = (0,5,10,15,20)
aj6.place(x = 390, y = 474)



Label(root, text = "θ\u2086:", font = ("Times New Roman", 11), bg = color).place(x=260,y=513)
rot6 = DoubleVar()
r6 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = rot6)
r6.place(x=280,y=495)
rot6.trace_variable('w',check)
thetaj6 = ttk.Combobox(root, width = 3, textvariable = rot6)
thetaj6['values'] = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360)
thetaj6.place(x = 390, y = 514)


Label(root, text = "α\u2086:", font = ("Times New Roman", 11), bg = color).place(x=260,y=553)
al7 = DoubleVar()
alph7 = Scale(root, from_=-360, to=360, orient=HORIZONTAL,variable = al7)
alph7.place(x=280,y=535)
al7.trace_variable('w',check)
twistj6 = ttk.Combobox(root, width = 3, textvariable = al7)
twistj6['values'] = (0,-270,-180,-90,90,180,270)
twistj6.place(x = 390, y = 554)



Label(root, text = "d\u2086:", font = ("Times New Roman", 11), bg = color).place(x=260,y=593)
offset6 = DoubleVar()
d6 = Scale(root, from_=-25, to=25, orient=HORIZONTAL,variable = offset6)
d6.place(x=280,y=575)
offset6.trace_variable('w',check)
offj6 = ttk.Combobox(root, width = 3, textvariable = offset6)
offj6['values'] = (0,-5,-10,-15,-20,5,10,15,20)
offj6.place(x = 390, y = 594)




Checkbutton1 = IntVar()
j1twist = Checkbutton(root, text = "Change Joint-1 Vertical",variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 1,bg=color)
j1twist.place(x=510,y=400)






root.mainloop()












