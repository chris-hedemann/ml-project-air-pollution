import numpy as np
import pandas as pd
import metpy.calc
from metpy.units import units


#Define PM2.5 Concentrations for Catagories
def create_target_labels(df):
    conditions = [
        (df['target'] <= 25),
        (df['target'] > 25) & (df['target'] <= 50),
        (df['target'] > 50) 
        ]

    # create a list of the values we want to assign for each condition
    values = [0, 1, 2]

    # create a new column and use np.select to assign values to it using our lists as arguments
    df['target_cat'] = np.select(conditions, values)

    return df


def create_wind(df):
    uwind = np.array(df['u_component_of_wind_10m_above_ground']) * units('m/s')
    vwind = np.array(df['v_component_of_wind_10m_above_ground']) * units('m/s')

    df['winddir'] = metpy.calc.wind_direction(uwind, vwind)
    df['windspeed'] = metpy.calc.wind_speed(uwind, vwind)

    df = df.drop('u_component_of_wind_10m_above_ground', axis=1)
    df = df.drop('v_component_of_wind_10m_above_ground', axis=1)

    return df


def time_features(df):
    # convert to pd datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    # create a column with the  weekday
    df['weekday'] = df.Date.dt.dayofweek # Monday = 0

    return df


def prior_features(df,
                   list_features_shift=['Place_ID','precipitable_water_entire_atmosphere',
        'relative_humidity_2m_above_ground',
        'specific_humidity_2m_above_ground', 'temperature_2m_above_ground', 
        'winddir', 'windspeed']):
    '''Function to create a dataframe with values of the prior day. Might result in missing rows (when no prior day is found)
    Args:   df DataFrame
            lists with features to keep or drop
    Returns: df'''
      
    list_features_drop = ['Place_ID_prior', 'deltatime', 'bool_arr', 'bool_arr2']

    # create new dataframe trunk with data of the days including target values
    df_next = df

    # copy df and create new columns with suffix _prior in name
    df_prior = df[list_features_shift]
    df_prior = df_prior.add_suffix('_prior')

    # shift all variables to the next value
    df_shift = df_prior.shift(periods=1)  

    # concat them with the new dataframe
    df_concat = pd.concat([df_next, df_shift], axis=1)

    # compare the Place_ID and Date columns of the regular dataframe with the ones of the prior

    list_columns = list(df_prior.columns) #columns of all variables that are from the day prior

    # create column with timedelta
    df_concat['deltatime'] = (df_concat['Date']-df_concat['Date'].shift()).fillna(pd.Timedelta('0 days'))

    # If timedelta is 1 day and they are the same location, then the values in the row are the ones of the day prior
    # Else: fill with nan , because they do not belong to the same location and no values for the prior day are available
    df_concat['bool_arr'] = (df_concat.deltatime != '1 days')
    df_concat['bool_arr2'] = ((df_concat['Place_ID'] != df_concat['Place_ID_prior']))

    df_concat.loc[(df_concat['bool_arr'] == True), list_columns] = np.nan # not next day
    df_concat.loc[(df_concat['bool_arr2'] == True), list_columns] = np.nan # not same location

    #drop unnecessary columns
    df_concat = df_concat.drop(columns = list_features_drop, axis=1)
    
    # return a new dataframe with the new features (concat)
    return df_concat