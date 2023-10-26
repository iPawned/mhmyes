def setup():
    # Set the size of your sketch
    size (500,500)
    
    pass
    
def draw():
    x = 300
    print('start')
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(5):
        if i % 2 == 0:
            fill(255,0,0)
        else:
            fill(255,255,255)
        print(i % 2)
        ellipse(250,250,x,x)
        x -= 75
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
