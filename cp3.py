import turtle

class Disk(object):
    def __init__(self, name, xpos, ypos, height, width):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    
    def showdisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()
        turtle.fillcolor("blue")  
        turtle.begin_fill()
        
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        
        turtle.end_fill()
    
    def newpos(self, xpos, ypos):
        self.cleardisk()
        self.dxpos = xpos
        self.dypos = ypos
        self.showdisk()
    
    def cleardisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()
        turtle.fillcolor("white") 
        turtle.begin_fill()
        
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        
        turtle.end_fill()

class Pole():
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.toppos = 0
        self.stack = []
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
    
    def showpole(self):
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.pendown()
        turtle.fillcolor("grey") 
        turtle.begin_fill()
        
        for _ in range(2):
            turtle.forward(self.pthick)
            turtle.left(90)
            turtle.forward(self.plength)
            turtle.left(90)
        
        turtle.end_fill()

    def pushdisk(self, disk):
        disk.newpos(self.pxpos, self.toppos)
        self.stack.append(disk)
        self.toppos += disk.dheight
    

if __name__ == "__main__":
    turtle.speed(1)  
    disk1 = Disk("d1", 0, 0, 20, 40)
    disk1.showdisk()
    disk1.newpos(50, 50)
    disk1.cleardisk()
    turtle.done()  
