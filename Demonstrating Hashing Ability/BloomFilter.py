import math
from bitarray import bitarray
import hashlib
from MurmurHash3 import *

class BloomFilter(object): 
  
    def __init__(self):
        pass

    def loadFromFile(self, filename, numItems = -1, errorProb = -1):
        if numItems == -1 and errorProb == -1:
          assert type(filename) == str and filename.split('.')[1] and filename.split('-')[4],
          '''The filename should be a string with the relevant extension added, as well necessary details \
          if only the filename is provided i.e. in the format: 'somestring-#items-#errorProb-#hashes-#bitarraysize.txt' '''

          filterinfo = ((filename.split('.'))[0]).split('-')[1:]
          self.numItems = int(filterinfo[0])
          self.errorProb = int(filterinfo[1])/100

        else:
          assert type(filename) == str and filename.split('.')[1], '''The filename should be a string with the relevant extension added i.e. 'somestring.txt' '''
          assert 0 < errorProb < 1 and type(errorProb) == float, 'Error Probability must be an integer between 0 and 1!'
          assert type(numItems) == int and numItems > 0, \
               'Number of expected items must be an integer greater than 0'

          self.numItems = numItems
          self.errorProb = errorProb
 

        self.bitArraySize = self.getBitArraySize(self.numItems, self.errorProb)
        self.hashCount = self.getOptimumHashCount(self.bitArraySize, self.numItems)

        data = open(filename, 'rb')
        
        self.bitArray = bitarray()
        self.bitArray.fromfile(data)
        self.bitArraySize += self.bitArray.fill()


        print('------------- Loaded Filter Details -------------- ')
        print('Capacity: ' + str(self.numItems))
        print('Allowable Error: ' + str(self.errorProb*100) + '%')
        print('Bit-Array Size: ' + str(self.bitArraySize))
        print('HashesPerItem: ' + str(self.hashCount))
        print('------------------------------------------- ')
        print(' ')

    def sendToFile(self, outFile):
      out = open(outFile.split('.')[0] + '-' + str(self.numItems) + '-' + str(int(self.errorProb*100)) + '-' + str(self.hashCount) + '-' + str(self.bitArraySize) + '.txt' , 'wb')
      self.bitArray.tofile(out)
      out.close()
  
   
    def generateEmptyFilter(self, numItems, errorProb):
        assert 0 < errorProb < 1, 'Error Probability must lie between 0 and 1!'
        assert type(numItems) == int and numItems > 0, \
               'Number of expected items must be an integer greater than 0'

        self.numItems = numItems
        self.errorProb = errorProb
        self.collisions = 0
        
        # Size of BloomFilter Array
        self.bitArraySize = self.getBitArraySize(self.numItems, self.errorProb)

        # Number of Hashes we'll be needing for each item
        self.hashCount = self.getOptimumHashCount(self.bitArraySize, numItems)
     
        # Initialize bit array for storing hashed results   
        self.bitArray = bitarray(self.bitArraySize)

        # Setting the whole array to 0 initially
        self.bitArray.setall(0)
        self.bitArraySize += self.bitArray.fill()

        
        print('------------- New Filter Details -------------- ')
        print('Capacity: ' + str(numItems))
        print('Allowable Error: ' + str(errorProb*100) + '%')
        print('Bit-Array Size: ' + str(self.bitArraySize))
        print('HashesPerItem: ' + str(self.hashCount))
        print('------------------------------------------- ')
        print(' ')
  

    def add(self, item): 
        ''' Adding item to the filter '''
        '''
        digests = [MurmurHash3_32(item, i) for i in range(1, self.hashCount+1)]
        for d in digests: self.bitArray[d] = True
        '''
        coll = 0
        for i in range(1, self.hashCount+1): 
            h = MurmurHash3_32(item, i) % self.bitArraySize # Generate Hash
  
            # set the bit True in bit_array 
            if self.bitArray[h]: coll += 1
            else: self.bitArray[h] = True
        if coll >= 7: self.collisions += 1
  
    def check(self, item): 
        ''' 
        Check for existence of an item in filter 
        '''
        #Generate SHA1 Hash
        item = hashlib.sha1(item.encode())
        item = (item.hexdigest()).upper()
        for i in range(1, self.hashCount+1): 
                h = MurmurHash3_32(item, i) % self.bitArraySize # Generate Hash2

                    # if any of bit is False then, then it means
                    # it isn't in the filter, and hence, is not present/taken
                if self.bitArray[h] == False:
                    print('Definitely Not Present!')
                    return False
        # Otherwise, it maybe taken/present
        print('Might Be There!')
        return True

    # These are based on a mathematical analysis done in founding paper  
    @classmethod
    def getBitArraySize(self, n, p): 
        ''' n = number of expected elements, p = error probability'''
        m = 8*math.ceil((n * math.log(p)) / math.log(1 / math.pow(2, math.log(2)))/8)
        return m 
  
    @classmethod
    def getOptimumHashCount(self, m, n):
        ''' n = number of expected elements, m = bit array size'''
        k = round((m/n) * math.log(2))
        return k

    @classmethod
    def getNumItems(self, m, p, k):

        n = math.ceil(m / (-k / math.log(1 - math.exp(math.log(p) / k))))
        return n
        
