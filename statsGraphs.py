import matplotlib.pyplot as plt
import csv
import numpy

atmosphericFile = open("atmosphericCarbon.csv","r")
atmosphericData = csv.reader(atmosphericFile)

stormInensityFile = open("tropicalStormIntensities.csv","r")
stormIntensityData = csv.reader(stormInensityFile)

atmosphericMeans: list = []
stormIntensityMeans: list = []
years: list = []

#skip over the column headings of each csv
next(atmosphericData)
next(stormIntensityData)

for row in atmosphericData: #traverse each row in the table
    years.append(row[0])
    atmosphericMeans.append(float(row[1]))
    
for row in stormIntensityData:
    stormIntensityMeans.append(float(row[1]))

atmosphericData = numpy.array(atmosphericMeans)
stormIntensityData = numpy.array(stormIntensityMeans)

histogram, plots = plt.subplots(2,3) #returns figure, array of plots

carbonGraph = plots[0,0]
stormsGraph = plots[0,1]
correlationGraph_partA = plots[0,2]
correlationGraph_partB = correlationGraph_partA.twinx()
carbonBoxPlot = plots[1,0]
stormsBoxPlot = plots[1,1]

carbonGraph.set_xlabel('Amount of Atmospheric Carbon Annually (PPM)')
carbonGraph.set_ylabel('Frequency', color='tab:red')

stormsGraph.set_xlabel('Tropical Storm Inensity') 
stormsGraph.set_ylabel('Frequency', color='tab:blue')

yearsToLabel = [int(year) for year in years if int(year) % 5 == 0]

correlationGraph_partA.set_xlabel('Years') 
correlationGraph_partA.set_ylabel('Atmospheric Carbon (PPM)', color='tab:red')
correlationGraph_partA.set_xticklabels(yearsToLabel)
correlationGraph_partB.set_ylabel('Storm Intensity', color='tab:blue')

carbonToLabel = [330+13*i for i in range(7)]

carbonBoxPlot.set_xlabel('Amount of Atmospheric Carbon Annually (PPM)', color='tab:red')
carbonBoxPlot.set_xticklabels(carbonToLabel)
carbonBoxPlot.set_yticklabels(' ')
stormsBoxPlot.set_xlabel('Tropical Storm Intensity', color='tab:blue')
stormsBoxPlot.set_yticklabels(' ')

carbonGraph.hist(atmosphericMeans, color='tab:red')
stormsGraph.hist(stormIntensityMeans, color='tab:blue')
correlationGraph_partA.plot(atmosphericMeans, color='tab:red')
correlationGraph_partB.plot(stormIntensityMeans)
carbonBoxPlot.boxplot(atmosphericMeans, vert=False)
stormsBoxPlot.boxplot(stormIntensityMeans, vert=False)

plt.show()