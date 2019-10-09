from PIL import Image; from time import sleep;import pygame;from math import sin,cos;im=Image.open("data/height.png");disp=im.load();col=Image.open("data/colour.png");rgb_im = col.convert('RGB');clock = pygame.time.Clock();screen = pygame.display.set_mode((360,202));pygame.display.set_caption('VoxelSpace');pygame.display.flip();screen.fill((100,100,255));locX=512;locY=512;Angle=2 
for u in range(-180,1):
  for v in range(-180,180):
    t=(v/float(180))*0.785+Angle;x=int(sin(t)*-u+locX);y=int(cos(t)*-u+locY) ;h=disp[x,y];height=(h-float(disp[locX,locY] )/-u*100 + 120);pygame.draw.line(screen, rgb_im.getpixel((x,y)), (180+v,202),(180+v,202-height),1);pygame.display.flip()
sleep(10)#Tweak locX, locY and Angle (radians) to your liking. You need to paste a heightmap and colourmap (named height.png and colour.png) into the directory containing the .py file.
