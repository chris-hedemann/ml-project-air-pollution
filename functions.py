


## Time Series Test Train Split

def test_train_time_split(data,target_name,date_name,test_size=0.25):
    '''Returns train-test split for time series data, ensuring that 
    data later in time are preserved for the test sample'''

    sorted_data = data.sort_values(date_name)
    n_obs = data.shape[0]
    arg_split = int( n_obs * (1. - test_size) )    ### for Place ID ? 

    train, test = sorted_data[0:arg_split+1], sorted_data[arg_split+1:]
    X_train, X_test = train.drop(target_name,axis=1), test.drop(target_name, axis=1)
    y_train, y_test = train[target_name], test[target_name]

    return X_train, X_test, y_train, y_test