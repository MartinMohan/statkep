#!/usr/bin/env python3
import unittest
import filecmp
from Treat1 import Treat1

class TestTreat1(unittest.TestCase):

    def setUp(self):
        #        print("setUp")
        self.In1="data/TCE.csv"
        self.In2="data/KOI.csv"
        self.Out1="data/TCE1.csv"
        self.Out2="data/TK.csv"

    def test_fnames(self):
        mytreat=Treat1(self.In1,self.In2)
        self.assertEqual(mytreat.get_ofiles(),(self.Out1,self.Out2) )

    def test_fcontent(self):
        mytreat=Treat1(self.In1,self.In2)
        print("diff %s %s"%(self.Out1,self.Out1+".T1"))
        result=filecmp.cmp(self.Out1,self.Out1+".T1")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
