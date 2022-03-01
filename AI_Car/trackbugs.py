import pygame
pygame.init()
window = pygame.display.set_mode((1200,400))       # set and create a display (background)
track = pygame.image.load('track5.png')            # image loder track (route)
car = pygame.image.load('tesla.png')               # image loder car
car = pygame.transform.scale(car, (30,60))
car_x = 150                 #location of car in x axis
car_y = 300                # location of car in y axis
focal_distance =  10     #  car on road stability          
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()              # car speed like clock
while drive:
    for event in pygame.event.get():              #  not loading  
        if event.type == pygame.quit:             #   and easily quit the game 
                drive = False                     #     when i click the cancel (red button)
    clock.tick(60)                    # speed is slow like 60sec in clock
    cam_x = car_x + cam_x_offset + 15      # car position is 30 and camera is center of car thats camera position is 15 in x axis
    cam_y = car_y + cam_y_offset 
   
    up_px =  window.get_at((cam_x , cam_y - focal_distance))[0]        # 255 is length os our white road
    down_px =  window.get_at((cam_x , cam_y - focal_distance))[0]       # when turn down then y axis positive
    right_px =  window.get_at((cam_x + focal_distance , cam_y ))[0]     # car starting of this syntax (- 2 )
    print(up_px, right_px, down_px)                                           #blit = (Block image transfer) track location 0=starting corner

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:     # direction is up then go and turn right then turn right
        direction = 'right'
        cam_x_offset = 15   # where stop the car like after red  before red ......
        car = pygame.transform.rotate(car , -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:     #car going right but not more white 
        direction = 'down' 
        car_x_offset = car_x + 10
        cam_x_offset = 0
        cam_y_offset = car_y - 65
        car = pygame.transform.rotate(car, -90)                                                # right side then car going to down side

    # drive 
       
    if direction =='up' and up_px == 255:               #  direction is up then going up                        
        car_y = car_y - 2
    
    elif direction == 'right' and right_px == 255:      # direction is right then going right
        car_x = car_x + 2                                 
    
    elif direction == 'down' and down_px ==255:    #direction is down then car is going down side
        car_y = car_y + 2
    window.blit(track, (0,0))           
    window.blit(car, (car_x,car_y))
    pygame.draw.circle(window,(0,200,0), (cam_x, cam_y), 3, 3)   # 0 , 200 , 0  is define a color of camera
                                                                 # first 5 is length of camera and second 5 is width of the camera              
    pygame.display.update()