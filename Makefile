all: treat1_test treat2_test

treat1_test:
	python Treat1_test.py

#treat2_test:
#	python Treat2_test.py

.PHONY: all treat1_test treat2_test
