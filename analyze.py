import matplotlib.pyplot as plt
import numpy as np
from utils import isPrime, getExpectedUnigramDistribution, getUnigramDistribution, getUnigramDistributionDifference, getUnigramDistributionShape

class Analyze:
    def __init__(self, ciphertext, graphDist, reportFindings):
        self.ct = ciphertext
        self.features = {}
        self.graphDist = graphDist
        self.reportFindings = reportFindings

    def analyze(self):
        self.findFeatures()

        if self.reportFindings:
            self.reportFeatures()
            self.checkShiftLikeliness()
            self.checkMaLikeliness()
            self.checkVigsLikeliness()
            self.checkPlayfairLikeliness()
            self.checkTranspoLikeliness()

        if self.graphDist:
            self.graphUnigramDistribution()

        return self.features

    def findFeatures(self):
        # Number of letters in ciphertext
        ctLength = len(self.ct)
        self.features['length'] = ctLength

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
        self.features['unigramDist'] = unigramDist

        # Unigram frequency distribution shape (normal, shifted, scrambled, uniform)
        self.features['unigramDistShape'] = getUnigramDistributionShape(unigramDist)

    def reportFeatures(self):
        # Report length of ciphertext and any missing letters
        print 'Length of ciphertext: %s letters' % self.features['length']
        if 'missingLetters' in self.features:
            ml = self.features['missingLetters']
            print '%s letters are missing from ciphertext: %s' % (str(len(ml)), ', '.join(ml))
        else:
            print 'All 26 letters are present.'

        # Report possible shapes of unigram frequency distribution
        print 'Unigram frequency distribution appears to be: %s' % ', '.join(self.features['unigramDistShape'])

    def graphUnigramDistribution(self):
        letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        ticks = np.arange(len(letters))
        plt.bar(ticks, self.features['unigramDist'], 0.35, label='Actual')
        plt.bar(ticks + 0.35, getExpectedUnigramDistribution(), 0.35, label='Expected')
        plt.xticks(ticks + 0.35, letters)
        plt.ylabel('Frequency')
        plt.title('Unigram Frequency Distribution')
        plt.legend()
        plt.show()

    def checkShiftLikeliness(self):
        print "\nSHIFT CIPHER:"
        if 'shifted' in self.features['unigramDistShape']:
            print "\tLikely, because the unigram distribution appears shifted."
        else:
            print "\tUnlikely, because the unigram distribution does not appear shifted."

    def checkMaLikeliness(self):
        print "\nMA CIPHER:"
        if 'scrambled' in self.features['unigramDistShape']:
            print "\tLikely, because the unigram distribution appears scrambled."
        else:
            print "\tUnlikely, because the unigram distribution does not appear scrambled."

    def checkVigsLikeliness(self):
        print "\nVIGENERE CIPHER:"
        if 'uniform' in self.features['unigramDistShape']:
            print "\tPossibly, because the unigram distribution appears flat."
        else:
            print "\tUnlikely, because the unigram distribution does not appear flat."

    def checkPlayfairLikeliness(self):
        print "\nPLAYFAIR CIPHER:"
        if self.features['length'] % 2 != 0:
            print "\tUnlikely, because the text is an uneven length."
        elif 'missingLetters' not in self.features:
            print "\tUnlikely, because all 26 letters are present in the text."
        else:
            if 'uniform' in self.features['unigramDistShape']:
                print "\tLikely, because the unigram distribution appears uniform, number of letters is even, and at least one letter is not present in the text."
            else:
                print "\tUnlikely, because the unigram distribution does not appear flat."

    def checkTranspoLikeliness(self):
        print "\nTRANSPOSITION CIPHER:"
        if isPrime(self.features['length']):
            print "\tUnlikely, because length of text is a prime number."
        else:
            if 'normal' in self.features['unigramDistShape']:
                print "\tLikely, because the unigram distribution appears normal."
            else:
                print "\tUnlikely, because the unigram distribution does not appear normal."
