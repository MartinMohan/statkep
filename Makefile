all: treat1_test treat2_test data/TCE1.csv.T1.timestamp


# Only generate new file if T(1) file has changed
data/TCE1.csv.T1.timestamp: data/TCE1.csv.T1
	./GenFiles.py --filename Treat1.py
	touch data/TCE1.csv.T1.timestamp

data/TK_vif.csv.T2.timestamp: data/TK_vif.csv.T2
	./GenFiles.py --filename Treat2.py --vif
	touch data/TK_vif.csv.T2.timestamp


# Only generate new file if T1 file has changed

treat1_test:
	python Treat1_test.py -v

treat2_test:
	python Treat2_test.py -v

.PHONY: all treat1_test treat2_test
