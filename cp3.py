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
        
        
        turtle.forward(self.dwidth/2)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth/2)
        
        turtle.end_fill()
    
    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        self.showdisk()
    
    def cleardisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()
        turtle.fillcolor("white") 
        turtle.begin_fill()
        turtle.color("white")
        
         
        turtle.forward(self.dwidth/2)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth/2)
        
        turtle.end_fill() 
        turtle.color("black")  
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
        self.toppos += disk.dheight
        self.stack.append(disk)
        disk.showdisk()
        
    def popdisk(self):
        disk = self.stack.pop()
        disk.newpos(self.pxpos, self.toppos)
        self.toppos -= disk.dheight
        disk.cleardisk()
        return disk



class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)*30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)


if __name__ == "__main__":
    turtle.speed(100)  
    disk1 = Disk("d1", 0, 0, 20, 40)
    pole1 = Pole("A", 0, 0)
    pole1.showpole()
    pole1.pushdisk(disk1)
    pole1.popdisk()

    h = Hanoi()
    h.solve()
    
    turtle.done()  



