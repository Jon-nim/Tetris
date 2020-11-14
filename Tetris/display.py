import pygame
class Display(object):
	def __init__(self,num):
		self.cube = 33
		self.posCenter = [33 * 12 + 15, 33 * 17 + 15]
		self.num = num
		self.colorList =[(66,53,242),(255,165,0),(255,215,0),(220,20,60),(148,0,211),(60,179,113),(30,144,255),(0,0,0)]
		self.color = self.colorList[num]

		####   SHAPE KEY == [which shape][inside the shape]
		self.shapes = [[(self.posCenter[0] - self.cube, self.posCenter[1],32,32),				##
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),				 	##
						 (self.posCenter[0] + self.cube, self.posCenter[1],32,32),				##								
						 (self.posCenter[0] + self.cube,self.posCenter[1] - self.cube,32,32)],	##

					   [(self.posCenter[0] + self.cube, self.posCenter[1],32,32),			
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#		#  
						 (self.posCenter[0] - self.cube, self.posCenter[1],32,32),			#		###							
						 (self.posCenter[0] - self.cube,self.posCenter[1] - self.cube,32,32)],	#

					   [(self.posCenter[0]-12, self.posCenter[1] - self.cube,32,32),				##
					 	 (self.posCenter[0] -12      , self.posCenter[1],32,32),			#		## O piece
						 (self.posCenter[0] + self.cube-12, self.posCenter[1],32,32),			#	##								
						 (self.posCenter[0] + self.cube-12,self.posCenter[1] - self.cube,32,32)],	##

					   [(self.posCenter[0] + self.cube, self.posCenter[1],32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] , self.posCenter[1]-self.cube,32,32),			#									
						 (self.posCenter[0] - self.cube,self.posCenter[1] - self.cube,32,32)], 	#


						[(self.posCenter[0] + self.cube, self.posCenter[1],32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] , self.posCenter[1]-self.cube,32,32),			#									
						 (self.posCenter[0] - self.cube,self.posCenter[1],32,32)],			#
						
						[(self.posCenter[0] - self.cube, self.posCenter[1],32,32),
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#====
						 (self.posCenter[0], self.posCenter[1] - self.cube,32,32),			#									
						 (self.posCenter[0] + self.cube,self.posCenter[1] - self.cube,32,32)],	#

					    [(self.posCenter[0] - self.cube - 12, self.posCenter[1],32,32),
					 	 (self.posCenter[0]  - 12     , self.posCenter[1],32,32),			#====
						 (self.posCenter[0] + self.cube- 12, self.posCenter[1],32,32),			#									
						 (self.posCenter[0] + self.cube * 2- 12,self.posCenter[1],32,32)],

						 [(self.posCenter[0] - self.cube, self.posCenter[1],32,32),
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#====
						 (self.posCenter[0] + self.cube, self.posCenter[1],32,32),			#		place holder shape;		aka is black;					
						 (self.posCenter[0] + self.cube * 2,self.posCenter[1],32,32)]]	#ending of shapes

		self.pos1 = self.shapes[num][0]
		self.pos2 = self.shapes[num][1]
		self.pos3 = self.shapes[num][2]
		self.pos4 = self.shapes[num][3]

		#					 Y  					X
		self.pos1RC = (self.pos1[1]//33, self.pos1[0]//33, self.color)
		self.pos2RC = (self.pos2[1]//33, self.pos2[0]//33, self.color)
		self.pos3RC = (self.pos3[1]//33, self.pos3[0]//33, self.color)
		self.pos4RC = (self.pos4[1]//33, self.pos4[0]//33, self.color)

		self.RClist = [self.pos1RC,self.pos2RC,self.pos3RC,self.pos4RC]
		 
	def drawPosition(self,screen):
		self.color = self.colorList[self.num]
		for i in range(4):
			pygame.draw.rect(screen, self.color, self.shapes[self.num][i])