import zlib
import string
import random
from MurmurHash3 import *
from filterFileHandler import generateFilterFile as gFF
from filterFileHandler import loadFilterFile as lFF
from filterFileHandlerAdler32 import generateFilterFile as gFFA
from filterFileHandlerAdler32 import loadFilterFile as lFFA

#---------------- Testing Hash Functions --------------------- #

def findChangedBit(n, x):
    # Calculate xor of n and x
    XOR = n ^ (x)
    # Count set bits in xor value
    result = bin(XOR).count("1")
    # Return the result
    return result


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



def testMurmur():
    average = 0
    prev = MurmurHash3_32('a3de', 1)
    n = 4

    for i in range(0, 10000):
        '''Basically, we are testing the bit change between over 10000 random strings
        of varying lenght, and we see that the average bit change between each hash
        is about 50% of average, verifying that this a decent and well spread hash
        function'''

        if i == 2000:
            n = 6
        if i == 4000:
            n = 8
        if i == 6000:
            n = 10
        if i == 8000:
            n = 12
        key = randomString(n)  # Generate Random String
        hashh = MurmurHash3_32(key, 1)         # Generate its Hash
        # Find average bit change with previous hash value
        average += (findChangedBit(prev, hashh)/32)*100
        prev = hashh

    print("Murmur Hash: average bit change was " + str(average/(10000)))

def testAdler():
    average = 0
    prev = zlib.adler32('a3de'.encode())
    n = 4

    for i in range(0, 10000):
        '''Basically, we are testing the bit change between over 10000 random strings
        of varying lenght, and we see that the average bit change between each hash
        is about 50% of average, verifying that this a decent and well spread hash
        function'''

        if i == 2000:
            n = 6
        if i == 4000:
            n = 8
        if i == 6000:
            n = 10
        if i == 8000:
            n = 12
        key = randomString(n)  # Generate Random String
        hashh = zlib.adler32(key.encode())         # Generate its Hash
        # Find average bit change with previous hash value
        average += (findChangedBit(prev, hashh)/32)*100
        prev = hashh

    print("Adler Hash: average bit change was " + str(average/(10000)))


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



print('----------------- TESTING MURMUR3 --------------------')
testMurmur()
gFF('TestData.txt', 'MainFilterFile.txt', 0.01)


print('----------------- TESTING ADLER32 --------------------')
testAdler()
gFFA('TestData.txt', 'MainFilterFile.txt', 0.01)

    

