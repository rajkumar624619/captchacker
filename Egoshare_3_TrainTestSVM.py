#!coding: utf-8

from svm import *

CRANGE = [100, 1000, 10000]
KERNEL_TYPE = [RBF]


for C in CRANGE:
    for KERNEL in KERNEL_TYPE:
        
        TRAINING_FOLDER = 'Egoshare/DBTraining'
        TEST_FOLDER = 'Egoshare/DBTest'
        VERBOSE = 0
        MODEL_FOLDER = 'Egoshare/Models'
        MODEL_FILE = "model_C="+str(C)+"_KERNEL="+str(KERNEL)+".svm"
        GENERATE_ANYWAY = 1

        execfile("Train & Test SVM.py")


raw_input()