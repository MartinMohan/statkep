#!/usr/bin/env python3
import unittest
import filecmp
from Treat2 import Treat2

class TestTreat2(unittest.TestCase):

    def setUp(self):
        self.In1="data/TK.csv"
#        self.Out1="Unknown" # depends on arguments passed
    def test_vif_fname(self):
        mytreat=Treat2(self.In1)
        ofile=mytreat.vif()
        self.Out1=self.In1.replace(".csv","_vif.csv")
        self.assertEqual(ofile,self.Out1)
    def test_cap1_fname(self):
        mytreat=Treat2(self.In1)
        ofile=mytreat.cap1()
        self.Out1=self.In1.replace(".csv","_cap1.csv")
        self.assertEqual(ofile,self.Out1)
    def test_cap2_fname(self):
        mytreat=Treat2(self.In1)
        ofile=mytreat.cap2()
        self.Out1=self.In1.replace(".csv","_cap2.csv")
        self.assertEqual(ofile,self.Out1)
    def test_vif_fcontent(self):
        mytreat=Treat2(self.In1)
        ofile=mytreat.vif()
        result=filecmp.cmp(ofile,ofile+".T2")
        self.assertTrue(result)
#    def test_cap2_fcontent(self):
#        mytreat=Treat2(self.In1)
#        ofile=mytreat.cap2()
#        result=filecmp.cmp(ofile,ofile+".T2")
#        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
