import random
import string


def MurmurHash3_32(key, seed=1):
    # Some hyper-parameters:
    r2 = 13
    m = 5
    n = int('0xe6546b64', 16)

    keySize = len(key)
    hashh = seed

    # Get converted hexademical values in 4 byte chunks
    # Because 4 byte = 32 bits. Remember our generated hashes
    # need to be 32 bit max.
    fourByteChunks, remainingBytes = getChunks(key)

    # Deal with 4 Byte Chunks -- Words
    for eachChunk in fourByteChunks:
        k = Scramble(int(eachChunk, 16))
        hashh = XOR(hashh, k)
        hashh = ROTL(hashh, r2)
        hashh = MULT(hashh, m) + n

    # For remainingByte that couldn't be in 4 Byte Chunk
    if remainingBytes:
        if len(remainingBytes) == 2:
            r = int(remainingBytes, 16) << 16
        elif len(remainingBytes) == 4:
            r = int(remainingBytes, 16) << 8
        else:
            r = int(remainingBytes, 16)

        k = Scramble(r)
        hashh = hashh ^ k

    hashh = hashh ^ keySize

    # Final Evalanche -- adding more randomness
    hashh = XOR(hashh, (hashh >> 16))
    hashh = MULT(hashh, int('0x85ebca6b', 16))
    hashh = XOR(hashh, (hashh >> 13))
    hashh = MULT(hashh, int('0xc2b2ae35', 16))
    hashh = XOR(hashh, (hashh >> 16))

    return hashh


def Scramble(k):
    ''' Just for scrabbling and distributing bits evenly'''
    # These are hyper-parameters that were found to be optimal
    c1 = int('0xcc9e2d51', 16)
    c2 = int('0x1b873593', 16)
    r1 = 15

    k = MULT(k, c1)
    k = ROTL(k, r1)
    k = MULT(k, c2)

    return k


def MULT(x, y):
    result = x*y
    # Overflow Protection --> incase goes over 32 bits
    if(abs(x*y) > (2 ** 31 - 1)):
        return result % (2**32)
    else:
        return result


def XOR(x, y):
    result = x ^ y
    # Overflow Protection --> incase goes over 32 bits
    if(abs(result) > (2 ** 31 - 1)):
        return result % (2**32)
    else:
        return result


def ROTL(val, bits):
    rol = val
    r_bits = bits
    result = (rol << r_bits) | (rol >> (32 - r_bits))
    # Overflow Protection --> incase goes over 32 bits
    if(abs(result) > (2 ** 31 - 1)):
        return result % (2**32)
    else:
        return result

def getChunks(key):
    ''' Dividing the key into byte sized chunks'''
    hex_string = key.encode().hex()
    length = len(hex_string)
    sep = length%8
    return [hex_string[i:i+8] for i in range(0, length-sep, 8)], hex_string[-sep:]
