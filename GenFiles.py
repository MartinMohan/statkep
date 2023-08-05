#!/usr/bin/env python3
#   author:martinmhan@yahoo.com date:  04/08/2023
#   Copyright (C) <2023>  <Martin Mohan>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
import argparse,sys,re
import shutil
from argparse import RawTextHelpFormatter
from Treat1 import Treat1
from Treat2 import Treat2
#from Treat3 import Treat3
#from Treat4 import Treat4
#from Treat5 import Treat5

class GenFiles():
    """ 
    TCE.csv: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=tce
    KOI.csv: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=koi

    Copy output files from each treatment. These are used as test files to compare against file generated.
    TCE.csv (34,000+ cases) is cleaned and saved as TCE1.csv (34,000+ cases)
    TCE.scv (34,000+ cases) is merged with corresponding lines in KOI.csv (8,000+ cases) and saved  as TK.csv(8,000+ cases)

    """
    def __init__(self,fname="python1.py"):
        """
        The TCE file name is generated from the input file
        """
#        self.progname=fname
# Make this a wrapper?
    def copyfile(self,ifile,ofile):
        shutil.copyfile(ifile,ofile) 
        print("Copy %s to %s"%(ifile,ofile))

    def setTestFiles(self,fname="Treat1.py"):
        if(fname=="Treat0.py"): # Are these correct NASA files
            self.copyfile("data/TCE.csv","data/TCE1.csv"+".T0")
            self.copyfile("data/KOI.csv","data/TK.csv"+".T0")
        elif(fname=="Treat1.py"):
            mytreat=Treat1()
            f1,f2=mytreat.get_ofiles()
            self.copyfile(f1,f1+'.T1')
            self.copyfile(f2,f2+".T1")
        elif(fname=="Treat2.py"):
            mytreat=Treat2()
            f1=mytreat.vif()
            #f1=mytreat.get_ofiles()
            self.copyfile(f1,f1+".T2")
        else:
            print("Error unknown program %s"%fname)
#        return(of1,of2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Input Treatment file and generate output file. This output file is copied to another file with a suffix e.g '.T1', 'T2'....This can be used to compare output vs expected output (default: %(default)s)"
,formatter_class=RawTextHelpFormatter)

    parser.add_argument( "--filename", type=str, default="Treat1.py", help="The name of Treat program \n \
Treat0.py cp TCE.csv/KOI.csv->TCE1.csv.T0,KOI.csv.T0\n \
Treat1.py TCE.csv/KOI.csv->TCE1.csv(.T1)/TK.csv(.T1) (clean/merge)\n \
Treat2.py --vif TK.csv -> TK_vif.csv(T2)\n \
Treat3.py TK_vif -> TK_vif_100g_None_Tpot.py (tpot)\n \
Treat4.py or Treat5.py ")

#    parser = argparse.ArgumentParser(description=mydesc,formatter_class=RawTextHelpFormatter)


    argv=parser.parse_args()
    mytreat=GenFiles()
    mytreat.setTestFiles(argv.filename)
#    mytreat=setTestFile(argv.filename)
#    mytreat=GetFiles(argv.tcefile)
