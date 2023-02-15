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
    values = ['Good', 'Fair', 'Poor']

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
