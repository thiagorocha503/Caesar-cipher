import unittest
from model.cifra import Cifra
from model.cifraException import CifraKeyException


# noinspection SpellCheckingInspection
class CifraTest(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(Cifra.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3), "DEFGHIJKLMNOPQRSTUVWXYZABC")
        self.assertEqual(Cifra.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5), "FGHIJKLMNOPQRSTUVWXYZABCDE")
        self.assertEqual(Cifra.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10), "KLMNOPQRSTUVWXYZABCDEFGHIJ")
        self.assertEqual(Cifra.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 16), "QRSTUVWXYZABCDEFGHIJKLMNOP")
        self.assertEqual(Cifra.encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25), "ZABCDEFGHIJKLMNOPQRSTUVWXY")

        self.assertRaises(CifraKeyException, Cifra.encode, "ABC", 0)
        self.assertRaises(CifraKeyException, Cifra.encode, "ABC", 26)
        self.assertEqual(Cifra.encode("THE QUICK BROWN FOX JUMPS OVER A LAZY DOG", 1), "UIF#RVJDL#CSPXO#GPY#KVNQT#PWFS#B#MBAZ#EPH")
        self.assertEqual(Cifra.encode("THE QUICK BROWN FOX JUMPS OVER A LAZY DOG", 3), "WKH#TXLFN#EURZQ#IRA#MXPSV#RYHU#D#ODCB#GRJ")
        self.assertEqual(Cifra.encode("THE QUICK BROWN FOX JUMPS OVER A LAZY DOG", 25), "SGD#PTHBJ#AQNVM#ENW#ITLOR#NUDQ#Z#KZYX#CNF")

    def test_decode(self):
        self.assertRaises(CifraKeyException, Cifra.decode, "ABC", 0)
        self.assertRaises(CifraKeyException, Cifra.decode, "ABC", 26)

        self.assertEqual(Cifra.decode("DEFGHIJKLMNOPQRSTUVWXYZABC", 3), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(Cifra.decode("FGHIJKLMNOPQRSTUVWXYZABCDE", 5), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(Cifra.decode("KLMNOPQRSTUVWXYZABCDEFGHIJ", 10), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(Cifra.decode("QRSTUVWXYZABCDEFGHIJKLMNOP", 16), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(Cifra.decode("ZABCDEFGHIJKLMNOPQRSTUVWXY", 25), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        self.assertEqual(Cifra.decode("UIF#RVJDL#CSPXO#GPY#KVNQT#PWFS#B#MBAZ#EPH", 1), "THE#QUICK#BROWN#FOX#JUMPS#OVER#A#LAZY#DOG")
        self.assertEqual(Cifra.decode("WKH#TXLFN#EURZQ#IRA#MXPSV#RYHU#D#ODCB#GRJ", 3), "THE#QUICK#BROWN#FOX#JUMPS#OVER#A#LAZY#DOG")
        self.assertEqual(Cifra.decode("SGD#PTHBJ#AQNVM#ENW#ITLOR#NUDQ#Z#KZYX#CNF", 25), "THE#QUICK#BROWN#FOX#JUMPS#OVER#A#LAZY#DOG")
