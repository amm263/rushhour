#!/usr/bin/python3

import sys
import time
from controller import Controller
from model import Model

#Input Options
verbose = False
interactive = False
file_path = ''
start_time = time.time()

#Parse arguments
del sys.argv[0] #First argument is program name.
for argument in sys.argv:
	if argument == '-v':
		verbose = True
	elif argument == '-i':
		interactive = True
	else:
		file_path = argument
		
if interactive:
	file_path = 'None - Interactive mode selected'
	
if verbose:	
	print ("Options:")
	print ("\tVebose: ", verbose)
	print ("\tInteractive: ", interactive)
	if len(file_path)==0:
		print ("\tFile path: No file selected")	
	else: 	
		print ("\tFile path: ", file_path)	


board = []
rows = 0
cols = 0
		
if interactive: 
	print ("\nPlease draw your board:")
	print ("-Use '.' for empty cells")
	print ("-Alphabetic characters are reserved for cars")
	print ("-'r' is reserved for the special red car")
	print ("-Insert a blank line to finish\n")
	while True:
		line = input()
		if len(line) == 0:
			break
		else:
			if (cols == 0) or (cols == len(line)):
				cols = len(line)
				board.insert(rows, line)
				rows += 1
			else :
				print ("Error: Wrong input in row ", rows, ". Expecting ", cols, " columns, but received ", len(line)) 

elif not file_path=='':
	f = open(file_path, 'r')
	for line in f:
		if (cols == 0) or (cols == len(line)-1):
			line = line.strip()
			cols = len(line)
			board.insert(rows, line)
			rows += 1
		else :	
			sys.exit("Error: Wrong input in row {}. Expecting {} columns, but received {}.".format(rows, cols, len(line)))
	f.close()		
				
else:		
	print ("Usage: $rushour.py [-v] [-i] [file_path] \n\t-v: Verbose mode \n\t-i: Interactive mode (overrides file usage)	\n\tfile_path: Parse a text file containing a game board")
	sys.exit()
				
if verbose:
	print ("\nBoard acquired: ")			
	for x in range(0,rows):
		print (board[x])	
	print ("\nFinding any solution...")				

board = ''.join(board)
model = Model(rows, cols, board)					
controller = Controller(model, verbose)

if (controller.play()):		
	if len(model.solution)>0:   #Paranoia
		depth = len(model.solution)
		if interactive or verbose:
			for x in range(1, depth):
				print ("\nStep {} - {}".format(x, model.solution[x]))
				for z in range(0,rows):
					print (model.solution_frames[x][z])	
			print("\nWon in {} steps!".format(depth-1))	
			print("\nTime: {0:.3} seconds".format(time.time()-start_time))
		else: 	
			f = open(file_path+'.solved', 'w')
			f.write("Step 0 - Origin board")
			for x in range(0,rows):
				f.write('\n'+board[x])	
			for x in range(1, depth):
				f.write("\nStep {} - {}".format(x, model.solution[x]))
				for z in range(0,rows):
					f.write('\n'+model.solution_frames[x][z])	
			f.write("\nWon in {} steps!".format(depth-1))	
			f.write("\nTime: {0:.3g} seconds".format(time.time()-start_time))
			f.close()
else:
	if interactive or verbose:
		print ("No movements left, can not find a solution.")			
			 
			
				
