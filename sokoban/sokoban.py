import pygame
import sys
import time
from UserString import MutableString

pygame.init()
pixelx = 60
pixely = 60
tilex = 10
tiley = 8
displayx = tilex * pixelx
displayy = tiley * pixely
iot_keycount = 0
iot_caption = 'iotsokoban'
pygame.display.set_caption('iot_caption')
DISPLAYSURF = pygame.display.set_mode((displayx, displayy), 0, 32)

WHITE = (255, 255, 255)
Imgwall = pygame.image.load('iot_wall.png')
ImgmanF = pygame.image.load('iot_manF.png')
ImgmanB = pygame.image.load('iot_manB.png')
ImgmanL = pygame.image.load('iot_manL.png')
ImgmanR = pygame.image.load('iot_manR.png')
Imgman = ImgmanF
Imgdot = pygame.image.load('iot_dot.png')
Imgbox = pygame.image.load('iot_B.png')
Imgclear = pygame.image.load('iot_clear.png')
manx = 0
many = 0

iot_stage = [
	[
	MutableString('##########'),
	MutableString('#@       #'),
	MutableString('#   .    #'),
	MutableString('#    B   #'),
	MutableString('#  B     #'),
	MutableString('#     .  #'),
	MutableString('#        #'),
	MutableString('##########')
	],
	[
	MutableString('##########'),
	MutableString('#@##     #'),
	MutableString('# #      #'),
	MutableString('# # B    #'),
	MutableString('# #  ### #'),
	MutableString('# #  ##  #'),
	MutableString('#    ## .#'),
	MutableString('##########')
	],
	[
	MutableString('##########'),
	MutableString('# .#######'),
	MutableString('#  #    ##'),
	MutableString('#  # # B##'),
	MutableString('#  #@#  ##'),
	MutableString('# B# #  ##'),
	MutableString('#    #  .#'),
	MutableString('##########')]]
stage_num = 0
stage_num = 0
iot_caption = 'iotsokoban [stage : %d]'%(stage_num+1)
pygame.display.set_caption(iot_caption)
stage_end = False
iot_map = []
for istage in range(tiley):
	iot_map.append(iot_stage[stage_num][istage][:])

while True:
	DISPLAYSURF.fill(WHITE)
	stage_end = True
	for ix in range(tilex):
		for iy in range(tiley):
			if '#'==iot_map[iy][ix]:	
				DISPLAYSURF.blit(Imgwall, (ix * pixelx, iy * pixely))
			elif '@'==iot_map[iy][ix]:
				DISPLAYSURF.blit(Imgman, (ix * pixelx, iy * pixely))
				manx = ix
				many = iy
			elif '.'==iot_map[iy][ix]:	
				DISPLAYSURF.blit(Imgdot, (ix * pixelx, iy * pixely))
			elif 'B'==iot_map[iy][ix]:	
				DISPLAYSURF.blit(Imgbox, (ix * pixelx, iy * pixely))
				if '.' !=iot_stage[stage_num][iy][ix]:
					stage_end = False
	pygame.display.update()
	if True == stage_end:
		DISPLAYSURF.blit(Imgclear, (120,210))
		pygame.display.update()
		keyinput = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					keyinput = True
					break
			if True == keyinput:
				break
			time.sleep(0.1)
			continue
		stage_num = stage_num + 1
		iot_map = []
		for istage in range(tiley):
			iot_map.append(iot_stage[stage_num][istage][:])
		iot_caption = 'iotsokoban [stage : %d]'%(stage_num+1)
		pygame.display.set_caption(iot_caption)
		continue
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			TempX = manx
			TempY = many
			if event.key == pygame.K_DOWN:
				Imgman = ImgmanF
				many = many + 1
			elif event.key == pygame.K_UP:
				Imgman = ImgmanB
				many = many - 1
			elif event.key == pygame.K_RIGHT:
				Imgman = ImgmanR
				manx = manx + 1
			elif event.key == pygame.K_LEFT:
				Imgman = ImgmanL
				manx = manx - 1
			elif event.key == pygame.K_r:
				iot_map = []
				for istage in range(tiley):
					iot_map.append(iot_stage[stage_num][istage][:])
				break
			else:
				continue
			#if ' ' == iot_map[many][manx] or '.' == iot_map[many][manx]:
			if '#' != iot_map[many][manx]:
				if 'B' == iot_map[many][manx]:
					if	iot_map[2*many-TempY][2*manx-TempX] ==' ' or iot_map[2*many-TempY][2*manx-TempX] == '.':
						iot_map[2*many-TempY][2*manx-TempX] = 'B'
					else:
						many = TempY
						manx = TempX
						continue
				if '.' == iot_stage[stage_num][TempY][TempX]: 	
					iot_map[TempY][TempX] = '.'
				else:
					iot_map[TempY][TempX] = ' ' 	
				iot_map[many][manx] = '@'
				iot_keycount = iot_keycount + 1
				print iot_keycount
			else:
				manx = TempX
				many = TempY
		elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

