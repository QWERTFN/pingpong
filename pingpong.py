from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("pingpong")

game = True
finish = False

while game:
   for e in event.get():
       if e.type == QUIT:
           game = False

display.update()
time.delay(50)
FPS = 60