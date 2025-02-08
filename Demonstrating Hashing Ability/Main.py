from filterFileHandlerAdler32 import *
from BloomFilter import *
import matplotlib



#Generate a filter from a database file and input it to a 
exampleFilter = generatePasswordFilterFile('testData1.txt', 'MainFilterFile.txt')
#exampleFilter = loadFilterFile('MainFilterFile-10000000-1-7-95850584.txt')

''' These are definitely present in the database '''
#dragon - AF8978B1797B72ACFFF9595A5A2A373EC3D9106D
#password - 5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8

# Let us check
exampleFilter.check('dragon')
exampleFilter.check('password')
exampleFilter.check('passwoord')
exampleFilter.check('password1')
exampleFilter.check('passwod')
exampleFilter.check('cartoon23')


''' -------------- Check Filter Details ---------------- '''
