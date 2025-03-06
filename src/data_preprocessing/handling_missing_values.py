import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def handling_few_missing_values(dataset):
    dataset['Movie Runtime'].fillna(dataset['Movie Runtime'].mode()[0], inplace=True)
    dataset['Writers'].fillna('Unknown', inplace=True)
    dataset['Language'].fillna(dataset['Language'].mode()[0], inplace=True)
    dataset['IMDB Vote Count'].fillna(int(dataset['IMDB Vote Count'].median()), inplace=True)
    dataset['IMDB Rating'].fillna(dataset['IMDB Rating'].mean(), inplace=True)
    dataset["RT Rating"].fillna(int(dataset["RT Rating"].mean()), inplace=True)
    return dataset

# def handling_many_missing_values(dataset):
#     df_missing = dataset[dataset[target_col].isna()]
#     df_not_missing = dataset[~dataset[target_col].isna()]
#
#     model = RandomForestRegressor()
#     X = df_not_missing[feature_cols]
#     y = df_not_missing[target_col]
#     model.fit(X, y)
#
#     X_missing = df_missing[feature_cols]
#     df.loc[df[target_col].isna(), target_col] = model.predict(X_missing)
#
# # Impute Domestic Gross
#     impute_with_model(df, 'Domestic Gross', ['IMDB Rating', 'Movie Runtime', 'IMDB Vote Count'])