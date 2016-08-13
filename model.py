class Model:
			
	def __init__(self, rows, cols, board):
		self.rows = rows
		self.cols = cols
		self.boardtree = []
		self.boardtree.append([])
		self.boardtree[0].append(BoardTreeNode(board))
		self.solution = []
		self.solution_frames = []

	def append_frame(self, depth, frame, parent, carId, direction):
		if len(self.boardtree) <= depth:
			self.boardtree.append([])
		frame = ''.join(frame)		#Store the frame as String (performance)
		self.boardtree[depth].append(BoardTreeNode(frame, parent, carId, direction))

	def split_frame(self, frame):
		ret_frame = []
		for x in range(0, self.rows):
			ret_frame.append(frame[x*self.cols:(x+1)*self.cols])
		return ret_frame	
			
	def find_frame(self, frame):
		curframe = "".join(frame)
		for node in self.boardtree:
			for board in node:
				if (curframe == board.frame):
					return True
		return False	
		
	def save_solution(self, board, depth):
		for x in range(depth, 0, -1):
			self.solution.append("Move car {} {}".format(board.car, board.direction))
			self.solution_frames.append(self.split_frame(board.frame))
			board = board.parent
		self.solution.reverse()
		self.solution_frames.reverse()		
		
		
class BoardTreeNode:
	def __init__(self, frame, parent=None, carId=None, direction=None):
		self.frame = frame
		self.parent = parent
		self.car = carId
		self.direction = direction
