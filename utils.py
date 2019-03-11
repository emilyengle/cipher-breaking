expectedUniDist = [ # in alphabetical order
    0.0804,
    0.0148,
    0.0334,
    0.0382,
    0.1249,
    0.024,
    0.0187,
    0.0505,
    0.0757,
    0.0016,
    0.0054,
    0.0407,
    0.0251,
    0.0723,
    0.0764,
    0.0214,
    0.0012,
    0.0628,
    0.0651,
    0.0928,
    0.0273,
    0.0105,
    0.0168,
    0.0023,
    0.0166,
    0.0009
]

def getExpectedUnigramDistribution():
    return expectedUniDist

def getUnigramDistributionDifference(dist):
    difference = 0
    for expectedFreq, actualFreq in zip(expectedUniDist, dist):
        difference += abs(expectedFreq - actualFreq) / expectedFreq
    return difference

def getUnigramDistribution(text):
    dist = []
    textLength = float(len(text))
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dist.append(text.count(letter) / textLength)
    return dist

def isPrime(num):
    # We're working with relatively small numbers, so this doesn't need to be great
    if num < 2:
        return False
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    for i in range(11, num / 2, 2):
        if num % i == 0:
            return False
    return True

def getUnigramDistributionShape(dist):
    possibleShapes = []

    if _testIfNormal(dist):
        possibleShapes.append('normal')
    if _testIfShifted(dist):
        possibleShapes.append('shifted')
    if _testIfUniform(dist):
        possibleShapes.append('uniform')
    if _testIfScrambled(dist):
        possibleShapes.append('scrambled')

    return possibleShapes

def _testIfShifted(dist):
    # TODO
    return

def _testIfScrambled(dist):
    # TODO
    return

def _testIfNormal(dist):
    # TODO
    return

def _testIfUniform(dist):
    # TODO
    return
