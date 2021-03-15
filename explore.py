import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
import sklearn.preprocessing

import acquire
import prepare
from wrangle import wrangle_telco


def plot_variable_pairs(df):
    '''
    This function will accept a dataframe as input 

    and plot all the pairwise relationships with the regression line for each pair
    '''
    sns.pairplot(df, 
                kind = "reg", 
                plot_kws = {'line_kws': {'color': 'red'}}) 




def months_to_years(df):
    '''
    This function will accept my telco-churn dataframe  

    and return a df with a new feature tenure_years, in complete years
    '''
    df['tenure_years'] = (df.tenure//12)
    return df




def plot_categorical_and_continuous_vars(df, categorical_var, continuous_var):
    '''
    This function will accept my dataframe 
    and the names of the cols that hold the categorical and continuous features,

    and output 3 different plots for visualizing a categorical var and a continuous var
    '''
    sns.barplot(data=df, y=continuous_var, x=categorical_var)
    plt.show()
    sns.swarmplot(data=df, y=continuous_var, x=categorical_var)
    plt.show()
    sns.boxplot(data=df, y=continuous_var, x=categorical_var)