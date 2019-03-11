from utils import getUnigramDistribution, getUnigramDistributionDifference

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
    def __init__(self, ciphertext):
        self.ct = ciphertext


class CrackPlayfair:
    def __init__(self, ciphertext):
        self.ct = ciphertext


class CrackTranspo:
    def __init__(self, ciphertext):
        self.ct = ciphertext
