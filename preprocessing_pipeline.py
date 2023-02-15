import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


def convert_0_to_nan(df,features):
    ''' 
    Returns a dataframe where zeros in selected features 
    are replaced with nans
    '''
    for feature in features:
        df[feature][df[feature] == 0.] = np.nan
    return df


def convert_labels(y,bins=[0,12.5,30,np.inf]):
    ''' 
    Returns a dataframe where zeros in selected features 
    are replaced with nans
    '''
    target_label = pd.cut(y,bins=bins,labels=False, include_lowest=True)
    return target_label


def test_train_time_split(data,target_name,date_name,test_size=0.25):
    '''Returns train-test split for time series data, ensuring that 
    data later in time are preserved for the test sample'''

    sorted_data = data.sort_values(date_name)
    n_obs = data.shape[0]
    arg_split = int( n_obs * (1. - test_size) )

    train, test = sorted_data[0:arg_split+1], sorted_data[arg_split+1:]
    X_train, X_test = train.drop(target_name,axis=1), test.drop(target_name, axis=1)
    y_train, y_test = train[target_name], test[target_name]

    return X_train, X_test, y_train, y_test

def make_pipeline(qnt_cols,cat_cols):

    qnt_pipeline = Pipeline([
        ('scale_qnt', StandardScaler()),
        ('impute_qnt', SimpleImputer(strategy='median')),
    ]) # columns with quantitative data

    cat_pipeline = Pipeline([
        ('impute_cat', SimpleImputer(strategy='constant', fill_value='missing')),
        ('ohe_cat', OneHotEncoder(handle_unknown='ignore'))
    ]) # columns with categorical data

    if cat_cols==None:
            preprocessor = ColumnTransformer([
            ('qnt', qnt_pipeline, qnt_cols)
        ]) # only quant to transform
    
    else:
        preprocessor = ColumnTransformer([
            ('qnt', qnt_pipeline, qnt_cols),
            ('cat', cat_pipeline, cat_cols)
        ]) # combining quant and cat to column transformer

    return preprocessor

