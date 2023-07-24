#!/usr/bin/env python3
import unittest
from Treat1 import Treat1

class TestTreat1(unittest.TestCase):
    #    __init__
    def test_get_args(self):
        In1="data_test/TCE.csv"
        In2="data_test/KOI.csv"
        Out1=In1.replace('TCE','TCE1')
        Out2=In1.replace('TCE','TK')

        mytreat=Treat1(In1,In2)
#        print ("mytreat.TCE1=%s"%mytreat.TCE1)
        rtn="In: "+In1+" "+In2+" Out: "+Out1+" "+Out2
        self.assertEqual(mytreat.get_args(), rtn)

if __name__ == '__main__':
    unittest.main()
