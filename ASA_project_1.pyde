from vehicle import Vehicle
from flock import Flock
from setting import *

flock1 = Flock()
flock2 = Flock()

d_r_6 = Flock()
d_l_7 = Flock()
m_r_7 = Flock()
m_l_2 = Flock()
m_d_3 = Flock()
l_d_4 = Flock()
d_stay_1 = Flock()
m_stary_1 = Flock()

def setup():
    size(1600, 800)
    
    for i in range(7):
        v = (Vehicle(1560 - i*100, 650 + i*3))
        d_l_7.addBoid(v)
    
    for i in range(6):
        v = (Vehicle(100 + i*100, 680 + i*3))
        d_r_6.addBoid(v)
    
    for i in range(7):
        v = (Vehicle(250 + i*100, 250 + i*3))
        m_r_7.addBoid(v)
        
    for i in range(2):
        v = (Vehicle(1200, 300 + i*3))
        m_l_2.addBoid(v)    
    
    for i in range(3):
        v = (Vehicle(750 + i*3, 150 + i*3))
        m_d_3.addBoid(v)
        
    for i in range(4):
        v = (Vehicle(1050 + i*3, 200 + i*3))
        l_d_4.addBoid(v)
    
    for i in range(1):
        v = (Vehicle(750 + i*3, 600 + i*3))
        d_stay_1.addBoid(v)

    for i in range(1):
        v = (Vehicle(500 + i*3, 230 + i*3))
        m_stary_1.addBoid(v)


    for i in range(3):
        v = (Vehicle(20 + i*3, 30 + i*3))
        flock1.addBoid(v)
    
    for i in range(5):
        v = (Vehicle(50 + i*3, 700 + i*3))
        flock2.addBoid(v)
    
    
def draw():
    
    background(255)
    fill(255, 204, 0)
    rect(100, 0, 10, 150)
    rect(100, 250, 10, 300)
    rect(100, 750, 10, 50)
    
    beginShape()
    vertex(200, 0)
    vertex(200, 50)
    vertex(400, 50)
    vertex(400, 150)
    vertex(600, 200)
    vertex(600, 0)
    endShape()
    
    rect(1200, 0, 400, 200, 20)
    rect(400, 700, 300, 100, 20)
    rect(825, 700, 300, 100, 20)
    rect(1250, 700, 300, 100, 20)
    rect(400, 400, 50, 100, 20)
    rect(600, 400, 80, 100, 20)
    rect(800, 400, 80, 100, 20)
    rect(1000, 400, 50, 100, 20)
    rect(1250, 400, 200, 100, 20)
    rect(200, 700, 20, 10, 20)
    rect(280, 700, 20, 10, 20)
    rect(400, 600, 20, 20, 20)
    rect(650, 600, 20, 20, 40)
    rect(825, 600, 20, 20, 40)
    rect(1105, 600, 20, 20, 40)
    rect(1250, 600, 20, 20, 40)
    rect(1430, 600, 20, 20, 40)
    rect(200, 600, 100, 80, 40)
    

    mouse = PVector(mouseX, mouseY)
    fill(200)
    stroke(0)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)

    flock1.run(target=mouse, color_int=0)
    #flock2.run(target=PVector(1600, 650), color_int=200)
    
    d_l_7.run(target=PVector(0, 700), color_int=204)
    d_r_6.run(target=PVector(1600, 700), color_int=128)
    m_r_7.run(target=PVector(1600, 200), color_int=153)
    m_l_2.run(target=PVector(1, 650), color_int=102)
    m_d_3.run(target=PVector(750, 800), color_int=255)
    l_d_4.run(target=PVector(1150, 800), color_int=51)
    d_stay_1.run(target=PVector(750, 600), color_int=32)
    m_stary_1.run(target=PVector(500, 230), color_int=32)
