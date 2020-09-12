#########################################################
# Py_Scripts.py
#   - Custom functions for all named functions in SNAP datasets.
#
# These functions were moved into this file
#   for reuse and to reduce Notebook complexity.
#########################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
import python_code.Reference as ref


#New Mexico
nm07_orig = pd.read_csv('./data/nm07.csv')
nm17_orig = pd.read_csv('./data/nm17.csv')

#Nebraska
ne07_orig = pd.read_csv('./data/ne07.csv')
ne17_orig = pd.read_csv('./data/ne17.csv')

#New Mexico
nm07 = pd.read_csv('./data/nm07.csv')
nm17 = pd.read_csv('./data/nm17.csv')

#Nebraska
ne07 = pd.read_csv('./data/clean_ne07.csv')
ne17 = pd.read_csv('./data/clean_ne17.csv')
################
    #EDA
################

def impute_df(df):
    """Returns a dataframe with mean imputed values for NaN."""
    my_imputer = SimpleImputer(missing_values=np.nan)
    data_with_imputed_values = pd.DataFrame(my_imputer.fit_transform(df),columns = df.columns)
    return data_with_imputed_values

def only_zero(df):
    """Drops all columns that are all zero values and returns a Dataframe."""
    filter = pd.DataFrame(df.sum(axis=0)==0, columns=['value'])
    filter = filter.loc[filter['value']==True]
    col = list(filter.index)
    return df.drop(col,axis=1)

################################
    #Correlations
################################

def corr_df(fullname, dataset):
    """Creates a dataframe on .corr(), used for unit categories."""
    fullname_df = pd.DataFrame()
    for feature in fullname['Table 1']:
        try:
            fullname_df[feature] = dataset[feature]
        except:
            continue
    fullname_df['CAT_ELIG']=dataset['CAT_ELIG'].astype("float64")
    return fullname_df

def corr_numcol(fullname,dataset):
    """Creates a dataframe on .corr(), used for personal characteristics categories."""
    fullname_df=pd.DataFrame()
    for feature in fullname['Table 1']:
        feature = feature[:-1]
        for num in range(1,17):
            combo=str(feature+str(num))
            try:
                fullname_df[combo]=dataset[combo]
            except:
                continue
    fullname_df['CAT_ELIG']=dataset['CAT_ELIG'].astype('float64')
    return fullname_df

def plot_simple_features(column,img_name,description):
    """Plots features on a countplot, used for columns with binary values and for EDA datasets."""
    plt.figure(figsize = (16,10))
    plt.suptitle(description, fontsize=20)
    idx = 221
    while idx<225:
        for key,value in {'nm07':nm07_orig,'nm17':nm17_orig,'ne07':ne07_orig,'ne17':ne17_orig}.items():
            mean = value[column].mean()
            ax = plt.subplot(idx)
            plt.title(f'$\it{key.upper()}$')
            sns.countplot(value[column],palette="husl")
            ax.axhline(mean,linewidth=1,color='r')
            ax.set_xlabel('')
            #ax.set_xticklabels([0,1])
            idx +=1
    plt.savefig("./images/ind_features/" + str(img_name) + ".png")
    

def plot_features(column,img_name,description):
    """Plots features on a countplot, used for columns with binary values."""
    plt.figure(figsize = (16,10))
    plt.suptitle(description, fontsize=20)
    idx = 221
    while idx<225:
        for key,value in {'nm07':nm07,'nm17':nm17,'ne07':ne07,'ne17':ne17}.items():
            ax = plt.subplot(idx)
            plt.title(f'$\it{key.upper()}$')
            sns.countplot(value[column])
            ax.axhline(y=value[value[column]==1][column].size,linewidth=1,color='r')
            ax.set_xlabel('')
            ax.set_xticklabels([0,1])
            idx +=1
    plt.savefig("./images/ind_features/" + str(img_name) + ".png")

def plot_features_hist(column,img_name,description):
    """Plots features on a histogram, best for currency columns"""
    plt.figure(figsize = (16,10))
    plt.suptitle(description, fontsize=20)
    idx = 221
    while idx<225:
        for key,value in {'nm07':nm07,'nm17':nm17,'ne07':ne07,'ne17':ne17}.items():
            ax = plt.subplot(idx)
            plt.title(f'$\it{key.upper()}$')
            plt.hist(value[column],bins=20,range=(1,value[column].max()))
            ax.set_xlabel(f"Number of zero's:{value[value[column]==0][column].count()}")
            ax.xaxis.set_label_coords(0.15, 1.05)
            idx +=1
    plt.savefig("./images/ind_features/" + str(img_name) + ".png")
    
def final(fullname, dataset):
    """Returns a sliced dataset of columns found in corr_features list."""
    fullname_df = pd.DataFrame()
    for feature in fullname:
        try:
            fullname_df[feature] = dataset[feature]
        except:
            continue
    fullname_df['CAT_ELIG']=dataset['CAT_ELIG']
    return fullname_df

################################
    #Predictions
################################

def clean_data_to_predict(dataset):
    """Cleans new datasets for processing through prediction"""
    fullname_df = pd.DataFrame()
    fullname_df['state']=dataset['STATENAME']
    for feature in ref.corr_features['Table 1']:
        try:
            fullname_df[feature] = dataset[feature].astype('float64')
        except:
            continue
    fullname_df['VEHICLEA']=fullname_df['VEHICLEA'].fillna(1) #set nulls to 1 for "no car"
    fullname_df=fullname_df.dropna() #drop the remaining null values out of the reduced column set
    return fullname_df

def top_coef_df(fullname, dataset):
    """Creates a dataframe on .corr(), used for unit categories."""
    fullname_df = pd.DataFrame()
    for ea in fullname['feature']:
        try:
            fullname_df[ea] = dataset[ea]
        except:
            continue
    fullname_df['state']=dataset['state']
    return fullname_df