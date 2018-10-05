import sys
import cell as celllib
import termplot
# from bashplotlib.histogram import plot_hist
# import gnuplotlib as gp

def printOnLine(string):
	print(string)

print("CellSim")

if len(sys.argv) <= 1:
	print("Invalid args provided")
	print("python3 src/ <units of food> <starting cells> <interphase legnth> <no food survival legnth>")
	exit(1)

starting_cells = int(sys.argv[2])
food = int(sys.argv[1])
precent_interphase = int(sys.argv[3])
precent_mitosis = 100 - precent_interphase

alive_cells = []

# Create Cells
for i in range(0, starting_cells):
	alive_cells.append(celllib.Cell(i, sys.argv[3], sys.argv[4]))

# keep the ids incrementing
i += 1

print(str(len(alive_cells)) + " Cells have been created...\nStarting simulation")

alive_graph = []

time = 0
while len(alive_cells) - 1:
	alive_graph.append(int(len(alive_cells)) + 100)
	for cell in alive_cells:
		celldata = cell.progress(time, food)
		food = celldata[0]
		if not celldata[1]:
			alive_cells.pop()
		
		if celldata[2]:
			alive_cells.pop()
			alive_cells.append(celllib.Cell(i, sys.argv[3], sys.argv[4]))
			alive_cells.append(celllib.Cell(i, sys.argv[3], sys.argv[4]))
			i += 1

	time += 1

print("The cells lasted for " + str(time) + " units of time")
# print(alive_graph)

print("Cells Over Time:")
termplot.plot(alive_graph)