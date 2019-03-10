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

class CrackShift:
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def crack(self):
        diffs = []
        for i in range(1, 26):
            shiftedText = self.getShiftedText(i)
            textDist = self.getUnigramDist(shiftedText)
            distDiff = self.getUnigramDistDiff(textDist)
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

    def getUnigramDist(self, shiftedText):
        unigramDist = []
        ctLength = float(len(shiftedText))
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            unigramDist.append(shiftedText.count(letter) / ctLength)
        return unigramDist

    def getUnigramDistDiff(self, uniDist):
        difference = 0
        for expectedFreq, actualFreq in zip(expectedUniDist, uniDist):
            difference += abs(expectedFreq - actualFreq) / expectedFreq
        return difference

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
