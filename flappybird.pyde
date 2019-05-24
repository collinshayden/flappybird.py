import random #imports random library
numScore = 0#assigns numScore to 0

class pole(object):#creates class
    def __init__(self,x):#constructor with inputs
        self.spacing = 125#base distance between top and bottom rects
        self.ran = random.randint(self.spacing, 500 - self.spacing);#random int to determine distance
    
        self.top = self.ran - self.spacing/2#this is the height of top rect
        self.bottom = 500 - (self.ran + self.spacing)#this is the height of bottom rect
        
        self.x = x#sets x to x from when the object is created
        self.w = 80#width
        self.speed = -3#speed of poles
    
    def move(self):#needs to call self as first instance  
        self.x += self.speed#similar to this. in JS
        if(self.x<-self.w):#if x goes past 0-width of pole
            #choses a new random space between top and bottom
            self.ran = random.randint(self.spacing, 500 - self.spacing/2);#make another random integer
            self.top = self.ran - self.spacing/2#
            self.bottom = 500 - (self.ran + self.spacing)
            
            self.x = 500+self.w#move the pole back off screen
            
    def display(self):
        stroke(0)#stroke color = black
        strokeWeight(1.5)#strokeweight
        fill(255,0,0)#fill RGB
        rect(self.x,0,self.w,self.top)#x,y,w,h
        rect(self.x,500-self.bottom,self.w,self.bottom)#x,y,w,h

class bird(object):
    def __init__(self,x,y,w,h):
        #sets class variables(local)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def move(self):
        self.y+=3#sets bird to fall at 4px/loop
        if(keyPressed):#if any key is pressed
            self.y-=15#bird goes up 15px  

    def display(self):
        fill(0,0,255)#blue
        ellipse(self.x,self.y,self.w,self.h)#circle
        
Pole = pole(500)#x,y,w,h,speed
Pole2 = pole(850)#x,y,w,h,speed
Bird = bird(50,250,20,20)#x,y,w,h

def endgame():#function when bird dies
    Bird.y = 250#resets bird y to start pos
    global numScore#calls global var 
    numScore = 0#resets score
    Pole.x = 500#resets first pole to off screen
    Pole2.x = 850#resets second pole to off screen
    
def collision():
    #if bird hits pole:
    if(Bird.x>Pole.x and Bird.x<Pole.x+Pole.w and Bird.y>0 and Bird.y<Pole.top or Bird.x>Pole.x and Bird.y<500 and Bird.y>500-Pole.bottom):
        print('hit pole')
        endgame()#calls endgame function
        
    #if bird hits second pole
    if(Bird.x>Pole2.x and Bird.x<Pole2.x+Pole2.w and Bird.y>0 and Bird.y<Pole2.top or Bird.x>Pole2.x and Bird.y<500 and Bird.y>500-Pole2.bottom):
        print('hit pole')
        endgame()#calls endgame function
        
    #if bird hits top or bottom of canvas:
    if(Bird.y<0 or Bird.y>500-Bird.w):
        print('hit top/bottom')
        endgame()
        
def score():
    fill(0,0,255)#blue
    textSize(32)#sets size of text
    text("score:",0,25)#displays "score:"
    global numScore#calls global var
    text(numScore,100,27)#displays numScore
#if the bird passes a pole:
    if(Bird.x>Pole.x-2 and Bird.x<Pole.x+2 or Bird.x>Pole2.x-2 and Bird.x<Pole2.x+2):
        print(numScore)#print the score
        numScore += 1#add one to the score

def setup():
    size(500,500)#canvas size
def draw(): 
    background(200)
    #calling class methods
    pole.move(Pole)
    pole.display(Pole)
    pole.move(Pole2)
    pole.display(Pole2)
    bird.move(Bird)
    bird.display(Bird)
    #calling functions
    collision()
    score()
    
