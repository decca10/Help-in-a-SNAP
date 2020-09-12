#########################################################
# Py_Reference.py
#   - Custom functions for all named functions in SNAP datasets.
#
# These functions were moved into this file
#   for reuse and to reduce Notebook complexity.
#########################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

################################
        #2007 Datasets
################################

unit07_demo= pd.read_csv('./data/07_DataDict/UNIT_Demo.csv')
unit07_assets=pd.read_csv('./data/07_DataDict/UNIT_Assets.csv')
unit07_exded=pd.read_csv('./data/07_DataDict/UNIT_ExDed.csv')
unit07_inc=pd.read_csv('./data/07_DataDict/UNIT_Inc.csv')
per07_char=pd.read_csv('./data/07_DataDict/PERS_Char.csv')
per07_inc=pd.read_csv('./data/07_DataDict/PERS_Inc.csv')

################################
        #2017 Datasets
################################

unit17_demo= pd.read_csv('./data/17_DataDict/UNIT_Demo.csv')
unit17_assets=pd.read_csv('./data/17_DataDict/UNIT_Assets.csv')
unit17_exded=pd.read_csv('./data/17_DataDict/UNIT_ExDed.csv')
unit17_inc=pd.read_csv('./data/17_DataDict/UNIT_Inc.csv')
per17_char=pd.read_csv('./data/17_DataDict/PERS_Char.csv')
per17_inc=pd.read_csv('./data/17_DataDict/PERS_Inc.csv')

################################
    #Correlated Features
################################

corr_features = pd.read_csv("./data/corr_features.csv")
