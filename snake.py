
import random
import turtle
import time
delay = 0.1

wn = turtle.Screen()
wn.title("yılan oyunu ")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)#ekran güncellemesinide kapatır

player =0
yazı = turtle.Turtle()
yazı.hideturtle()
yazı.color("white")
yazı.penup()
yazı.goto(0,-100)
yazı.write("first player : w a s d , second player : arrow keys ", None, "center", "100pt ")
time.sleep(1.5)
yazı.clear()

kafa1 = turtle.Turtle()
kafa2= turtle.Turtle()

#elma
elma=turtle.Turtle()
elma.speed(0)#animasyon hızı
elma.shape("circle")
elma.color("red")
elma.penup()
elma.goto(0,100)

def head(kafa):
    global player
    kafa.speed(0)#animasyon hızı
    kafa.shape("square")
    kafa.color("white")
    kafa.penup()
    kafa.goto(0,0)
    kafa.direction = "stop"
    if player>0:
        kafa.color("red")
        kafa.goto(100,0)
    player += 1
head(kafa1)
head(kafa2)

def go_up():
    kafa1.direction = "up"

def go_down():
    kafa1.direction = "down"

def go_left():
    kafa1.direction = "left"
   
def go_right():
    kafa1.direction = "right"

def go_up2():
    kafa2.direction = "up"

def go_down2():
    kafa2.direction = "down"

def go_left2():
    kafa2.direction = "left"
   
def go_right2():
    kafa2.direction = "right"

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up2, "Up")
wn.onkeypress(go_down2, "Down")
wn.onkeypress(go_left2, "Left")
wn.onkeypress(go_right2, "Right")

def move(kafa):
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y+20)
        
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y-20)

    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x-20)

    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x+20)

     
kuyruk1 = []
kuyruk2 = []
def govde(kafa,kuyruk):
    
    if kafa.distance(elma) < 20:
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        elma.goto(x,y)
        #kuyruk ekleme
        new_kuyruk = turtle.Turtle()
        new_kuyruk.speed(0)
        new_kuyruk.shape("square")
        if kafa == kafa2:new_kuyruk.color("red")
        else: new_kuyruk.color("white") 
        new_kuyruk.penup()
        kuyruk.append(new_kuyruk) 
 #burdaki muhabbet kuruğun en sonundaki kutuyu bi öncekinşn yerine atıyo 
    for index in range(len(kuyruk)-1, -1, -1):
      x = kuyruk[index-1].xcor()
      y = kuyruk[index-1].ycor()
      kuyruk[index].goto(x,y)
    if len(kuyruk) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruk[0].goto(x,y)
    
def bodyrools(kafa , kuyruk, kafaa):    
    
 for segment in kuyruk:
        if segment.distance(kafa) < 20 or segment.distance(kafaa) < 20  or kafa.distance(kafaa) < 20 :
            time.sleep(0.5)
            kafa.goto(0,0)
            kafa.direction = "stop"
        
            # Hide the segments
            for segment in kuyruk:
             segment.goto(1000, 1000)
        
            # Clear the segments list
            kuyruk.clear()

def kural(kafa,kuyruk):
    if kafa.xcor()>390 or kafa.xcor()<-390 or kafa.ycor()>390 or kafa.ycor()<-390:
        kafa.goto(0,0)
        time.sleep(0.5)
        kafa.direction = "stop"

        for segment in kuyruk:
         segment.goto(1000, 1000)
        kuyruk.clear()            
    

while True:
    wn.update()
    kural(kafa1,kuyruk1)
    kural(kafa2,kuyruk2) 
    govde(kafa1,kuyruk1)
    govde(kafa2,kuyruk2)
    move(kafa1)
    move(kafa2)
    bodyrools(kafa1,kuyruk1,kafa2)
    bodyrools(kafa2,kuyruk2,kafa1)


    time.sleep(delay)
    


