#!/usr/bin/env python3
import unittest
import filecmp
from Treat2 import Treat2

class TestTreat2(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.In1="data/TK.csv"
#        self.Out1="Unknown"

    def test_vif(self):
        mytreat=Treat2(self.In1)
        ofile=mytreat.vif()
        self.Out1=self.In1.replace(".csv","_vif.csv")
        self.assertEqual(ofile,self.Out1)

    def test_cmp_vif(self):
        mytreat=Treat2(self.In1)
        ofile=mytreat.vif()
        result=filecmp.cmp(ofile,ofile+".T2")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
