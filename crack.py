from utils import getUnigramDistribution, getUnigramDistributionDifference
import re

class CrackShift:
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def crack(self):
        # TODO: rewrite for efficiency - text doesn't need to be rewritten each
        # time and re-counted. Diffs array can just be shifted.
        diffs = []
        for i in range(1, 26):
            shiftedText = self.getShiftedText(i)
            textDist = getUnigramDistribution(shiftedText)
            distDiff = getUnigramDistributionDifference(textDist)
            diffs.append(distDiff)

        bestShifts = self.getBestShifts(diffs)
        print '\nBest shifts found (best one first): +%i, +%i, +%i\n' % (bestShifts[0], bestShifts[1], bestShifts[2])

        for shift in bestShifts:
            print 'Results for +%i: %s\n' % (shift, self.getShiftedText(shift).lower())

    def getShiftedText(self, shiftNum):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        shiftedText = ''
        for let in self.ct:
            currIndex = letters.index(let)
            newIndex = (currIndex + shiftNum) % len(letters)
            shiftedText += letters[newIndex]
        return shiftedText

    def getBestShifts(self, diffs):
        bestShifts = []
        for i in range(3):
            index = diffs.index(min(diffs))
            bestShifts.append(index + 1)
            diffs[index] = 1000000
        return bestShifts

class CrackMa:
    def __init__(self, ciphertext):
        self.ct = ciphertext


class CrackVigs:
    def __init__(self, ciphertext, keyLength=None):
        self.ct = ciphertext
        self.repetitions = {}
        self.table = []
        self.minKey = 2
        self.maxKey = 17
        self.keyLength = keyLength

    def crack(self):
        if not self.keyLength:
            # Build table of trigraph repetition distance factors
            self.buildRepetitionsDict()
            self.buildFactorsTable()

            # Choose most probable keyword length
            keyLengths = self.chooseBestKeyLengths()
        else:
            keyLengths = [self.keyLength]

        # Crack series of shift ciphers given keyword length
        for key in keyLengths:
            shiftCiphers = self.breakTextIntoShiftCiphers(key)
            solvedCiphers = self.solveShiftCiphers(shiftCiphers)
            plaintext = self.replaceText(solvedCiphers, key)

            print "\nKey length tried: ", key
            print "Found plaintext: ", plaintext

        print "\nIf none of these key lengths look right, run '$ python ciphertool.py crack vigs [keylength]' to try a different key length"

    def buildRepetitionsDict(self):
        # Get all trigraphs in text and their number of repetitions, if any
        for i in range(0, len(self.ct) - 2):
            trigraph = self.ct[i:i + 3]
            reps = re.finditer(trigraph, self.ct)
            if trigraph not in self.repetitions:
                self.repetitions[trigraph] = []
            for r in reps:
                if r.start() not in self.repetitions[trigraph]:
                    self.repetitions[trigraph].append(r.start())

        # Remove non-repeated trigraphs from list
        for trigraph in self.repetitions.keys():
            if len(self.repetitions[trigraph]) == 1:
                del self.repetitions[trigraph]

    def buildFactorsTable(self):
        # Build table (2-d array) listing trigraphs and the divisors of their separation lengths
        for trigraph in self.repetitions:
            factors = [False for j in range(self.minKey, self.maxKey + 1)] # Keywords of length 2-20
            differences = []
            for i in range(0, len(self.repetitions[trigraph]) - 1):
                differences.append(self.repetitions[trigraph][i+1] - self.repetitions[trigraph][i])
            for d in differences:
                for num in range(self.minKey, self.maxKey + 1):
                    if d % num == 0:
                        factors[num - self.minKey] = True
            self.table.append(factors)

    def chooseBestKeyLengths(self):
        factorCounts = [0 for i in range(self.minKey, self.maxKey + 1)]
        for line in self.table:
            for i in range(0, len(line)):
                if line[i]:
                    factorCounts[i] += 1
        factorCountsExpected = [len(factorCounts) / float(i + self.minKey) for i in range(0, len(factorCounts))]
        factorDifferences = [abs(factorCountsExpected[i] - factorCounts[i]) / float(factorCountsExpected[i]) for i in range(0, len(factorCounts))]

        bestKeys = []
        for i in range(3):
            index = factorDifferences.index(max(factorDifferences))
            bestKeys.append(index + self.minKey)
            factorDifferences[index] = 0
        return bestKeys

    def breakTextIntoShiftCiphers(self, keyLength):
        shifts = []
        for i in range(0, keyLength):
            cipher = ''
            for j in range(i, len(self.ct), keyLength):
                cipher += self.ct[j]
            shifts.append(cipher)
        return shifts

    def solveShiftCiphers(self, shiftCiphers):
        solvedCiphers = []
        for cipher in shiftCiphers:
            c = CrackShift(cipher)
            diffs = []
            for i in range(1, 26):
                shiftedText = c.getShiftedText(i)
                textDist = getUnigramDistribution(shiftedText)
                distDiff = getUnigramDistributionDifference(textDist)
                diffs.append(distDiff)

            bestShift = c.getBestShifts(diffs)[0]
            plaintext = c.getShiftedText(bestShift).lower()
            solvedCiphers.append(plaintext)
        return solvedCiphers

    def replaceText(self, solvedCiphers, keyLength):
        plaintext = []
        for i in range(0, keyLength):
            cipher = solvedCiphers[i]
            for j in range(0, len(cipher)):
                plaintext.insert(j * i + j + i, cipher[j])
        return "".join(plaintext)


class CrackPlayfair:
    def __init__(self, ciphertext):
        self.ct = ciphertext


class CrackTranspo:
    def __init__(self, ciphertext):
        self.ct = ciphertext
