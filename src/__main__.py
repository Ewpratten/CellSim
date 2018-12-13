import sys
import cell as celllib
import termplot
import csv

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
max_cells = 100

alive_cells = []

# Create Cells
for i in range(0, starting_cells):
	alive_cells.append(celllib.Cell(i, sys.argv[3], sys.argv[4]))

# keep the ids incrementing
i += 1

print(str(len(alive_cells)) + " Cells have been created...\nStarting simulation")

alive_graph = []
csv_data = []

time = 0
while len(alive_cells) - 1:
	isRoom = True if len(alive_cells) <= max_cells else False
	# save data about current iteration
	alive_graph.append(int(len(alive_cells)) + 100)
	csv_data.append([time, len(alive_cells), food])
	
	for cell in alive_cells:
		celldata = cell.progress(time, food, isRoom)
		food = celldata[0]
		if not celldata[1]:
			alive_cells.pop()
		
		if celldata[2]:
			alive_cells.pop()
			alive_cells.append(celllib.Cell(i, sys.argv[3], sys.argv[4]))
			alive_cells.append(celllib.Cell(i, sys.argv[3], sys.argv[4]))
			i += 1

	time += 1
	max_cells +=  2
	print(f"Alive: {len(alive_cells)} | Max: {max_cells}", end="\r")

print("The cells lasted for " + str(time) + " units of time")
# print(alive_graph)

print("Cells Over Time:")
termplot.plot(alive_graph)

print("Exporting CSV for Graphing")
with open("./csv/output-graphing.csv", "w") as outfile:
	writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for iteration in csv_data:
		writer.writerow(iteration[1:])

print("Exporting Normal CSV")
with open("./csv/output.csv", "w") as outfile:
	writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for iteration in csv_data:
		writer.writerow(iteration)

print("Generating MatPlotLib Graph")
import matplotlib
matplotlib.use("agg")
from matplotlib import pyplot as plt
from matplotlib import style

from numpy import genfromtxt

# with open("./output.csv", 'r') as f:
# 	num_cols = len(f.readline().split())
# 	f.seek(0)
# 	data = genfromtxt(f, usecols = range(2,num_cols), delimiter=',')
data = genfromtxt('./csv/output-graphing.csv',delimiter=',')

plt.plot(data)

plt.title('Cell Generation Data')
plt.ylabel('Y axis')
plt.xlabel('Time (Hours)')

plt.savefig("output.png")

print("Done!")
exit(0)