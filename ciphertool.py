import sys
from analyze import Analyze
from crack import CrackShift, CrackMa, CrackVigs, CrackPlayfair, CrackTranspo

if __name__ == '__main__':
    # Get ciphertext and store it
    ct = open('ciphertext.txt', 'r')
    ciphertext = ''
    for line in ct.readlines():
        ciphertext += line
    ct.close()

    # Remove spaces and newlines and capitalize text
    ciphertext = ciphertext.replace('\n', '').replace(' ', '').upper()

    # Analyze ciphertext or attempt to crack a given cipher type
    if sys.argv[1] == 'analyze':
        a = Analyze(ciphertext, graphDist=True, reportFindings=False)
        a.analyze()
    elif sys.argv[1] == 'crack':
        if sys.argv[2] == 'shift':
            c = CrackShift(ciphertext)
            c.crack()
        elif sys.argv[2] == 'ma':
            CrackMa(ciphertext)
        elif sys.argv[2] == 'vigs':
            c = CrackVigs(ciphertext)
            c.crack()
        elif sys.argv[2] == 'playfair':
            CrackPlayfair(ciphertext)
        elif sys.argv[2] == 'transpo':
            CrackTranspo(ciphertext)
        else:
            print 'Unrecognized cipher name. Try shift, ma, vigs, playfair, or transpo'
    else:
        print 'Unrecognized command. Run $ python ciphertool.py analyze or $ python ciphertool.py crack [cipher]'
