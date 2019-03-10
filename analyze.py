import matplotlib.pyplot as plt
import numpy as np

class Analyze:
    def __init__(self, ciphertext, graphDist=True):
        self.ct = ciphertext
        self.features = {}
        self.graphDist = graphDist

    def analyze(self):
        self.findFeatures()
        self.reportFeatures()

        self.checkShiftLikeliness()
        self.checkMaLikeliness()
        self.checkVigsLikeliness()
        self.checkPlayfairLikeliness()
        self.checkTranspoLikeliness()

        return self.features

    def findFeatures(self):
        # Number of letters in ciphertext
        ctLength = len(self.ct)
        self.features['length'] = str(ctLength) + ' letters'

        # If all 26 letters are present in ciphertext or some are missing
        missingLetters = []
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if letter not in self.ct:
                missingLetters.append(letter)
        if len(missingLetters) > 0:
            self.features['missingLetters'] = missingLetters

        # Unigram frequency distribution of ciphertext
        unigramDist = []
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            unigramDist.append(self.ct.count(letter) / float(ctLength))
        self.features['unigramFreqDist'] = unigramDist

        # TODO: store if unigram frequency distribution is normal/shifted/scrambled/uniform

    def getFeatures(self):
        return self.features

    def reportFeatures(self):
        # Report length of ciphertext and any missing letters
        print 'Length of ciphertext: %s' % self.features['length']
        if 'missingLetters' in self.features:
            ml = self.features['missingLetters']
            print '%s letters are missing from ciphertext: %s' % (str(len(ml)), ', '.join(ml))
        else:
            print 'All 26 letters are present.'

        # Graph unigram frequency distribution
        # TODO graph against expected distribution
        if self.graphDist:
            letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            ticks = np.arange(len(letters))
            plt.bar(ticks, self.features['unigramFreqDist'], align='center', alpha=0.5)
            plt.xticks(ticks, letters)
            plt.ylabel('Frequency')
            plt.title('Unigram Frequency Distribution')
            plt.show()

    def checkShiftLikeliness(self):
        # TODO: a shifted unigram frequency dist is a clue of shifts
        return

    def checkMaLikeliness(self):
        return

    def checkVigsLikeliness(self):
        # If likely, report possible key lengths
        return

    def checkPlayfairLikeliness(self):
        # Playfair must have an even number of letters and may not have all 26 letters present
        return

    def checkTranspoLikeliness(self):
        # If likely, report possible factors?
        return
