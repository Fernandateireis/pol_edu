import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('/home/freitas/Downloads/internet2/data/merge_iex_censo_banco.csv')

tpot_data = tpot_data.drop(columns='SG_UF')
features = tpot_data.drop('IEX', axis=1)

training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['IEX'], random_state=42)

# Average CV score on the training set was: -2.8237191312334575
exported_pipeline = KNeighborsRegressor(n_neighbors=68, p=2, weights="distance")
# Fix random state in exported estimator
if hasattr(exported_pipeline, 'random_state'):
    setattr(exported_pipeline, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features

#cv results
from sklearn.model_selection import cross_val_score
result = cross_val_score(exported_pipeline, features, tpot_data['target'],
                         cv=5, scoring='mean_squared_error')
result['test_score'].mean()
