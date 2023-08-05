#!/usr/bin/env python3
import unittest
from Treat1 import Treat1

class TestTreat1(unittest.TestCase):
    def test_get_ofiles(self):
        In1="data_test/TCE.csv"
        In2="data_test/KOI.csv"
        Out1=In1.replace('TCE','TCE1')
        Out2=In1.replace('TCE','TK')

        mytreat=Treat1(In1,In2)
        print("In: %s %s\nOut: %s %s"%(In1,In2,Out1,Out2))
        self.assertEqual(mytreat.get_ofiles(),(Out1,Out2) )

if __name__ == '__main__':
    unittest.main()
