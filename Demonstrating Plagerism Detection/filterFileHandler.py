from BloomFilter import *

import time
'''Generate a Boom Filter from a Input Database'''

def generateFilterFile(inputFile, outputFile, errorProb):
    # Load Input Data in Correct Format (i.e. 1 String per line!)
    data = open(inputFile)

    # Find File Length
    for i, l in enumerate(data):  pass
    length = i + 1
    data.seek(0)
        
    # Specification of Filter --> items & error-probability required
    Filter = BloomFilter()
    Filter.generateEmptyFilter(length, errorProb)

    # Populate Filter
    print('')
    listData = [data.readline()for line in range(0, length)]

    for line in listData:
        Filter.add(line.strip())

    print('Number of Collisions While Generating Filter: ' + str(Filter.collisions))
    print('')
    
    # Output a file
    Filter.sendToFile(outputFile)

    return Filter


def loadFilterFile(inputFile, numItems = 0, errorProb = 0):
    Filter = BloomFilter()   # Generate a filter object

    # If filter specifications not defined, assume in inputFile name
    if numItems == 0 and errorProb == 0:        Filter.loadFromFile(inputFile)
    # else, pass specifications as arguments
    else: Filter.loadFromFile(inputFile, numItems, errorProb)

    return Filter

