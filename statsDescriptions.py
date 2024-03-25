import csv
import numpy 
from scipy import stats, ndimage

atmosphericFile = open("atmosphericCarbon.csv","r")
atmosphericData = csv.reader(atmosphericFile)

stormInensityFile = open("tropicalStormIntensities.csv","r")
stormIntensityData = csv.reader(stormInensityFile)

years: list = []
atmosphericMeans: list = []
stormIntensityMeans: list = []

#skip over the column headings of each csv
next(atmosphericData)
next(stormIntensityData)

for row in atmosphericData: #traverse each row in the table
    years.append(row[0])
    atmosphericMeans.append(float(row[1]))
    
for row in stormIntensityData:
    stormIntensityMeans.append(float(row[1]))
    
#convery python lists into numpy arrays used for calculations with scipy library functions
atmosphericMeans = numpy.array(atmosphericMeans)
stormIntensityMeans = numpy.array(stormIntensityMeans)

#perform calculations of yearly atmosphericMeans and atmosphericUncertainties
sampleSize = len(years)

average_of_atmosphericMeans: float = ndimage.mean(atmosphericMeans)
average_of_stormIntensityMeans: float = ndimage.mean(stormIntensityMeans)

median_of_atmosphericMeans: float = ndimage.median(atmosphericMeans)
median_of_stormIntensityMeans: float = ndimage.median(stormIntensityMeans)

mode_of_atmosphericMeans: float = stats.mode(atmosphericMeans)
mode_of_stormIntensityMeans: float = stats.mode(stormIntensityMeans)

variance_of_atmosphericMeans: float = ndimage.variance(atmosphericMeans)
variance_of_stormIntensityMeans: float = ndimage.variance(stormIntensityMeans)

standardDev_of_atmosphericMeans: float = ndimage.standard_deviation(atmosphericMeans)
standardDev_of_stormIntensityMeans: float = ndimage.standard_deviation(stormIntensityMeans)

#display x axis headings of table
headings: list = ["","Sample Size", "Mean", "Median", "Mode(s)", "Variance", "Standard Deviation"]
print(f"{headings[0]:^40}", end = "")
print(f"{headings[1]:^10}", end = "")
print(f"{headings[2]:^10}", end = "")
print(f"{headings[3]:^10}", end = "")
print(f"{headings[4]:^10}", end = "")
print(f"{headings[5]:^10}", end = "")
print(f"{headings[6]:^10}")

#display row of atmosphericData for annual atmosphericMeans
rows: list = ["Annual Atmospheric Carbon Averages", "Annual Storm Intensity Averages"]
print(f"{rows[0]:^40}", end = "")
print(f"{sampleSize:^10}", end = "")
print(f"{average_of_atmosphericMeans:^10.4f}", end = "")
print(f"{median_of_atmosphericMeans:^10.4f}", end = "")
print(f"{mode_of_atmosphericMeans[0]:^10.4f}", end = "")
print(f"{variance_of_atmosphericMeans:^10.4f}", end = "")
print(f"{standardDev_of_atmosphericMeans:^10.4f}")

print(f"{rows[1]:^40}", end = "")
print(f"{sampleSize:^10}", end = "")
print(f"{average_of_stormIntensityMeans:^10.4f}", end = "")
print(f"{median_of_stormIntensityMeans:^10.4f}", end = "")
print(f"{mode_of_stormIntensityMeans[0]:^10.4f}", end = "")
print(f"{variance_of_stormIntensityMeans:^10.4f}", end = "")
print(f"{standardDev_of_stormIntensityMeans:^10.4f}")