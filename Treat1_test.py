#!/usr/bin/env python3
import unittest
import filecmp
from Treat1 import Treat1

class TestTreat1(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.In1="data/TCE.csv"
        self.In2="data/KOI.csv"
        self.Out1=self.In1.replace('TCE','TCE1')
        self.Out2=self.In1.replace('TCE','TK')

    def test_get_ofiles(self):
        mytreat=Treat1(self.In1,self.In2)
        self.assertEqual(mytreat.get_ofiles(),(self.Out1,self.Out2) )

    def test_cmp_ofiles(self):
        mytreat=Treat1(self.In1,self.In2)
        result=filecmp.cmp(self.Out1,self.Out1+".T1")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
