from filterFileHandler import *
from BloomFilter import *


'''Generate a filter from a database file and output it to a file'''
exampleFilter = generateFilterFile('BBCTextCleaned.txt', 'MainFilterFile.txt', 0.001)


'''Load pre-existing filter'''
exampleFilter = loadFilterFile('MainFilterFile-43402-1-10-624024.txt')


def fileCheck(inputFile, Filter):
    count = 0
    matches = 0
    file = open(inputFile)

    for i, l in enumerate(file):  pass
    length = i + 2
    file.seek(0)
    
    for line in range(0, length):
        data = (file.readline()).strip()
        if Filter.check(data): matches += 1
        count += 1
    print('Document was about ' + str(int((matches/count)*100)) + '% plagerised')


# Let us check
fileCheck('SampleDoc.txt', exampleFilter)                        
