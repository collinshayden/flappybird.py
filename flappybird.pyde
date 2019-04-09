import random
Pole1X=0
Pole1Y=0
Pole2X=0
Pole2Y=0
BirdX=0
BirdY=0
class pole(object):#creates class
    def __init__(self,x,y,w,h,speed):#constructor with inputs
        self.r = random.randint(100,180)#chooses random int between 100,180
        self.x = x+w#makes the pole start off screen
        self.y = y
        self.y2 = 500-self.r
        self.w = w
        self.h = self.r#sets random height
        self.speed = speed
    
    def move(self):#needs to call self as first instance
        self.x += self.speed#similar to this. in JS
        if(self.x<-self.w):#if x goes past 0-width of pole
            self.r = random.randint(100,250)#make another random integer
            self.h=self.r#set the height as that int
            self.x = 500+self.w#move the pole back off screen
            
    def display(self):
        stroke(0)#stroke color = black
        strokeWeight(1.5)#strokeweight
        fill(255,0,0)#fill RGB
        rect(self.x,self.y,self.w,self.h)
        rect(self.x,self.y2,self.w,self.h+75)

class bird(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def move(self):
        self.y+=4
        if(keyPressed):
            self.y-=15  

    def display(self):
        fill(0,0,255)
        rect(self.x,self.y,self.w,self.h)


Pole1 = pole(500,0,50,150,-3)#x,y,w,h,speed
Pole2 = pole(800,0,50,150,-3)
Bird = bird(50,250,20,20)#x,y,w,h

def endgame():
    noLoop()
    
def collision():
    #if bird hits pole 1:
    if((Bird.x>Pole1.x and Bird.y>Pole1.y and Bird.y<Pole1.y+Pole1.h) or (Bird.x>Pole1.x and Bird.y>Pole1.y2 and Bird.y<Pole1.y2+Pole1.h)):
        print('hit pole 1')
        endgame()
        
    #if bird hits pole 2
    if((Bird.x>Pole2.x and Bird.y>Pole2.y and Bird.y<Pole2.y+Pole2.h) or (Bird.x>Pole2.x and Bird.y>Pole2.y2 and Bird.y<Pole2.y2+Pole2.h)):
        print('hit pole 2')
        endgame()
    #if bird hits top or bottom of canvas:
    if(Bird.y<0 or Bird.y>500-Bird.w):
        print('hit top/bottom')
        endgame()
def setup():
    size(500,500)

def draw(): 
    background(200)
    pole.move(Pole1)
    pole.display(Pole1)
    pole.move(Pole2)
    pole.display(Pole2)
    bird.move(Bird)
    bird.display(Bird)
    collision()
    
