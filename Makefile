#all: treat1_test treat2_test data/TCE1.csv.T1.timestamp
all: treat1_test treat2_test timestamps

timestamps: data/TCE1.csv.T1.timestamp data/TK_vif.csv.T2.timestamp data/TK_cap1.csv.T2.timestamp
#timestamps: data/TCE1.csv.T1.timestamp data/TK_vif.csv.T2.timestamp data/TK_cap1.csv.T2.timstamp data/TK_cap2.csv.T2.timstamp

# Only generate new file if T(1) file has changed
# If generating new file then creat the file against which it will be compared.
#eg. cp data/TCE1.csv data/TCE1.csv.T1

data/TCE1.csv.T1.timestamp: data/TCE1.csv.T1
	#./GenFiles.py --filename Treat1.py
	./Treat1.py
	touch data/TCE1.csv.T1.timestamp

data/TK_vif.csv.T2.timestamp: data/TK_vif.csv.T2
#	./GenFiles.py --filename Treat2.py --vif
	./Treat2.py --vif
	touch data/TK_vif.csv.T2.timestamp

data/TK_cap1.csv.T2.timestamp: data/TK_cap1.csv.T2
#	./GenFiles.py --filename Treat2.py --cap1
	./Treat2.py --cap1
	touch data/TK_cap1.csv.T2.timestamp

##eg. cp data/TK_cap2.csv data/TK_cap2.csv.T2
#data/TK_cap2.csv.T2.timestamp: data/TK_cap2.csv.T2
#	./Treat2.py --cap2
#	touch data/TK_cap2.csv.T2.timestamp

# Only generate new file if T1 file has changed

treat1_test:
	python Treat1_test.py -v

treat2_test:
	python Treat2_test.py -v

.PHONY: all treat1_test treat2_test
