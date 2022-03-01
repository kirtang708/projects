import pygame
pygame.init()
window = pygame.display.set_mode((1200,400))       # set and create a display (background)
track = pygame.image.load('track3.png')            # image loder track (route)
car = pygame.image.load('tesla.png')               # image loder car
car = pygame.transform.scale(car, (30,60))
car_x = 155                # location of car in x axis
car_y = 300                # location of car in y axis
focal_distance =  25       # because our camera is 15 in x axis          
cam_x_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()              # car speed like clock
while drive:
    for event in pygame.event.get():              #  not loading  
        if event.type == pygame.QUIT:             #   and easily quit the game 
                drive = False                     #     when i click the cancel (red button)
    clock.tick(60)                    # speed is slow like 60sec in clock
    cam_x = car_x + cam_x_offset + 15                 # car position is 30 and camera is center of car thats camera position is 15 in x axis
    cam_y = car_y + 15
   
    up_px =  window.get_at((cam_x , cam_y - focal_distance))[0] 
    right_px =  window.get_at((cam_x + focal_distance, cam_y ))[0] # in graph right x axis is positive
    print(up_px, right_px)  
    
    # change direction (take turn)
    if direction == 'up' and up_px!= 255 and right_px==255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90 )


    # drive  
    if direction=='up' and up_px == 255:                         # 255 is length os our white road
        car_y = car_y - 2                             # car starting of this syntax (- 2 )  
    if direction == 'right' and right_px == 255:
        car_x = car_x +2
    
    window.blit(track, (0,0))           #blit = (Block image transfer) track location 0=starting corner
    window.blit(car, (car_x,car_y))
    pygame.draw.circle(window,(0,200,0), (cam_x, cam_y), 5, 5)   # 0 , 200 , 0  is define a color of camera  first 5 is length of camera and second 5 is width of the camera              
                                                                 
    pygame.display.update()