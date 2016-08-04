class Model:
			
	def __init__(self, rows, cols, board):
		self.rows = rows
		self.cols = cols
		self.boardtree = []
		self.boardtree.append([])
		self.boardtree[0].append(BoardTreeNode(board))

	def append_frame(self, depth, frame, parent, carId, direction):
		if len(self.boardtree) <= depth:
			self.boardtree.append([])
		self.boardtree[depth].append(BoardTreeNode(frame, parent, carId, direction))
		
	def find_frame(self, frame):
		for node in self.boardtree:
			for board in node:
				equal_lines = 0
				for i in range(0,self.rows):
					if board.frame[i] == frame[i]:
						equal_lines += 1
				if equal_lines == self.rows:
					return True				
		return False
		
		
class BoardTreeNode:
	def __init__(self, frame, parent=None, carId=None, direction=None):
		self.frame = frame
		self.parent = parent
		self.car = carId
		self.direction = direction
