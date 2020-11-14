import pygame
import random
from display import *
pygame.init()

class L(object):
	def __init__(self, screen, nnn):
		self.colorList =[(66,53,242),(255,165,0),(255,215,0),(220,20,60),(148,0,211),(60,179,113),(30,144,255)]
		self.color = self.colorList[nnn]
		self.posCenter = [cube * 4 +1, cube+1]
		self.shapeShape = nnn
		self.shapeNum = 0;
		self.updatePos(0, 0)
		self.draw(screen)
		self.fallEvent = pygame.USEREVENT + 1
		pygame.time.set_timer(self.fallEvent, 1000)
		self.hitBot = False
		self.canSwitch = True

	def updatePos(self, x, y):
		self.posCenter[0] += x
		self.posCenter[1] += y
		####   SHAPE KEY == [which shape][Shape formation rotation][inside the shape]
		self.shapes = [[[(self.posCenter[0] - cube, self.posCenter[1],32,32),			#        #
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#      ###
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#       # 
						 (self.posCenter[0]       , self.posCenter[1],32,32),			# 		#
						 (self.posCenter[0], self.posCenter[1] + cube,32,32),			#		##
						 (self.posCenter[0] + cube,self.posCenter[1] + cube,32,32)],	#			***L PIECE
						[(self.posCenter[0] + cube, self.posCenter[1],32,32),			# 
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#		###
						 (self.posCenter[0] - cube,self.posCenter[1],32,32),			#		#
						 (self.posCenter[0] - cube,self.posCenter[1] + cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] + cube,32,32),			#		
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#		##
						 (self.posCenter[0], self.posCenter[1] - cube,32,32),			#		 #
						 (self.posCenter[0] - cube,self.posCenter[1] - cube,32,32)]],	#====	 #

					   [[(self.posCenter[0] + cube, self.posCenter[1],32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#		#  
						 (self.posCenter[0] - cube, self.posCenter[1],32,32),			#		###							
						 (self.posCenter[0] - cube,self.posCenter[1] - cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] + cube,32,32),			#		##
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#		#
						 (self.posCenter[0], self.posCenter[1] - cube,32,32),			#		#
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)],	#			***J PIECE
						[(self.posCenter[0] - cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#		###
						 (self.posCenter[0] + cube,self.posCenter[1],32,32),			#		  #
						 (self.posCenter[0] + cube,self.posCenter[1] + cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#		#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#		#
						 (self.posCenter[0], self.posCenter[1] + cube,32,32),			#	   ##
						 (self.posCenter[0] - cube,self.posCenter[1] + cube,32,32)]],	#====

					   [[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)],	#			***O PIECE
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)]],	#====

					   [[(self.posCenter[0] + cube, self.posCenter[1],32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] , self.posCenter[1]-cube,32,32),			#									
						 (self.posCenter[0] - cube,self.posCenter[1] - cube,32,32)], 	#
						[(self.posCenter[0], self.posCenter[1] + cube,32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)],	#			***Z PIECE
						[(self.posCenter[0] - cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0], self.posCenter[1] + cube,32,32),			#
						 (self.posCenter[0] + cube,self.posCenter[1] + cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] - cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0] - cube,self.posCenter[1] + cube,32,32)]],	#====

						 [[(self.posCenter[0] + cube, self.posCenter[1],32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] , self.posCenter[1]-cube,32,32),			#									
						 (self.posCenter[0] - cube,self.posCenter[1],32,32)],			#
						[(self.posCenter[0] + cube, self.posCenter[1],32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0], self.posCenter[1] - cube,32,32),			#									
						 (self.posCenter[0],self.posCenter[1] + cube,32,32)],			#			***T PIECE
						[(self.posCenter[0] + cube, self.posCenter[1],32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] - cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0], self.posCenter[1] + cube,32,32)],			#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#====
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] - cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0], self.posCenter[1] + cube,32,32)]],	#====

						 [[(self.posCenter[0] - cube, self.posCenter[1],32,32),
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#====
						 (self.posCenter[0], self.posCenter[1] - cube,32,32),			#									
						 (self.posCenter[0] + cube,self.posCenter[1] - cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube,self.posCenter[1] + cube,32,32)],	#			***S PIECE
						[(self.posCenter[0] + cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0], self.posCenter[1] + cube,32,32),			#
						 (self.posCenter[0] - cube,self.posCenter[1] + cube,32,32)],	#
						[(self.posCenter[0], self.posCenter[1] + cube,32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0] - cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0] - cube,self.posCenter[1] - cube,32,32)]],	#====

					   [[(self.posCenter[0] - cube, self.posCenter[1],32,32),
					 	 (self.posCenter[0]       , self.posCenter[1],32,32),			#====
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#									
						 (self.posCenter[0] + cube * 2,self.posCenter[1],32,32)],		#
						[(self.posCenter[0] + cube, self.posCenter[1] - cube,32,32),	#
						 (self.posCenter[0] + cube, self.posCenter[1],32,32),			#
						 (self.posCenter[0] + cube, self.posCenter[1] + cube,32,32),	#
						 (self.posCenter[0] + cube,self.posCenter[1] + cube* 2,32,32)],	#			***I PIECE
						[(self.posCenter[0] - cube, self.posCenter[1] + cube,32,32),	#
						 (self.posCenter[0]       , self.posCenter[1] + cube,32,32),	#
						 (self.posCenter[0] + cube,self.posCenter[1] + cube,32,32),		#
						 (self.posCenter[0] + cube * 2,self.posCenter[1] + cube,32,32)],#
						[(self.posCenter[0], self.posCenter[1] - cube,32,32),			#
						 (self.posCenter[0]       , self.posCenter[1],32,32),			#
						 (self.posCenter[0], self.posCenter[1] + cube,32,32),			#
						 (self.posCenter[0],self.posCenter[1] + cube*2,32,32)]]] 	#ending of shapes

		self.pos1 = self.shapes[self.shapeShape][self.shapeNum][0]
		self.pos2 = self.shapes[self.shapeShape][self.shapeNum][1]
		self.pos3 = self.shapes[self.shapeShape][self.shapeNum][2]
		self.pos4 = self.shapes[self.shapeShape][self.shapeNum][3]

		#					 Y  					X
		self.pos1RC = (self.pos1[1]//33, self.pos1[0]//33, self.color)
		self.pos2RC = (self.pos2[1]//33, self.pos2[0]//33, self.color)
		self.pos3RC = (self.pos3[1]//33, self.pos3[0]//33, self.color)
		self.pos4RC = (self.pos4[1]//33, self.pos4[0]//33, self.color)

		self.RClist = [self.pos1RC,self.pos2RC,self.pos3RC,self.pos4RC]
		 

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == self.fallEvent:
				self.drop()

			if event.type == pygame.KEYDOWN:
				#################   LEFT  #################
				if event.key == pygame.K_LEFT:
					for i in range(4):
						if self.RClist[i][1] <= 0:
							return
					if board.ColisionDetectLR(self.RClist, -1) == True:
						return
					self.updatePos(cube * -1, 0)

				#################   RIGHT  #################
				elif event.key == pygame.K_RIGHT:
					for i in range(4):
						if self.RClist[i][1] >= 9:
							return
					if board.ColisionDetectLR(self.RClist, +1) == True:
						return
					self.updatePos(cube, 0)
				#################   UP     #################
				elif event.key == pygame.K_UP:
					self.rotate()
				#################  DOWN ####################
				elif event.key == pygame.K_DOWN:
					if board.ColisionDetectDown(self.RClist):
						board.stickPiece(self.RClist)
						self.hitBot = True
					self.updatePos(0, cube)
					board.score += 1
				################# SPACE ####################
				elif event.key == pygame.K_SPACE:
					while(not board.ColisionDetectDown(self.RClist)):
						board.score += 1
						self.drop()
					board.stickPiece(self.RClist)
					self.hitBot = True
				################ C #######################
				elif event.key == pygame.K_c:
					if(self.canSwitch == True):
						if(holdPiece.num == 7):
							global nextPieceNum
							holdPiece.num = self.shapeShape;
							self.shapeShape = nextPieceNum
							nextPieceNum = random.randint(0,6)
						else:
							tmp = holdPiece.num
							holdPiece.num = self.shapeShape
							self.shapeShape = tmp
						self.canSwitch = False
						self.posCenter = [cube * 4 +1, cube+1]
						self.updatePos(0,0)					

				###############  R  ######################
				elif event.key == pygame.K_r:
					#reset board
					board.rowColumn = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], 
					[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], 
					[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[2,2,2,2,2,2,2,2,2,2]] 

	def draw(self, surface):
		self.color = self.colorList[self.shapeShape]
		pygame.draw.rect(surface,self.color,self.pos1)
		pygame.draw.rect(surface,self.color,self.pos2)
		pygame.draw.rect(surface,self.color,self.pos3)
		pygame.draw.rect(surface,self.color,self.pos4)

	def drop(self):
		if board.ColisionDetectDown(self.RClist):
			board.stickPiece(self.RClist)
			self.hitBot = True
			
		self.updatePos(0, cube)

	def rotate(self):
		self.shapeNum += 1
		if self.shapeNum > 3:
			self.shapeNum = 0
		self.updatePos(0,0)
		for i in range(4):
			if self.shapes[self.shapeShape][self.shapeNum][i][0] <= 0:
				self.updatePos(cube, 0)
			if self.shapes[self.shapeShape][self.shapeNum][i][0] >= 33 * 10:
				self.updatePos(cube * -1, 0)
		if board.ColisionDetectLR(self.RClist, 0):
			if not board.ColisionDetectLR(self.RClist, 2): #########!!!!!!!!!!!!!!!!!!!!!
				self.updatePos(cube, 0)
			elif not board.ColisionDetectLR(self.RClist, -2):
				self.updatePos(cube * -1, 0)
			else:
				self.shapeNum -= 1
				if self.shapeNum == -1:
					self.shapeNum = 3
				self.updatePos(cube,0)
			for i in range(4):
					if self.shapes[self.shapeShape][self.shapeNum][i][0] <= 0:
						self.shapeNum -= 1
						if self.shapeNum == -1:
							self.shapeNum = 3
						self.updatePos(cube, 0)
					if self.shapes[self.shapeShape][self.shapeNum][i][0] >= 33 * 10:
						self.shapeNum -= 1
						if self.shapeNum == -1:
							self.shapeNum = 3
						self.updatePos(cube * -1, 0)
		if board.ColisionUD(self.RClist, 0):
			if not board.ColisionUD(self.RClist, 1):
				self.updatePos(0, cube * -1)

		

class Board(object):
	def __init__(self):
		#scoreboard
		self.tetris = 0
		self.score = 0

		#				   0 1 2 3 4 5 6 7 8 9
		self.rowColumn = [[0,0,0,0,0,0,0,0,0,0], #0
						  [0,0,0,0,0,0,0,0,0,0], #1
						  [0,0,0,0,0,0,0,0,0,0], #2 
						  [0,0,0,0,0,0,0,0,0,0], #3
						  [0,0,0,0,0,0,0,0,0,0], #4
						  [0,0,0,0,0,0,0,0,0,0], #5
						  [0,0,0,0,0,0,0,0,0,0], #6
						  [0,0,0,0,0,0,0,0,0,0], #7 
						  [0,0,0,0,0,0,0,0,0,0], #8
						  [0,0,0,0,0,0,0,0,0,0], #9
						  [0,0,0,0,0,0,0,0,0,0], #10
						  [0,0,0,0,0,0,0,0,0,0], #11
						  [0,0,0,0,0,0,0,0,0,0], #12
						  [0,0,0,0,0,0,0,0,0,0], #13
						  [0,0,0,0,0,0,0,0,0,0], #14
						  [0,0,0,0,0,0,0,0,0,0], #15
						  [0,0,0,0,0,0,0,0,0,0], #16
						  [0,0,0,0,0,0,0,0,0,0], #17
						  [0,0,0,0,0,0,0,0,0,0], #18
						  [0,0,0,0,0,0,0,0,0,0], #19
						  [2,2,2,2,2,2,2,2,2,2]] #20 for the bottom. will not change and will stay as the bottom

	def ColisionDetectDown(self,fdsa):
		for i in range(4):
			if self.rowColumn[fdsa[i][0] + 1][fdsa[i][1]] != 0:
				return True
		return False

	def ColisionDetectLR(self,fdsa,num):
		for i in range(4):
			if fdsa[i][1] + num > 9:
				return True
			if self.rowColumn[fdsa[i][0]][fdsa[i][1] + num] != 0:
				return True
		return False

	def ColisionUD(self, fdsa, num):
		for i in range(4):
			if self.rowColumn[fdsa[i][0] - num][fdsa[i][1]] != 0:
				return True
		return False

	def stickPiece(self,fdsa):
		for i in range(4):
			self.rowColumn[fdsa[i][0]][fdsa[i][1]] = fdsa[i]
		self.LineCheck()

	def DrawBoard(self, screen):
		self.scoreDisplay = myFont.render(('SCORE'),1,(255,255,255))
		screen.blit(self.scoreDisplay,(33 * 11 + 10, 5))
		self.scoreDisplay = myFont.render('%07i' % self.score,1,(255,255,255))
		screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 1 + 5))
		if self.tetris == 0:
			pass
		elif self.tetris == 1:
			self.scoreDisplay = myFont.render('SINGLE',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 13 + 5))
			self.scoreDisplay = myFont.render('+100pts',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 14 + 5))
		elif self.tetris == 2:
			self.scoreDisplay = myFont.render('DOUBLE',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 13 + 5))
			self.scoreDisplay = myFont.render('+200pts',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 14 + 5))
		elif self.tetris == 3:
			self.scoreDisplay = myFont.render('TRIPLE',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 13 + 5))
			self.scoreDisplay = myFont.render('+300pts',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 14 + 5))
		elif self.tetris == 4:
			self.scoreDisplay = myFont.render('TETRIS',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 13 + 5))
			self.scoreDisplay = myFont.render('+500pts',1,(255,255,255))
			screen.blit(self.scoreDisplay,(33 * 11 + 6 , 33 * 14 + 5))
		rowNum = -1
		for row in self.rowColumn:
			rowNum += 1
			for spot in row:
				if spot == 0:
					continue
				if spot == 2:
					continue
				else:
					pygame.draw.rect(screen, spot[2], (spot[1] * 33 +1, rowNum * 33+1, 32, 32))

	def LineCheck(self):
		TBD = []
		rowCounter = -1
		for row in self.rowColumn:
			rowCounter += 1
			numCounter = 0
			for spot in row:
				if spot == 0:
					break
				if spot == 2:
					break
				numCounter += 1
			if numCounter == 10:
				TBD.append(rowCounter)
		self.deleteRows(TBD)

	def deleteRows(self, TBD):
		self.score += len(TBD) * 100
		self.tetris = len(TBD)
		if len(TBD) > 3:
			self.score += 100
		for rowNum in TBD:
			self.rowColumn.pop(rowNum)
			self.rowColumn.insert(0,[0,0,0,0,0,0,0,0,0,0])
		self.DrawBoard


def DrawGrid(surface):
	x = 0
	y = 0
	w = 33 * 10
	h = 33 * 20
	#for i in range(21):
	pygame.draw.line(surface, (255,255,255), (w,cube * 2 + 10),(width,cube * 2 + 10))
	pygame.draw.line(surface, (255,255,255), (w,cube * 15 + 10),(width,cube * 15 + 10))
	pygame.draw.line(surface, (255,255,255), (x,y),(width,y)) #top line
	pygame.draw.line(surface, (255,255,255), (w,y),(w,h))	#middle line
	#	y += 33
	#y = 0
	
	pygame.draw.line(surface, (255,255,255), (x,y),(x,h)) #left line
	pygame.draw.line(surface, (255,255,255), (width,y),(width,h)) #right linec
	pygame.draw.line(surface, (255,255,255), (x,h),(width,h)) #bottom line
	#	x += 33


def DrawWin(surface):
	surface.fill((0,0,0))
	DrawGrid(surface)
	piece.draw(surface)
	holdPiece.drawPosition(surface)
	board.DrawBoard(surface)
	holdPiece.drawPosition(surface)
	pygame.display.update()




def main():
	global width, height, cube , piece, board, myFont, holdPiece, nextPieceNum
	cube = 33
	width = 33 * 16
	height = 33 * 20
	screen = pygame.display.set_mode((width + 1,height + 1))
	myFont = pygame.font.Font("TFont.ttf", 30)
	clock = pygame.time.Clock()
	test = random.randint(0,6)
	nextPieceNum = random.randint(0,6)
	piece = L(screen, test)
	holdPiece = Display(7)
	board = Board()
	

	


	game = True
	while game:
		if piece.hitBot == True:
			test = nextPieceNum;
			nextPieceNum = random.randint(0,6)
			piece = L(screen, test)
			if board.ColisionUD(piece.RClist,0):
				print('gameover')
				game = False
		clock.tick()
		piece.move()
		DrawWin(screen)





if __name__ == '__main__':
	main()
