#varlist
ball_x = 100
ball_y = 100

x_speed = 5
y_speed = 5




def setup():
    size(500,800)

def draw():

    global ball_x 
    global ball_y 

    global x_speed 
    global y_speed 
   
    background(0,0,0) 
#ball 1 movement 
    
    fill(65,182,230)
    ellipse(ball_x,ball_y,20,20)
    
    #now the movement

        
     
    if ball_y > 850 :
        print("bounce")
      #  y_speed = - y_speed
    

       # need to get ball to reset if keyPressed and key == 'r' or key == 'r':
            #y_speed = - y_speed #this gets b
    
      #  ball_x = ball_x + x_speed
        
    
    
    #if ball_y < 25 :
     #y_speed = - y_speed
       
    ball_y = ball_y + y_speed
    
    if ball_x > 500:
        x_speed = - x_speed
    
    ball_x = ball_x + x_speed
    

# rectangle 
    fill(219,62,177)
    #rect(0, 650, 100 , 25)
    
#Pattle movement code
    if ball_y > 560 and ball_x > mouseX and ball_x < mouseX + 100 and ball_y < 650:
        y_speed = -y_speed 
   
    if ball_y < 500 :
        ball_y + y_speed
    
    if ball_x > 0:
        x_speed = - x_speed
    
    if ball_x < 500:
        x_speed = - x_speed
    
    if ball_y <0 :
        y_speed = - y_speed
    
   
    
    
    
    rect(pmouseX - 50  , 650, 100, 25)
    



#bricks
    noFill()
    fill(254,221,0)
    rect(100 , 100, 100, 25)
    rect (300,100,100,25)
    rect (50,200,90,25)
    rect (100,220,90,25)
    rect (190,220,90,25)
    rect (280,220,90,25)
    rect (350,200,90,25)
    
    

    

            




    

    
    
    
   

       

  #if lose code
    #if ball_y > 850 :
        #fill(65,182,230)
        #textSize(32)
        #text("Try Again!", 160, 400)  # Specify a z-axis value
        #text("You Lose", 160, 300)  # Default depth, no z-value specified
        #text("Click R to restart", 119, 500)  # Default depth, no z-value specified
