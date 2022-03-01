import pygame
pygame.init()
window = pygame.display.set_mode((1200,400))       # set and create a display (background)
track = pygame.image.load('track1.png')            # image loder track (route)
car = pygame.image.load('tesla.png')               # image loder car
car = pygame.transform.scale(car, (30,60))
car_x = 150               #location of car in x axis
car_y = 300                # location of car in y axis
focal_distance =  25       #  because our camera is 15 in x axis (15+10)         
clock = pygame.time.Clock()              # car speed like clock
while True:
    clock.tick(60)                    # speed is slow like 60sec in clock
    cam_x = car_x + 15                 # car position is 30 and camera is center of car thats camera position is 15 in x axis
    cam_y = car_y + 15
   
    up_px =  window.get_at((cam_x , cam_y - focal_distance))[0]
    print(up_px)    
    if up_px == 255:                         # 255 is length os our white road
        car_y = car_y - 2                             # car starting of this syntax (- 2 )  
    window.blit(track, (0,0))           #blit = (Block image transfer) track location 0=starting corner
    window.blit(car, (car_x,car_y))
    pygame.draw.circle(window,(0,255,0), (cam_x, cam_y), 5, 5)   # 0 , 200 , 0  is define a color of camera , first 5 is length of camera and second 5 is width of the camera                                                                            
    pygame.display.update()