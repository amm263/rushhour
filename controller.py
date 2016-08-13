from model import Model
import sys
class Controller:
	def __init__(self, model, verbose):
		self.model = model
		self.curdepth = 0
		self.verbose = verbose
	
	#Start the game. True is returned if a solution was found, False otherwise.
	def play(self):
		depth = 0
		while True:
			moved = False
			curboardlist = self.model.boardtree[depth]
			depth += 1
			for board in curboardlist:
				originframe = self.model.split_frame(board.frame); 
				car_list = self.get_car_list(originframe)
				for car in car_list:
					if car['id'] == 'r': # Test if the red car is in a winning position.
						if car['tail_y']+car['size'] == self.model.cols:
							self.model.save_solution(board, depth)
							return True
					if car['alignment'] == '-':			#Moves orizontally
						if (car['tail_y'] > 0) and (originframe[car['tail_x']][car['tail_y']-1] == '.') :
							#Move Left
							curframe = originframe.copy()
							currow = list(curframe[car['tail_x']])
							currow[car['tail_y']-1] = car['id']
							currow[car['tail_y']+car['size']-1] = '.'
							curframe[car['tail_x']] = ''.join(currow)
							if not self.model.find_frame(curframe):
								self.model.append_frame(depth, curframe, board, car['id'], 'Left')
								moved = True
						if ((car['tail_y']+car['size']) < self.model.cols) and (originframe[car['tail_x']][car['tail_y']+car['size']] == '.') :  
							#Move Right
							curframe = originframe.copy()
							currow = list(curframe[car['tail_x']])
							currow[(car['tail_y']+car['size'])] = car['id']
							currow[car['tail_y']] = '.'
							curframe[car['tail_x']] = ''.join(currow)
							if not self.model.find_frame(curframe):
								self.model.append_frame(depth, curframe, board, car['id'], 'Right')
								moved = True
					else:								#Moves vertically
						if (car['tail_x'] > 0) and (originframe[car['tail_x']-1][car['tail_y']] == '.') :
							#Move Up
							curframe = originframe.copy()
							currow_tail = list(curframe[car['tail_x']-1])
							currow_head = list(curframe[car['tail_x']+car['size']-1])
							currow_tail[car['tail_y']] = car['id']
							currow_head[car['tail_y']] = '.'
							curframe[car['tail_x']-1] = ''.join(currow_tail)
							curframe[car['tail_x']+car['size']-1] = ''.join(currow_head)
							if not self.model.find_frame(curframe):
								self.model.append_frame(depth, curframe, board, car['id'], 'Up')
								moved = True
						if ((car['tail_x']+car['size']) < self.model.rows) and (originframe[car['tail_x']+car['size']][car['tail_y']] == '.') : 
							#Move Down 
							curframe = originframe.copy()
							currow_tail = list(curframe[car['tail_x']])
							currow_head = list(curframe[car['tail_x']+car['size']])
							currow_tail[car['tail_y']] = '.'
							currow_head[car['tail_y']] = car['id']
							curframe[car['tail_x']] = ''.join(currow_tail)
							curframe[car['tail_x']+car['size']] = ''.join(currow_head)
							if not self.model.find_frame(curframe):
								self.model.append_frame(depth, curframe, board, car['id'], 'Down')	
								moved = True		
			if not moved:
				#No movements left, can not find a solution.
				return False
	
	# Analyze a frame and returns the list of cars.
	# This function assumes that the first alphabetic character found is the 'tail' of the car.
	# A car is represented by its 'id' (letter used to represent it), position of the 'tail' (x and y), and size of the car. 
	def get_car_list(self, frame):
		car_list = []
		for x in range(0, self.model.rows):
			for y in range(0, self.model.cols):
				if frame[x][y].isalpha():
					index = -1
					for car in car_list:
						if frame[x][y] == car['id']:
							index = car_list.index(car)
							break
					if index == -1:
						car_id = frame[x][y]
						car_tail_x = x
						car_tail_y = y
						car_size = 1
						car_alignment = ''
						#Check DOWN
						if x<self.model.rows:
							for i in range(x+1, self.model.rows):
								if frame[i][y] == car_id:
									car_size += 1
									car_alignment = '|'
								else: 
									break		
						#Check RIGHT
						if y<self.model.cols:
							for i in range(y+1, self.model.cols):
								if frame[x][i] == car_id:
									car_size += 1
									car_alignment = '-'
								else:
									break
						if car_alignment != '':
							car = dict()
							car['id'] = car_id
							car['tail_x'] = car_tail_x
							car['tail_y'] = car_tail_y
							car['size'] = car_size 
							car['alignment'] = car_alignment
							car_list.append(car)
						else:
							sys.exit("Error: car {} size is {} and it's not aligned!".format(car_id, car_size))
		return car_list					
							
							
						
						
		
		
