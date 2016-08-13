#Rush Hour

This program solves the Rush Hour board game.  
Input can be submitted by console through the interactive (-i) option or through a file passed as program argument.  
For example:  
- rushhour.py -i   
- rushhour.py *myboardfile*

Any input file must contain a simple board formatted as:

	....AA
	..BBCC
	rr..EF
	GGHHEF
	...IEF
	...IJJ


`.`characters are used as empty cells.  
Alphabetic characters are reserved for cars.   
`r` is reserved for the special red car. 

The solution to the problem is printed on console in interactive mode or saved to a file with the *.solved* extension.
To always see the solution on console is recommended to use the verbose (-v) option.  

##Rules
1. The *red car* must be aligned horizontally and must exit from the right border of the board.

##Requirements
Python 3

##Notes
The program should be quite flexible and should support rectangular or square boards of any size.

**Andrea Mazzotti - 2016**
